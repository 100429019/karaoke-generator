from pytube import YouTube
import os

PATH = os.getcwd() + '/test/'
VIDEO_ID = input('Video id: ')

# Create a YouTube object for the video you want to download
yt = YouTube("https://www.youtube.com/watch?v="+ VIDEO_ID)

# Print the video title and duration
print("Title:", yt.title)
print("Duration:", yt.length, "seconds")

# Select the highest quality stream
stream = yt.streams.get_highest_resolution()

# Download the video to a local file
stream.download(output_path= PATH + yt.title, filename="video.mp4")
