import os
import subprocess

def convert_video(input_path):
    base, _ = os.path.splitext(input_path)
    output_path = base + '_converted.mp4'
    command = ['ffmpeg', '-i', input_path, '-vcodec', 'h264', '-acodec', 'aac', output_path]
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return output_path
