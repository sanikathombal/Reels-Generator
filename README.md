# Reels-Generator

# 🎬 VidSnapAI

VidSnapAI is a **Flask-based web application** that automatically creates short video reels from **uploaded images and text**, using **AI-generated voiceovers** and **FFmpeg**.  
It is designed to quickly turn image folders into engaging reels with narration.

---

## 🚀 Features

- 📸 Upload multiple images (JPG / PNG / JPEG)
- 📝 Convert text into AI-generated voice (using ElevenLabs)
- 🎥 Automatically generate video reels using FFmpeg
- 🖼️ Gallery view to see generated reels
- 🔁 Background process that continuously checks for new uploads
- ⚡ Simple folder-based workflow

---

## 🛠️ Tech Stack

- **Python**
- **Flask** – Web framework
- **ElevenLabs API** – Text-to-speech (AI voice)
- **FFmpeg** – Image + audio to video conversion
- **HTML / CSS** – Frontend templates

---

## ⚙️ Installation & Setup

### 1️⃣ Install Dependencies
```bash
pip install -U elevenlabs
pip install flask
2️⃣ Configure API Key
Add your ElevenLabs API key in config.py:

python
Copy code
ELEVENLABS_API_KEY = "your_api_key_here"
3️⃣ Run the Flask App
bash
Copy code
python main.py
4️⃣ Start Background Generator (New Terminal)
bash
Copy code
python generate_process.py
🧑‍💻 How It Works
Upload only image files (.jpg, .jpeg, .png)

A unique folder is created inside user_uploads/

Add a desc.txt file containing narration text

The background script:

Converts text → AI voice (audio.mp3)

Combines images + audio using FFmpeg

Saves the final reel in static/reels/

Processed folders are tracked in done.txt

⚠️ Important Notes
❗ Only JPG images are recommended
(Other formats may cause FFmpeg errors)

🔐 ElevenLabs API is paid

🖥️ FFmpeg must be installed and accessible via command line

🔄 Do not delete done.txt while the app is running

📌 Future Improvements
Background music support

Custom video duration per image

Better error handling

Docker support

Cloud storage integration

📂 Output Location
Generated video reels are saved in:

swift
Copy code
static/reels/
Gallery view is available at:

bash
Copy code
/gallery



