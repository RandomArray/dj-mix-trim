#!/usr/bin/env python3

import argparse
import sys
from trim_mix import trim_mp3
from update_cue import update_cue_file
from utils import check_dependencies, get_start_time, print_colored

def main():
    parser = argparse.ArgumentParser(
        description="Trim the first N tracks from a DJ mix and update the CUE file accordingly."
    )
    parser.add_argument("-i", "--input-mp3", required=True, help="Input MP3 file")
    parser.add_argument("-c", "--input-cue", required=True, help="Input CUE file")
    parser.add_argument("-n", "--num-tracks", required=True, type=int, help="Number of tracks to remove from the beginning")
    parser.add_argument("-f", "--fade-in", type=int, default=0, help="Number of seconds for fade-in effect at the beginning of the trimmed MP3")
    
    args = parser.parse_args()

    input_mp3 = args.input_mp3
    input_cue = args.input_cue
    num_tracks_to_remove = args.num_tracks
    fade_in = args.fade_in

    # Check for required dependencies
    check_dependencies()

    # Get the start time of the track to keep
    start_time = get_start_time(input_cue, num_tracks_to_remove)

    if not start_time:
        print_colored("Could not find the start time of the specified track in the CUE file.", "red")
        sys.exit(1)

    # Output filenames
    trimmed_mp3 = f"trimmed_{input_mp3}"
    updated_cue = f"trimmed_{input_cue}"

    # Trim the MP3 file
    print_colored(f"Trimming MP3 file from {start_time}...", "green")
    trim_mp3(input_mp3, trimmed_mp3, start_time, fade_in)

    # Update the CUE file
    print_colored("Updating CUE file...", "green")
    update_cue_file(input_cue, updated_cue, num_tracks_to_remove, trimmed_mp3)

    print_colored("Process completed successfully.", "green")
    print_colored(f"Trimmed MP3: {trimmed_mp3}", "yellow")
    print_colored(f"Updated CUE: {updated_cue}", "yellow")

if __name__ == "__main__":
    main()

