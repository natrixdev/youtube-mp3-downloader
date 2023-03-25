# YouTube mp3 Downloader

A python script that will save the audio of a video with the URL of this one. 

the following Python script is using the `pytube` and `moviepy` libraries

This script first asks for the YouTube video URL input from the user. Then it tries to create a pytube.YouTube object from the URL, which will raise an exception if the URL is invalid or the video is not available. If this happens, the script prints an error message and exits.

If the video object is successfully created, the script gets the video title and creates the output filename by adding the ".mp3" extension. It then downloads the video as an MP4 file using the highest available resolution stream. Once the video is downloaded, it uses MoviePy to extract the audio from the video and save it as an MP3 file with the previously created filename.

The script then removes the original MP4 file and moves the output file to the user's desktop. Finally, it prints the output file path to the user.
