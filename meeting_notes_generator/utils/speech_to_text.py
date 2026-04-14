import speech_recognition as sr

def audio_to_text(audio_file):
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(audio_file) as source:
            print("🎧 Loading audio...")
            audio = recognizer.record(source)

        print("📝 Converting speech to text...")

        text = recognizer.recognize_google(audio)

        return text

    except Exception as e:
        print("❌ Speech recognition error:", e)
        return ""