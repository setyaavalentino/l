import os
import subprocess
import argparse

def merge_video_audio(video_path, audio_path, output_path):
    """
    Merges video and audio with seamless looping of video to match audio length.
    """
    if not os.path.exists(video_path):
        print(f"Error: Video file not found: {video_path}")
        return
    if not os.path.exists(audio_path):
        print(f"Error: Audio file not found: {audio_path}")
        return
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # FFmpeg command:
    # -stream_loop -1: loops video infinitely
    # -i video: input video
    # -i audio: input audio
    # -c:v copy: copy video codec (fast)
    # -c:a aac: encode audio to aac
    # -shortest: stop when the shortest stream (audio) ends
    cmd = [
        "ffmpeg", "-y",
        "-stream_loop", "-1",
        "-i", video_path,
        "-i", audio_path,
        "-map", "0:v:0",
        "-map", "1:a:0",
        "-c:v", "libx264", "-preset", "veryfast",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest",
        output_path
    ]
    
    print(f"Merging {video_path} and {audio_path} -> {output_path}")
    subprocess.run(cmd)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge Video and Audio with Looping")
    parser.add_argument("--video", help="Path to video file")
    parser.add_argument("--audio", help="Path to audio file")
    parser.add_argument("--output", default="downloads/output/final_video.mp4", help="Output path")
    
    args = parser.parse_args()
    
    if args.video and args.audio:
        merge_video_audio(args.video, args.audio, args.output)
    else:
        # Interactive mode if no args
        video = input("Enter video file path: ")
        audio = input("Enter audio file path: ")
        output = input("Enter output file path (default: downloads/output/output.mp4): ") or "downloads/output/output.mp4"
        merge_video_audio(video, audio, output)
