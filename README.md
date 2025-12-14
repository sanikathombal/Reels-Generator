# Reels-Generator

🎬 VidSnapAI
    VidSnapAI is a Flask-based web application that automatically creates short video reels from uploaded images and text, using AI-generated voiceovers and FFmpeg.
    It is designed to quickly turn image folders into engaging reels with narration.

🚀 Features -
    📸 Upload multiple images (JPG / PNG / JPEG)
    📝 Convert text into AI-generated voice (using ElevenLabs)
    🎥 Automatically generate video reels using FFmpeg
    🖼️ Gallery view to see generated reels
    🔁 Background process that continuously checks for new uploads
    ⚡ Simple folder-based workflow

🛠️ Tech StackPython -
    Flask – Web framework
    ElevenLabs API – Text-to-speech (AI voice)
    FFmpeg – Image + audio to video conversion
    HTML / CSS – Frontend templates

⚙️ Installation & Setup
1️⃣ Install Dependencies
    pip install -U ElevenLabs
    pip install flask

2️⃣ Configure API Key
    Add your ElevenLabs API key in config.py :
    ELEVENLABS_API_KEY = "your_api_key_here"

3️⃣ Run the Flask App
    python main.py

4️⃣ Start Background Generator (New Terminal)
    python generate_process.py

🧑‍💻 How It Works - 
     1. Upload only image files (.jpg, .jpeg, .png)
     2. A unique folder is created inside user_uploads/
     3. Add a desc.txt file containing narration text
     4. The background script:
        - Converts text → AI voice (audio.mp3)
        - Combines images + audio using FFmpeg
        - Saves the final reel in static/reels/
     5. Processed folders are tracked in done.txt

⚠️ Important Notes - 
    ❗ Only JPG images are recommended
    (Other formats may cause FFmpeg errors)
    🔐 ElevenLabs API is paid
    🖥️ FFmpeg must be installed and accessible via command line
    🔄 Do not delete done.txt while the app is running

📌 Future Improvements-
    Background music support
    Custom video duration per image
    Better error handling
    Docker support
    Cloud storage integration
    FFmpeg – Image + audio to video conversion

HTML / CSS – Frontend templates

