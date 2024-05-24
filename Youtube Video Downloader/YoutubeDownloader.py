import os
import time
from pytube import YouTube

#method to download video
def download_youtube_video(link, output_path):
    try: #try the link
        yt = YouTube(link)
        stream = yt.streams.get_highest_resolution() #'watches' the entire video in high res
        print(f"Downloading: {yt.title}") #user display for progress
        startTime = time.time()
        stream.download(output_path) #puts the video in the said path
        endTime = time.time()
        downloadTime = endTime - startTime #finds time difference
        minutes, seconds = divmod(downloadTime, 60) #formats time into minutes and seconds
        print("Download completed successfully.") #user progress indicator
        print(f"Download time: {int(minutes)} minutes {int(seconds)} seconds") #prints time taken!
    except Exception as e: #if the link's bad
        print(f"An error occurred: {str(e)}")

videoLink = input("Enter the YouTube video link: ")


outputDir = "Youtube Vids"


if not os.path.exists(outputDir): #if the directory ain't there, it's gon make one
    os.makedirs(outputDir)

download_youtube_video(videoLink, outputDir) #runs the entire thing