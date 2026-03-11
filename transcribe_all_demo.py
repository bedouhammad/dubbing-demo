import glob
import os
import json
import subprocess
from faster_whisper import WhisperModel

# مهم: نقرأ فقط الـ chunks الأصلية (بدون أي _clean)
CHUNKS_GLOB = "work/chunks/chunk_[0-9][0-9][0-9].wav"

CLEAN_DIR = "work/chunks_clean"
OUT_TXT = "work/transcript.txt"
OUT_JSON = "work/transcript.json"

LANG = "en"
MODEL_NAME = "medium"
BEAM_SIZE = 5
CHUNK_SECONDS = 600.0

os.makedirs(CLEAN_DIR, exist_ok=True)

chunk_files = sorted(glob.glob(CHUNKS_GLOB))
if not chunk_files:
    raise SystemExit("No original chunks found in work/chunks/ (expected chunk_000.wav etc.)")

print("Loading model:", MODEL_NAME)
model = WhisperModel(MODEL_NAME, device="cpu", compute_type="int8")

all_segments = []

# نكتب تدريجيًا: يفضل تشوف نتائج أول بأول
with open(OUT_TXT, "w", encoding="utf-8") as out_txt:
    for idx, wav_path in enumerate(chunk_files):
        base = os.path.basename(wav_path)                # chunk_000.wav
        clean_name = base.replace(".wav", "_clean.wav")  # chunk_000_clean.wav
        clean_path = os.path.join(CLEAN_DIR, clean_name)

        print(f"\n[{idx+1}/{len(chunk_files)}] Cleaning: {base}")
        subprocess.run([
            "ffmpeg", "-y", "-i", wav_path,
            "-af", "highpass=f=80, lowpass=f=8000, loudnorm=I=-16:TP=-1.5:LRA=11",
            "-ac", "1", "-ar", "16000", "-c:a", "pcm_s16le",
            clean_path
        ], check=True)

        print(f"[{idx+1}/{len(chunk_files)}] Transcribing: {os.path.basename(clean_path)}")
        segments, _ = model.transcribe(
            clean_path,
            language=LANG,
            vad_filter=True,
            beam_size=BEAM_SIZE
        )

        segments = list(segments)
        print("  Segments:", len(segments))

        time_offset = idx * CHUNK_SECONDS

        # اكتب بعد كل chunk + flush
        for s in segments:
            text = s.text.strip()
            if not text:
                continue
            start = float(s.start) + time_offset
            end = float(s.end) + time_offset
            all_segments.append({"start": start, "end": end, "text": text})
            out_txt.write(text + "\n")

        out_txt.flush()
        print(f"[{idx+1}/{len(chunk_files)}] Wrote text so far: {out_txt.tell()} bytes")

data = {
    "language": LANG,
    "model": MODEL_NAME,
    "beam_size": BEAM_SIZE,
    "chunk_seconds": CHUNK_SECONDS,
    "chunk_count": len(chunk_files),
    "segments": all_segments
}

with open(OUT_JSON, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\nDONE.")
print("Wrote:", OUT_TXT)
print("Wrote:", OUT_JSON)
print("Cleaned chunks in:", CLEAN_DIR)

