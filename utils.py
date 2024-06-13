import shutil
import sys
import re

def check_dependencies():
    required_cmds = ["ffmpeg", "cuebreakpoints", "shnsplit"]
    for cmd in required_cmds:
        if not shutil.which(cmd):
            print_colored(f"{cmd} could not be found, please install it.", "red")
            sys.exit(1)

def get_start_time(cue_file, num_tracks_to_remove):
    track_count = 0
    start_time = None
    with open(cue_file, "r") as file:
        for line in file:
            if "TRACK" in line:
                track_count += 1
            if track_count == num_tracks_to_remove + 1 and "INDEX 01" in line:
                start_time = re.search(r"(\d+:\d+:\d+)", line).group(1)
                break
    return start_time

def print_colored(message, color):
    colors = {
        "red": "\033[0;31m",
        "green": "\033[0;32m",
        "yellow": "\033[1;33m",
        "blue": "\033[0;34m",
        "nc": "\033[0m"  # No Color
    }
    print(f"{colors[color]}{message}{colors['nc']}")

