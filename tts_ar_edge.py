import os
import subprocess

INPUT_FILE = "translated.txt"
OUT_DIR = "tts_out"

# Voices (يمكن تغييرهم لاحقاً)
VOICE_FEMALE = "ar-SA-ZariyahNeural"  # Speaker 1 (Female)
VOICE_MALE   = "ar-SA-HamedNeural"    # Speaker 2 (Male)

os.makedirs(OUT_DIR, exist_ok=True)

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    lines = [l.strip() for l in f.readlines() if l.strip()]

for i, line in enumerate(lines, start=1):
    # نتوقع الشكل: Speaker 1: ....
    if ":" in line:
        speaker, text = line.split(":", 1)
    else:
        speaker, text = "Speaker", line

    speaker_raw = speaker.strip().lower()
    speaker_norm = speaker_raw.replace(" ", "").replace("_", "")

    # التقاط Speaker 1/2 حتى لو الصيغة مختلفة
    is_speaker1 = ("speaker1" in speaker_norm) or (speaker_norm == "s1")
    is_speaker2 = ("speaker2" in speaker_norm) or (speaker_norm == "s2")

    # Speaker 1 = Female, Speaker 2 = Male (والافتراضي Male لو غير معروف)
    voice = VOICE_FEMALE if is_speaker1 else VOICE_MALE

    # اسم ثابت للملفات
    speaker_key = "speaker1" if is_speaker1 else "speaker2"

    text = text.strip()

    out_mp3 = os.path.join(OUT_DIR, f"{i:03d}_{speaker_key}.mp3")
    out_wav = os.path.join(OUT_DIR, f"{i:03d}_{speaker_key}.wav")

    # 1) TTS إلى MP3
    subprocess.run(
        ["edge-tts", "--voice", voice, "--text", text, "--write-media", out_mp3],
        check=True
    )

    # 2) تحويل مضمون إلى WAV قياسي (يدعم afplay ودمج ffmpeg بسهولة)
    subprocess.run(
        ["ffmpeg", "-y", "-i", out_mp3, "-ac", "1", "-ar", "44100", "-c:a", "pcm_s16le", out_wav],
        check=True
    )

print("Done. Created MP3 + WAV segments in tts_out/")

