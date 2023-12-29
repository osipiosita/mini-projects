from pytube import YouTube
import tkinter as tk
from tkinter import dialog


def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        highest_resolution = streams.get_highest_resolution()
        highest_resolution.download(output_path=save_path)
        print('Video downloaded Successfully!')

    except Exception as e:
        print(e)

url = 'https://youtube.com/shorts/oXO3q2Kvc4U?si=JyUttUVR5TIVEZYj'
save_path = 'C:/Users/ackam/Desktop'
download_video(url, save_path)