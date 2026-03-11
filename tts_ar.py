import os
import subprocess

INPUT_FILE = "translated.txt"
OUT_DIR = "tts_out"

os.makedirs(OUT_DIR, exist_ok=True)

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    lines = [l.strip() for l in f.readlines() if l.strip()]

for i, line in enumerate(lines, start=1):
    # نتوقع الشكل: Speaker 1: ....
    if ":" in line:
        speaker, text = line.split(":", 1)
    else:
        speaker, text = "Speaker", line

    speaker = speaker.strip().replace(" ", "_")
    text = text.strip()

    aiff_path = os.path.join(OUT_DIR, f"{i:03d}_{speaker}.aiff")
    wav_path  = os.path.join(OUT_DIR, f"{i:03d}_{speaker}.wav")

    # توليد AIFF بصوت عربي موجود عندك (Majed)
    subprocess.run(["say", "-v", "Majed", text, "-o", aiff_path], check=True)

    # تحويل AIFF إلى WAV
    subprocess.run(["ffmpeg", "-y", "-i", aiff_path, wav_path], check=True)

print(f"Done. WAV files are in: {OUT_DIR}")

