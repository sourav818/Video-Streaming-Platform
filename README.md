# Video-Streaming-Platform
Build a platform to upload, stream, and manage video content.

📌 Features
🎬 Upload and manage video files

🔁 Auto-converts uploaded videos to .mp4 using FFmpeg

📺 Watch videos in browser with a clean player UI

🧾 Stores video metadata in a SQLite database

🧰 Modular structure (ready for S3, login, etc.)

🔧 Technologies Used
Python

Flask – web backend

SQLite – lightweight database

FFmpeg – video conversion

HTML/CSS – frontend templates

📁 Project Structure
video_streaming_app/
├── app.py
├── config.py
├── database.db
├── requirements.txt
├── utils/
│   └── ffmpeg_handler.py
├── templates/
│   ├── index.html
│   ├── upload.html
│   └── player.html
├── static/
│   └── style.css
├── videos/
└── README.md

Install Dependencies
pip install -r requirements.txt

Install FFmpeg
Make sure ffmpeg is installed and added to system PATH.
Download FFmpeg

5. Run the App
python app.py
Open your browser and visit:
👉 http://127.0.0.1:5000

🚀 Future Improvements
AWS S3 video storage

User authentication

Bootstrap styling

Admin dashboard

Video categories & search

👤 Author
Sourav Paul
Email:- souravpaul043@gmail.com
