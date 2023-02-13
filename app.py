import sys
import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *


window = tk.Tk()

window.title("TipTops Price Aggregator")
window.geometry("400x200")

#Functions

def search():
    if clicked.get() == "Lake County" :
        exec(open("LakeCountyPriceTracker.py").read())
    if clicked.get() == "Lake Tax":
        exec(open("LakeCountyPriceTracker.py").read())
    if clicked.get() == "Lake Clerk":
        exec(open("LakeClerkPriceTracker.py").read())


#Dropdown

options = [
    "Lake Clerk",
    "Lake County",
    "Lake Tax"
]

clicked = StringVar()

clicked.set("Lake Clerk")

drop = OptionMenu(window, clicked, *options)
drop.grid(column= 1, row=1, columnspan=2, padx=10, pady=25)

btn = Button(window, text = "Get Prices", command = search)
btn.grid(column= 3, row=1, columnspan=1, padx=10, pady=25)

label = Label(window, text= " ")

window.mainloop()