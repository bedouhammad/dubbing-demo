from mishkal.tashkeel import TashkeelClass

INPUT = "work/translated_ar_fixed.txt"
OUTPUT = "work/translated_ar_fixed_tashkeel.txt"


t = TashkeelClass()

with open(INPUT, "r", encoding="utf-8") as f:
    lines = [l.strip() for l in f if l.strip()]

with open(OUTPUT, "w", encoding="utf-8") as out:
    for line in lines:
        # تشكيل السطر
        out.write(t.tashkeel(line) + "\n")

print("DONE.")
print("Wrote:", OUTPUT)

