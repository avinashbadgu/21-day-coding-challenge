from pytube import YouTube
from tkinter import *
import tkinter as tk

window = Tk()
window.geometry("1000x500")
window.title("Day 9(YOUTUBE VIDEO DOWNLOADER)")

text = StringVar()
res1 = IntVar()
res2 = IntVar()
res3 = IntVar()

Label(window, text="YOUTUBE VIDEO DOWNLOADER", bg='grey', font=('Calibri 15')).pack()
Label(window, text="Enter the link to download", font=('Calibri 12')).pack()
Entry(window, textvariable=text, width=50).pack()
Checkbutton(text='360p', onvalue=18, offvalue=0, variable=res1).pack()
Checkbutton(text='720p', onvalue=22, offvalue=0, variable=res2).pack()
Checkbutton(text='1080p', onvalue=37, offvalue=0, variable=res3).pack()

def downloader():
    global res
    t = text.get()
    video = YouTube(t)

    if res1.get() == 18:
        res = 18
    elif res2.get() == 22:
        res = 22
    elif res3.get() == 37:
        res = 37

    video_streams = video.streams.filter(file_extension='mp4').get_by_itag(res)
    video_streams.download(filename="Untitled", output_path="video_path")
    Label(window, text="Downloaded Successfully").pack()

Button(window, text="Download", bg='green', command=downloader).pack()

window.mainloop()
