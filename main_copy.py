#Seperate copy of main for Graphics solution to use.
#Hour 2: Started Extension
from tkinter import *
import tkinter as tk
#from main import *

def runA():
    def runD():
        x1 = entry.get()
        #returned = checkPassword(x1)
        returned = "Hi"
        result = Label(rootA, text=returned)
        result.pack()
    
    rootA = tk.Tk()
    rootA.title("Check Password")

    canvasA = Canvas(rootA, width=400, height=400)
    canvasA.pack()

    #iconA = PhotoImage(file="bc-brands-small.png")
    #rootA.iconphoto(False, iconA)

    entry = Entry(rootA)
    entry.pack()

    go = Button(rootA, text="Check Password", compound=LEFT, command=runD)
    go.pack()

    back = Button(rootA, text="Back", command=rootA.destroy)
    back.pack()
def runB():
    print("Hi")
def runC():
    root.destroy()

root = Tk()
root.title("Password Security")

icon = PhotoImage(file="bc-brands-small.png")
root.iconphoto(False, icon)

canvas = Canvas(width=500, height=200, bg="lightblue")
canvas.pack(expand=YES, fill=BOTH)

banner = PhotoImage(file="banner.png")
canvas.create_image(0, 0, image=banner, anchor=NW)

a = Label(root, text="Please select an option:")
a.pack()

btn = Button(root, text="Check Password", compound=LEFT, command=runA)
btn.pack()

btn = Button(root, text="Generate Password", compound=LEFT, command=runB)
btn.pack()

btn = Button(root, text="Quit", compound=LEFT, command=runC)
btn.pack()

a = Label(text="\nCoded by Ben C. Copyright (C) 2021. All rights reserved", pady=20, font=("Myriad Pro", 9, "italic"))
a.pack()
