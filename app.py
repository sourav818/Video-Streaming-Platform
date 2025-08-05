import os
import sqlite3
from flask import Flask, request, redirect, url_for, render_template, send_from_directory, abort
from werkzeug.utils import secure_filename
from utils.ffmpeg_handler import convert_video
from config import UPLOAD_FOLDER, DB_PATH

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize database
def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS videos (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT NOT NULL,
                            filename TEXT NOT NULL,
                            uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                        )''')
init_db()

# Home Page
@app.route('/')
def index():
    with sqlite3.connect(DB_PATH) as conn:
        videos = conn.execute("SELECT * FROM videos ORDER BY uploaded_at DESC").fetchall()
    return render_template('index.html', videos=videos)

# Upload Route
@app.route('/upload', methods=['GET', 'POST'])
def upload_video():
    if request.method == 'POST':
        file = request.files.get('video')
        title = request.form.get('title', 'Untitled Video')
        
        if file and file.filename:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Convert using FFmpeg
            output_path = convert_video(filepath)
            output_name = os.path.basename(output_path)

            # Save metadata
            with sqlite3.connect(DB_PATH) as conn:
                conn.execute("INSERT INTO videos (title, filename) VALUES (?, ?)", (title, output_name))
            return redirect(url_for('index'))
        else:
            return "No file uploaded!", 400

    return render_template('upload.html')

# Stream video file directly
@app.route('/videos/<filename>')
def stream_video(filename):
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    except FileNotFoundError:
        abort(404)

# Watch video page
@app.route('/watch/<int:video_id>')
def watch(video_id):
    with sqlite3.connect(DB_PATH) as conn:
        video = conn.execute("SELECT * FROM videos WHERE id = ?", (video_id,)).fetchone()
    if video:
        return render_template('player.html', video=video)
    else:
        return "Video not found", 404

# Run app
if __name__ == '__main__':
    app.run(debug=True)
