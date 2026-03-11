replacements = {
    "منظمة العفو الدولية": "الذكاء الاصطناعي",
}

INPUT_FILE = "work/translated_ar.txt"
OUTPUT_FILE = "work/translated_ar_fixed.txt"

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    text = f.read()

for old, new in replacements.items():
    text = text.replace(old, new)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(text)

print("تم تعديل الترجمة ✔")
print("الملف الجديد:", OUTPUT_FILE)

