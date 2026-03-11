# 🎙️ Arabic Dubbing Demo

An end-to-end AI-powered pipeline that automatically **transcribes English audio**, **translates it to Arabic**, and **generates dubbed Arabic audio** — complete with two-speaker voice synthesis.

---

## 🚀 What It Does

This project takes an English audio file and produces a fully dubbed Arabic version through a multi-stage pipeline:

1. **Transcription** — Converts English speech to text using Whisper
2. **Translation** — Translates the transcript to Arabic
3. **Tashkeel (Diacritization)** — Adds Arabic diacritics for accurate pronunciation
4. **Text-to-Speech** — Synthesizes natural Arabic audio using Edge TTS with two-speaker support

---

## 🗂️ Project Structure

```
dubbing_demo/
│
├── transcribe.py                   # Transcribe audio to English text
├── transcribe_all_demo.py          # Batch transcription
├── transcribe_chunks.py            # Chunk-based transcription
├── transcribe_en.py                # English-specific transcription
│
├── translate.py                    # Core translation script
├── translate_to_ar.py              # Translate English text to Arabic
├── translate_dialogue_to_ar.py     # Dialogue-aware translation
├── fix_translation.py              # Post-process and fix translations
│
├── tashkeel_ar.py                  # Arabic diacritization
│
├── tts_ar.py                       # Arabic TTS (base)
├── tts_ar_edge.py                  # Arabic TTS using Edge TTS
├── tts_ar_edge_male.py             # Male voice TTS
├── tts_ar_two_speakers_edge.py     # Two-speaker Arabic dubbing
│
├── make_dialogue_demo.py           # Full pipeline demo runner
│
├── demo.wav                        # Sample input audio
├── transcript.txt                  # Generated transcript
├── translated.txt                  # Generated Arabic translation
├── final_demo_arabic.wav           # Final dubbed Arabic output
│
├── input/                          # Input audio files
├── tts_out/                        # TTS output audio files
├── work/                           # Intermediate working files
└── piper_voices/                   # Local TTS voice models
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| [OpenAI Whisper](https://github.com/openai/whisper) | Speech-to-text transcription |
| [Microsoft Edge TTS](https://github.com/rany2/edge-tts) | Neural Arabic voice synthesis |
| [Piper TTS](https://github.com/rhasspy/piper) | Local offline TTS engine |
| Python 3 | Core language |

---

## ⚙️ Setup & Installation

```bash
# Clone the repository
git clone https://github.com/bedouhammad/dubbing-demo.git
cd dubbing-demo

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ How to Run

**Full pipeline demo:**
```bash
python make_dialogue_demo.py
```

**Step by step:**
```bash
# Step 1: Transcribe
python transcribe.py

# Step 2: Translate to Arabic
python translate_to_ar.py

# Step 3: Generate dubbed audio
python tts_ar_two_speakers_edge.py
```

---

## 🎧 Example Output

- **Input:** `demo.wav` — English audio
- **Output:** `final_demo_arabic.wav` — Dubbed Arabic audio with two speakers

---

## 📌 Notes

- This is a local demo pipeline built and tested on macOS
- Arabic diacritization (`tashkeel`) is applied before TTS for more natural pronunciation
- Two-speaker mode simulates dialogue dubbing with distinct male/female voices

---

## 👤 Author

**Abdelrahman Hammad**  
[GitHub @bedouhammad](https://github.com/bedouhammad)
