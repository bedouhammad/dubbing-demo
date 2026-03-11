import re
from pathlib import Path

SRT_PATH = Path("work/wx_test/english.srt")
OUT_PATH = Path("work/dialogue_en.txt")

def parse_srt(srt_text: str):
    # يرجّع قائمة بلوكات نصية من الـ SRT
    blocks = re.split(r"\n\s*\n", srt_text.strip())
    lines = []
    for b in blocks:
        parts = b.strip().splitlines()
        if len(parts) < 3:
            continue
        # parts[0] رقم، parts[1] توقيت، والباقي نص
        text = " ".join(p.strip() for p in parts[2:] if p.strip())
        text = re.sub(r"\s+", " ", text).strip()
        if text:
            lines.append(text)
    return lines

def main():
    if not SRT_PATH.exists():
        raise SystemExit(f"مش لاقي الملف: {SRT_PATH}")

    srt = SRT_PATH.read_text(encoding="utf-8", errors="ignore")
    turns = parse_srt(srt)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    speaker = 1
    with OUT_PATH.open("w", encoding="utf-8") as f:
        for i, t in enumerate(turns, start=1):
            # بدّل المتحدث كل بلوك (Demo)
            f.write(f"SPEAKER_{speaker}: {t}\n")
            speaker = 2 if speaker == 1 else 1

    print("Saved:", OUT_PATH, "| lines:", len(turns))

if __name__ == "__main__":
    main()

