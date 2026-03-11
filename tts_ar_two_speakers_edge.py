import asyncio
import edge_tts
import os
import re

INPUT = "work/dialogue_ar.txt"
OUT_DIR = "work/tts_two"

VOICE_FEMALE = "ar-SA-ZariyahNeural"
VOICE_MALE   = "ar-SA-HamedNeural"

os.makedirs(OUT_DIR, exist_ok=True)

def pick_voice(label: str) -> str:
    # SPEAKER_1 = female, SPEAKER_2 = male
    if "SPEAKER_1" in label:
        return VOICE_FEMALE
    return VOICE_MALE

async def synth_line(i: int, label: str, text: str):
    voice = pick_voice(label)
    out_file = os.path.join(OUT_DIR, f"{i:04d}_{label}.wav")
    communicate = edge_tts.Communicate(
        text=text,
        voice=voice,
        rate="+0%",
        pitch="+0Hz"
    )
    await communicate.save(out_file)
    print("Saved:", out_file)

async def main():
    with open(INPUT, "r", encoding="utf-8") as f:
        lines = [l.strip() for l in f if l.strip()]

    idx = 0
    for line in lines:
        if ":" not in line:
            continue
        label, text = line.split(":", 1)
        label = label.strip()
        text = text.strip()
        if not text:
            continue

        idx += 1
        # تنظيف بسيط
        text = re.sub(r"\s+", " ", text).strip()
        await synth_line(idx, label.replace(" ", "_"), text)

asyncio.run(main())

