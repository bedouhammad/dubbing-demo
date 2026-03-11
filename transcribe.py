from faster_whisper import WhisperModel

# تحميل موديل التفريغ (متوسط – مناسب للماك)
model = WhisperModel("medium", device="cpu", compute_type="int8")

# تفريغ الصوت الإنجليزي
segments, info = model.transcribe("demo.wav", language="en")

# طباعة النص
for segment in segments:
    print(segment.text)

