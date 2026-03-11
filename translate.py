from transformers import pipeline

translator = pipeline(
    "translation",
    model="facebook/nllb-200-distilled-600M"
)

with open("transcript.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    if ":" in line:
        speaker, text = line.split(":", 1)
        result = translator(
            text.strip(),
            src_lang="eng_Latn",
            tgt_lang="arb_Arab"
        )
        print(f"{speaker}: {result[0]['translation_text']}")

