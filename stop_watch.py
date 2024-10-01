#Author: Amadeus Kaczmarek
#Date: September 30 2024

import tkinter as tk
import time
#gui libarary and time

runtimer=False
i = 0.00

def update_timer():
    global runtimer
    global i
    global time
    if runtimer:
        i += 0.01
        time_label.config(text=f"{i:.2f}")
        root.after(10, update_timer)
    return time

def start():
    global runtimer
    if not runtimer:
        runtimer = True
        update_timer()

def stop():
    global runtimer
    runtimer = False
    return runtimer

def reset():
    global i
    i = 0.00 
    time_label.config(text=f"{i:.2f}")
    return i

root = tk.Tk()
root.title("Stop Watch")
time_label = tk.Label(root, text="0.00", font=("Arial", 30))
start_button = tk.Button(root, text="Start",command=start)
stop_button = tk.Button(root, text="Stop", command=stop)
reset_button = tk.Button(root, text="Reset", command=reset)
#in gui

start_button.grid(row=0, column=0)
stop_button.grid(row=0, column=1)
reset_button.grid(row=0, column=2)
time_label.grid(row=1, column=0, columnspan=3, pady=10)
#formating of gui
root.mainloop()
