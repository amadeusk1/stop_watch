#Author: Amadeus Kaczmarek
#Date: September 30 2024

import tkinter as tk
import time

i = 0.00
runtimer = True

while runtimer:
    i += 0.01
    print(f"{i:.2f}")
    time.sleep(0.01)
    if i >= 3.00:
        runtimer = False




"""
root = tk.Tk()
root.title("Stop Watch")
w = tk.Label(root, text='GeeksForGeeks.org!')
start = tk.Button(root, text="Start")
stop = tk.Button(root, text="Stop")


start.grid(row=0, column=0)
stop.grid(row=0, column=1)
root.mainloop()
"""