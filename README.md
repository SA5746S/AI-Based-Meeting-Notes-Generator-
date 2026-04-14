# AI-Based-Meeting-Notes-Generator-

AI-Based Meeting Notes Generator
📌 Project Overview

The AI-Based Meeting Notes Generator is a Python-based AI system that converts meeting audio into structured text notes. It uses Speech Recognition and Natural Language Processing (NLP) to generate transcripts, summaries, and action items automatically.

This project is designed for students and professionals to automate meeting documentation and improve productivity.

🚀 Features
🎤 Speech-to-Text conversion (Audio → Text)
🧠 AI-based text summarization
📌 Automatic action item extraction
💾 Save meeting notes to file
🌐 Optional Flask web interface

🛠️ Technologies Used
Python 3.10+
OpenAI Whisper / SpeechRecognition
HuggingFace Transformers
PyTorch
Flask (optional web UI)
Pydub (audio processing)

📁 Project Structure
meeting_notes_generator/
│
├── app.py
├── utils/
│   ├── speech_to_text.py
│   ├── summarizer.py
│   ├── action_items.py
│
├── sample_audio/
│   └── meeting.wav
│
├── output/
│   └── notes.txt
│
├── templates/
│   └── index.html
│
└── README.md

⚙️ Installation
1. Clone the repository
git clone https://github.com/your-username/meeting-notes-generator.git
cd meeting-notes-generator
2. Create virtual environment (recommended)
python -m venv venv
venv\Scripts\activate  # Windows
3. Install dependencies
pip install -r requirements.txt

If requirements.txt is not available:

pip install whisper transformers torch flask pydub speechrecognition


▶️ How to Run
CLI Version
python app.py

Then enter audio file path:

sample_audio/meeting.wav

🌐 Flask Web Version (optional)
python app.py

Open browser:

http://127.0.0.1:5000
📊 Output Example
Input

Audio meeting file (.wav)

Output
FULL TRANSCRIPT:
- Meeting speech converted to text


SUMMARY:
- Key points of discussion


ACTION ITEMS:
- Task 1 assigned to member A
- Task 2 deadline set

🧠 Working Flow
Audio Input
   ↓
Speech-to-Text (Whisper)
   ↓
Text Processing (NLP)
   ↓
Summarization + Action Extraction
   ↓
Final Meeting Notes

📌 Applications
Corporate meetings
Online classes
Project discussions
Interview transcription

⚠️ Limitations
Accuracy depends on audio quality
Background noise may affect results
Speaker identification is optional and complex
🔮 Future Improvements 
Real-time meeting transcription
Zoom / Google Meet integration
Speaker diarization
Multilingual support
Cloud deployment

👨‍💻 Author

Shibnath Sahoo

📜 License

This project is for academic purposes only.
