import whisper  

model = whisper.load_model("medium")

audio = whisper.load_audio("recording.ogg")
audio = whisper.pad_or_trim(audio)

mel = whisper.log_mel_spectrogram(audio).to(model.device)

_, probs = model.detect_language(mel)
detected_language = max(probs, key=probs.get)
print(f"Detected language: {detected_language}")

options = whisper.DecodingOptions()
result = whisper.decode(model, mel, options)

print("Transcribed text:", result.text)
