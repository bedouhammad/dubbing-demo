import json
from faster_whisper import WhisperModel

AUDIO = "work/clean.wav"
OUT_JSON = "work/transcript.json"
OUT_TXT  = "work/transcript.txt"

print("Loading model...")
model = WhisperModel("small", device="cpu", compute_type="int8")

print("Starting transcription...")
segments, info = model.transcribe(
    AUDIO,
    language="en",
    vad_filter=True
)

segments = list(segments)
print("Segments found:", len(segments))

if len(segments) == 0:
    print("ERROR: No segments were transcribed.")
    exit(1)

data = {
    "language": info.language,
    "duration": info.duration,
    "segments": []
}

for s in segments:
    text = s.text.strip()
    if text:
        data["segments"].append({
            "start": s.start,
            "end": s.end,
            "text": text
        })

with open(OUT_JSON, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open(OUT_TXT, "w", encoding="utf-8") as f:
    for seg in data["segments"]:
        f.write(seg["text"] + "\n")

print("DONE.")
print("Wrote:", OUT_JSON)
print("Wrote:", OUT_TXT)

