# DJ Mix Trimmer

A tool to trim the first N tracks from a DJ mix and update the corresponding CUE file.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/RandomArray/dj-mix-trim.git
    cd dj-mix-trim
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Ensure you have the required command-line tools installed:
    ```sh
    sudo apt update
    sudo apt install ffmpeg cuetools shntool
    ```

## Usage

```sh
./dj_mix_trim.py -i <input_mp3> -c <input_cue> -n <num_tracks_to_remove> [-f <fade_in_seconds>]
```

### Example

```sh
./dj_mix_trim.py -i mix.mp3 -c mix.cue -n 12 -f 5
```

This command will trim the first 12 tracks from `mix.mp3`, apply a 5-second fade-in, and update `mix.cue` accordingly.

## License

MIT License

