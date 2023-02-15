import sys
import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

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

def search_all():
    exec(open("searchAll.py").read())

#Dropdown

options = [
    "Lake Clerk",
    "Lake County",
    "Lake Tax"
]

clicked = StringVar()

clicked.set("Lake Clerk")

drop = OptionMenu(window, clicked, *options)
drop.grid(column= 1, row=1, columnspan=2, padx=10, pady=10)

btn1 = Button(window, text = "Get Prices", command = search)
btn1.grid(column= 3, row=1, columnspan=1, padx=10, pady=10)

btn2 = Button(window, text= "Get All Prices", command = search_all)
btn2.grid(column= 2, row=2, columnspan=2, padx=10, pady=10)

label = Label(window, text= " ")

window.mainloop()