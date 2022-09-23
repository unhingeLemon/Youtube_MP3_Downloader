# importing packages
from tkinter import X
from pytube import YouTube
import os
destination = './downloaded'


def dlmp3(link):
    yt = YouTube(link)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print(yt.title + " has been successfully downloaded.")


f = open("./ytLinks.txt", "r")
for x in f:
  dlmp3(x)