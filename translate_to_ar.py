from transformers import pipeline

INPUT = "work/transcript.txt"
OUTPUT = "work/translated_ar.txt"

print("Loading translator...")
translator = pipeline(
    "translation",
    model="Helsinki-NLP/opus-mt-en-ar"
)

with open(INPUT, "r", encoding="utf-8") as f:
    lines = [l.strip() for l in f if l.strip()]

with open(OUTPUT, "w", encoding="utf-8") as out:
    for line in lines:
        ar = translator(line, max_length=400)[0]["translation_text"]
        out.write(ar + "\n")

print("DONE.")
print("Wrote:", OUTPUT)

