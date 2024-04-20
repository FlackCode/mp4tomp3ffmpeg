import subprocess
import os

input_dir = './VideoInput'
output_dir = './AudioOutput'
os.makedirs(input_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)

def convert_video_to_audio(input_file, output_file):
    ffmpeg_cmd = [
        'C:\\PATH_Programs\\ffmpeg.exe',
        '-i', input_file,
        '-vn',
        '-acodec', 'libmp3lame',
        '-ab', '192k',
        '-ar', '44100',
        '-y',
        output_file
    ]

    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print(f'Successfully converted {input_file} to {output_file}')
    except subprocess.CalledProcessError as e:
        print(f'Conversion of {input_file} failed!')

for i, filename in enumerate(os.listdir(input_dir)):
    if filename.endswith('.mp4'):
        input_file = os.path.join(input_dir, filename)
        output_file = os.path.join(output_dir, f'audio_{i}.mp3')
        convert_video_to_audio(input_file, output_file)
