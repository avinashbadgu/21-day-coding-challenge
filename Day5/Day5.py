'''
Day 5 
Create Countdown Clock & Timer using Python
'''

import time
import tkinter as tk
from tkinter import *
from datetime import datetime
from win10toast import ToastNotifier
import winsound

window = Tk()
window.geometry('700x700')
window.title('Day4(CountDown Timer)')
Label(window, text="CountDown Clock and Timer", font='Calibri 15').pack(pady=20)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
Label(window, text=current_time).pack()

check = tk.BooleanVar()
hour = tk.IntVar()
minus = tk.IntVar()
secon = tk.IntVar()

def countdown():
    h = hour.get()
    m = minus.get()
    s = secon.get()
    t = h * 3600 + m * 60 + s
    while t:
        mins, secs = divmod(t, 60)
        display = '{:02d}:{:02d}'.format(mins, secs)
        time.sleep(1)
        t -= 1
        Label(window, text=display).pack()
    
    if check.get():
        winsound.Beep(440, 1000)
        
    Label(window, text="Time-Up", font='bold 20').place(x=250, y=440)
    
    toast = ToastNotifier()
    toast.show_toast("Notification", "Timer is Off", duration=20, icon_path=None, threaded=True)

Label(window, text="Enter time in HH:MM:SS", font='bold').pack()
Entry(window, textvariable=hour, width=30).pack()
Entry(window, textvariable=minus, width=30).pack()
Entry(window, textvariable=secon, width=30).pack()

Checkbutton(text='Check for Music', onvalue=True, variable=check).pack()
Button(window, text="Set Countdown", command=countdown, bg='yellow').pack()

window.update()
window.mainloop()
