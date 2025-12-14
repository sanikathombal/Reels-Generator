<div align="center">

# 🎬 VidSnapAI  
### AI-Powered Video Reel Generator

Turn images and text into engaging AI-narrated video reels using Flask, ElevenLabs, and FFmpeg.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black)
![FFmpeg](https://img.shields.io/badge/FFmpeg-Video%20Processing-green)
![AI](https://img.shields.io/badge/AI-Text--to--Speech-purple)
![Status](https://img.shields.io/badge/Status-Active-success)

</div>

---

## 📌 Overview

**VidSnapAI** is a full-stack Python web application that automatically converts image collections and descriptive text into short, AI-narrated video reels.

The project demonstrates:
- AI integration (Text-to-Speech)
- Backend automation
- Media processing with FFmpeg
- Scalable folder-based workflows

Ideal for **content creators**, **automation demos**, and **AI portfolio projects**.

---

## ✨ Key Features

- 📸 Multi-image upload support (`.jpg`, `.jpeg`, `.png`)
- 🧠 AI voice generation using **ElevenLabs**
- 🎥 Automated video creation with **FFmpeg**
- 🖼️ Built-in gallery to preview generated reels
- 🔁 Background worker for continuous processing
- ⚡ Simple, scalable, and efficient architecture

---

## 🧰 Tech Stack

| Layer        | Technology |
|--------------|------------|
| Backend      | Python, Flask |
| AI / Voice   | ElevenLabs API |
| Video Engine | FFmpeg |
| Frontend     | HTML, CSS |
| Automation   | Background Python Process |

---

## 🏗️ Architecture

User Upload
↓
Image Folder + desc.txt
↓
AI Text-to-Speech
↓
Audio + Images
↓
FFmpeg Video Rendering
↓
Final Reel (static/reels/)

yaml
Copy code

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/VidSnapAI.git
cd VidSnapAI
2️⃣ Install Dependencies
bash
Copy code
pip install flask
pip install -U elevenlabs
3️⃣ Configure API Key
Edit config.py:

python
Copy code
ELEVENLABS_API_KEY = "your_api_key_here"
4️⃣ Run the Application
bash
Copy code
python main.py
5️⃣ Start Background Processor (New Terminal)
bash
Copy code
python generate_process.py
🧑‍💻 How It Works
Upload image files via the web interface

A unique folder is created in user_uploads/

Add narration text inside desc.txt

Background service:

Converts text → AI voice

Combines images + audio via FFmpeg

Saves output to static/reels/

Completed folders are tracked using done.txt

📂 Project Structure
csharp
Copy code
VidSnapAI/
│
├── main.py                 # Flask web app
├── generate_process.py     # Background reel generator
├── text_to_audio.py        # ElevenLabs integration
├── config.py               # API configuration
├── done.txt                # Processed folder tracker
│
├── user_uploads/           # Input images & text
├── static/
│   └── reels/              # Generated videos
└── templates/              # Frontend HTML files
⚠️ Important Notes
❗ JPG images recommended (best FFmpeg compatibility)

🔐 ElevenLabs API is paid

🖥️ FFmpeg must be installed and available in system PATH

🔄 Do not delete done.txt during runtime

🚀 Future Enhancements
🎵 Background music support

⏱️ Custom image timing controls

🐳 Docker containerization

☁️ Cloud storage (AWS / GCP)

📊 Processing status dashboard

🎯 Use Cases
Social media reel automation

AI demo projects

Content creation pipelines

Media processing automation

Portfolio showcase for AI & backend skills

