from transformers import pipeline

INP = "work/dialogue_en.txt"
OUT = "work/dialogue_ar.txt"

print("Loading translator...")
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-ar", device=0)  # على Mac غالباً device=0 = mps لو متاح، لو علّق خليها -1

lines_out = []
with open(INP, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        if ":" not in line:
            lines_out.append(line)
            continue

        label, text = line.split(":", 1)
        label = label.strip()
        text = text.strip()

        if not text:
            lines_out.append(f"{label}:")
            continue

        # ترجمة
        ar = translator(text, max_length=512)[0]["translation_text"].strip()
        lines_out.append(f"{label}: {ar}")

with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines_out) + "\n")

print("Saved:", OUT)

