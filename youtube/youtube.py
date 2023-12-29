from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url,save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        highest_quality = streams.get_highest_resolution()
        highest_quality.download(output_path=save_path)
        print('video downloaded successfully!')
    
    except Exception as e:
        print(e)

def open_file_dialog():
    folder = filedialog.askdirectory()

    if folder:
        print(f'selcted folder: {folder}')

    return folder

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()

    video_url = input('Kindly enter the url for the video: ')
    save_path = open_file_dialog()

    if save_path:      
        print('download started...')
        download_video(video_url,save_path)
    
    else:
        print('Invalid DIrectory!')

    