def update_cue_file(input_cue, output_cue, num_tracks_to_remove, newfile):
    with open(input_cue, "r") as infile, open(output_cue, "w") as outfile:
        track_count = 0
        for line in infile:
            if "FILE" in line:
                outfile.write(f'FILE "{newfile}" MP3\n')
            elif "TRACK" in line:
                track_count += 1
                if track_count > num_tracks_to_remove:
                    if track_count == num_tracks_to_remove + 1:
                        track_count = 1
                    outfile.write(line)
            else:
                if track_count > num_tracks_to_remove:
                    outfile.write(line)

