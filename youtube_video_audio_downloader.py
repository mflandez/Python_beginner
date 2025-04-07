from pytube import YouTube
from sys import argv
import pytube.request
import re

print("Script started")

try:
    # Configure pytube
    pytube.request.default_range_size = 1024
    
    # Get and validate URL
    if len(argv) < 2:
        raise ValueError("Please provide a YouTube URL")
    
    url = argv[1]
    print("URL received:", url)
    
    # Convert any URL format to standard
    video_id = re.search(r'(?:v=|shorts/|youtu.be/)([\w-]+)', url).group(1)
    proper_url = f"https://youtube.com/watch?v={video_id}"
    
    # Create YouTube object with OAuth
    print("Creating YouTube object...")
    yt = YouTube(
        proper_url,
        use_oauth=True,
        allow_oauth_cache=True
    )
    
    # Get metadata
    print("\nVideo Info:")
    print(f"Title: {yt.title}")
    print(f"Views: {yt.views:,}")
    print(f"Length: {yt.length//60}:{yt.length%60:02d}")
    print(f"Author: {yt.author}")
    
except Exception as e:
    print(f"\nERROR: {str(e)}")
    print("Possible solutions:")
    print("1. Try a different video URL")
    print("2. Update pytube: pip install --upgrade pytube")
    print("3. Check your internet connection")