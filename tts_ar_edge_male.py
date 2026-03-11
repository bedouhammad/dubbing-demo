import asyncio
import edge_tts
import os

INPUT = "work/translated_ar_fixed_tashkeel.txt"
OUT_DIR = "work/tts_male"
VOICE = "ar-SA-HamedNeural"

START_FROM = 285  # غير الرقم لو حابب

os.makedirs(OUT_DIR, exist_ok=True)

async def main():
    with open(INPUT, "r", encoding="utf-8") as f:
        lines = [l.strip() for l in f if l.strip()]

    for i, line in enumerate(lines, start=1):
        # عدّي السطور اللي اتعملت قبل كده
        if i < START_FROM:
            continue

        out_file = f"{OUT_DIR}/{i:03d}.wav"

        communicate = edge_tts.Communicate(
            text=line,
            voice=VOICE,
            rate="+0%",
            pitch="+0Hz"
        )

        await communicate.save(out_file)
        print("Saved:", out_file)

asyncio.run(main())

