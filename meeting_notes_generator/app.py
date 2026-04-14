from utils.speech_to_text import audio_to_text
from utils.summarizer import summarize_text
import os

def main():
    print("\n📄 AI MEETING NOTES GENERATOR\n")

    audio_path = input("Enter audio file path (.wav): ")

    if not os.path.exists(audio_path):
        print("❌ File not found!")
        return

    # Step 1: Speech to Text
    text = audio_to_text(audio_path)

    if not text:
        print("❌ No text extracted!")
        return

    print("\n📜 FULL TRANSCRIPT:\n")
    print(text)

    # Step 2: Summarization
    summary = summarize_text(text)

    print("\n✨ SUMMARY:\n")
    print(summary)

    # Step 3: Save output
    os.makedirs("output", exist_ok=True)

    with open("output/notes.txt", "w", encoding="utf-8") as f:
        f.write("FULL TRANSCRIPT:\n")
        f.write(text)
        f.write("\n\nSUMMARY:\n")
        f.write(summary)

    print("\n✅ Saved to output/notes.txt")

if __name__ == "__main__":
    main()