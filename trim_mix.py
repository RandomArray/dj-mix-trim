import subprocess

def trim_mp3(input_mp3, output_mp3, start_time, fade_in):
    if fade_in > 0:
        cmd = [
            "ffmpeg",
            "-i", input_mp3,
            "-ss", start_time,
            "-af", f"afade=t=in:ss=0:d={fade_in}",
            "-c:a", "libmp3lame",
            "-q:a", "2",
            output_mp3
        ]
    else:
        cmd = [
            "ffmpeg",
            "-i", input_mp3,
            "-ss", start_time,
            "-c", "copy",
            output_mp3
        ]
    subprocess.run(cmd, check=True)

