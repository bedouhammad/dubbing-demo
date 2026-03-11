import glob
import os
import json
from faster_whisper import WhisperModel

CHUNKS_GLOB = "work/chunks/chunk_*.wav"
OUT_TXT = "work/transcript.txt"
OUT_JSON = "work/transcript.json"

# أسرع/أخف على Mac Air. لو الجودة غير كافية نرفع لـ small لاحقاً.
MODEL_NAME = "small"
LANG = "en"

print("Loading model:", MODEL_NAME)
model = WhisperModel(MODEL_NAME, device="cpu", compute_type="int8")

chunk_files = sorted(glob.glob(CHUNKS_GLOB))
if not chunk_files:
    raise SystemExit("No chunks found in work/chunks/")

all_segments = []
total_chunks = len(chunk_files)

with open(OUT_TXT, "w", encoding="utf-8") as out_txt:
    for idx, wav_path in enumerate(chunk_files):
        print(f"\n[{idx+1}/{total_chunks}] Transcribing: {os.path.basename(wav_path)}")

        segments, info = model.transcribe(
    wav_path,
    language=LANG,
    vad_filter=True,
    beam_size=5,
    best_of=5,
    temperature=0.0
)

        )

        segments = list(segments)
        print("  Segments:", len(segments))

        # إزاحة الزمن حسب ترتيب الشانكات (كل شانك 10 دقائق = 600 ثانية)
        # هذا تقريبي للديمو. لاحقاً نستخدم مدة كل شانك بدقة.
        time_offset = idx * 600.0

        for s in segments:
            text = s.text.strip()
            if not text:
                continue

            start = float(s.start) + time_offset
            end = float(s.end) + time_offset

            all_segments.append({"start": start, "end": end, "text": text})
            out_txt.write(text + "\n")

# JSON منظم
data = {
    "language": LANG,
    "chunk_count": total_chunks,
    "segments": all_segments
}

with open(OUT_JSON, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\nDONE.")
print("Wrote:", OUT_TXT)
print("Wrote:", OUT_JSON)

