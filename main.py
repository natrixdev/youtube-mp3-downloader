import os
import pytube
from moviepy.editor import *

# Ask for the video URL input
video_url = input("Enter the YouTube video URL: ")

# Check if the URL is valid and retrieve the video object
try:
    video = pytube.YouTube(video_url)
except:
    print("Video does not exist or is not available.")
    exit()

# Get the video title and create the output filename
video_title = video.title
filename = video_title + ".mp3"

# Download the video as an MP4 file
video_stream = video.streams.get_highest_resolution()
video_stream.download()

# Convert the MP4 file to an MP3 file using MoviePy
video_clip = VideoFileClip(video_stream.default_filename)
audio_clip = video_clip.audio
audio_clip.write_audiofile(filename)

# Remove the original MP4 file
os.remove(video_stream.default_filename)

# Move the output file to the desktop
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
output_path = os.path.join(desktop_path, filename)
os.replace(filename, output_path)

# Print the output file path to the user
print("File saved at " + output_path)
