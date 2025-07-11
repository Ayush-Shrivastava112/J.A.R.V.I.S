# J.A.R.V.I.S
J.A.R.V.I.S is an AI-powered voice assistant built with Python that responds to your commands, plays music, fetches news, opens websites, and features a glowing 3D visual interface inspired by Iron Man’s JARVIS.
🚀 Features

- 🎤 Voice-controlled commands (online/offline)
- 🗣️ Text-to-speech responses (offline)
- 🌐 Opens websites and searches queries
- 📰 Fetches live news using NewsAPI
- 🎵 Plays music via custom YouTube library
- 🕒 Tells time and date
- 🌌 Glowing 3D blue orb visual UI using `pygame`


---

## 🛠️ Technologies Used

| Category              | Tech Stack                                       |
|-----------------------|--------------------------------------------------|
| Voice Recognition     | `speech_recognition`, `vosk` (optional)          |
| Text-to-Speech (TTS)  | `pyttsx3`                                        |
| APIs & Web Access     | `requests`, `webbrowser`, `NewsAPI`, `OpenAI`   |
| GUI & Visuals         | `pygame` (rotating blue orb)                     |
| System Utilities      | `os`, `datetime`, `json`                         |
| Programming Language  | Python 3.8+                                      |

---

## 🖥️ Setup Instructions

### 1. **Clone the Repository**
```bash
git clone https://github.com/Ayush-Shrivastava112/jarvis-ai.git
cd jarvis-ai
2. Create Virtual Environment (Optional but Recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Download Vosk Model (if using offline recognition)
5. Download google Model (if using online recognition)

Extract and place as a folder named model in your project root.

5. Add Your API Keys
Get a free key from NewsAPI.org

Optional: Add OpenAI key for AI-based response(Paid)

python
Copy
Edit
# In your script (e.g., client.py)
newsapi = "your-newsapi-key"
openai.api_key = "your-openai-key"(not pasting my api key for security)
▶️ How to Use
bash
Copy
Edit
python jarvis.py
Then speak any command:

"What's the news today?"
"Play some music"
"Open YouTube"
"What's the time?"

🌀 Visual Interface (Optional)
pygame is used to render a glowing rotating 3D orb

It activates when JARVIS is listening/responding

🧪 Example Commands
Command	Action
"Play Shape of You"	Plays YouTube song
"Tell me the news"	Reads latest news headlines
"What's the time?"	Speaks current system time
"Open Google"	Opens Google in browser

📁 Project Structure
bash
Copy
Edit
jarvis-ai/
│
├── musiclibrary.py        # Custom music commands
├── jarvis.py              # Main voice assistant script
├── client.py              # Optional OpenAI client
├── orb_ui.py              # Visual orb interface using pygame
├── requirements.txt
├── .gitignore
└── README.md
