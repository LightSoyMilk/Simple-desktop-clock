from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")

foreground_color = "#2ed9ff"

def time():
    clock_string = strftime("%H:%M:%S %p")
    label.config(text = clock_string)
    label.after(1000, time)

label = Label(root, font=("led_real", 80), background = "pink", foreground = foreground_color)
label.pack(anchor="center")

time()

mainloop()