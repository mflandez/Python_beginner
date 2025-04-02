import yt_dlp
from sys import argv

def youtube_downloader(url):
    ydl_opts = {
        'format': 'best',  # Best quality available
        'quiet': False,    # Show progress
        'no_warnings': False,
        'extract_flat': False,
        'noplaylist': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Get video info
            info = ydl.extract_info(url, download=False)
            
            print("\n📹 Video Info:")
            print(f"Title: {info['title']}")
            print(f"Channel: {info['uploader']}")
            print(f"Views: {info['view_count']:,}")
            print(f"Duration: {info['duration_string']}")
            
            # Download confirmation
            if input("\nDownload? (y/n): ").lower() == 'y':
                print("⬇️ Downloading...")
                ydl.download([url])
                print("✅ Download complete!")
    
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: python downloader.py <youtube_url>")
    else:
        youtube_downloader(argv[1])