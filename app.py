import sys
import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *


window = tk.Tk()

window.title("TipTops Price Aggregator")
window.geometry("400x200")

#buttons

def LakeClerk():
    exec(open("LakeClerkPriceTracker.py").read())

def LakeCounty():
    exec(open("LakeCountyPriceTracker.py").read())

def LakeTax():
    exec(open("LakeCountyPriceTracker.py").read())

btn1 = Button(window, text="Lake Clerk", bg="black", fg="white", command = LakeClerk)
btn1.grid(column=1, row=5, padx=25, pady=25)

btn2 = Button(window, text="Lake County", bg="black", fg="white", command = LakeCounty)
btn2.grid(column=2, row=5, padx=25, pady=25)

btn3 = Button(window, text="Lake Tax", bg="black", fg="white", command = LakeTax)
btn3.grid(column=3, row=5, padx=25, pady=25)

window.mainloop()