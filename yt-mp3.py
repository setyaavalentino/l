import yt_dlp
import os
import sys
import argparse

def download_youtube(url, mode='mp3', output_dir='downloads'):
    os.makedirs(output_dir, exist_ok=True)
    
    if mode == 'mp3':
        target_dir = os.path.join(output_dir, 'mp3')
        os.makedirs(target_dir, exist_ok=True)
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(target_dir, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'quiet': False,
        }
    else: # mp4
        target_dir = os.path.join(output_dir, 'videos')
        os.makedirs(target_dir, exist_ok=True)
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': os.path.join(target_dir, '%(title)s.%(ext)s'),
            'quiet': False,
        }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"[*] Downloading: {url}")
            ydl.download([url])
        return True
    except Exception as e:
        print(f"[!] Error downloading {url}: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YouTube Downloader CLI (MP3/MP4)")
    parser.add_argument("target", nargs="?", help="YouTube URL or path to a .txt file containing URLs")
    parser.add_argument("--mode", choices=['mp3', 'mp4'], default='mp3', help="Download mode: mp3 (audio only) or mp4 (video)")
    
    args = parser.parse_args()
    
    target = args.target
    if not target:
        target = input("Enter YouTube URL or path to .txt file: ").strip()
    
    if not target:
        print("[!] No target provided.")
        sys.exit(1)
        
    urls = []
    if os.path.isfile(target) and target.endswith('.txt'):
        print(f"[*] Reading URLs from file: {target}")
        with open(target, 'r') as f:
            urls = [line.strip() for line in f if line.strip()]
    else:
        urls = [target]
            
    if not urls:
        print("[!] No URLs found.")
        sys.exit(1)
        
    print(f"[*] Mode: {args.mode.upper()}")
    for url in urls:
        success = download_youtube(url, args.mode)
        if success:
            print(f"[+] Successfully processed: {url}")
        else:
            print(f"[-] Failed to process: {url}")
