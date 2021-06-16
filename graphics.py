#Graphics File
#Hour 3: Finished Extension
from tkinter import *
import tkinter as tk
from main_copy import checkPassword
from main_copy import generatePassword

runPC = 1

def runA():
    
    def runD():
        global runPC
        
        x1 = entry.get()
        returned = "Input #" + str(runPC) + ": "
        if x1 == "":
            returned = returned + "ERR - MUST ENTER PASSWORD"
        else:
            returnedA = "Strength - " + str(checkPassword(x1))
            if returnedA == "None":
                returned = returned + "ERR - UNEXPECTED INPUT. Refer to terminal for more details."
            else:
                returned = returned + returnedA

        runPC += 1
        
        result = Label(rootA, text=returned)
        result.pack()
    
    rootA = tk.Tk()
    rootA.title("Check Password")

    canvas = Canvas(rootA, width=500, height=200, bg="lightblue")
    canvas.pack(expand=YES, fill=BOTH)

    #iconA = PhotoImage(file="bc-brands-small.png")
    #rootA.iconphoto(False, iconA)

    entry = Entry(rootA, width=50)
    entry.pack()

    go = Button(rootA, text="Check Password", compound=LEFT, command=runD)
    go.pack()

    back = Button(rootA, text="Back", command=rootA.destroy)
    back.pack()

    a = Label(rootA, text="\nCoded by Ben C. Copyright (C) 2021. All rights reserved", pady=20, font=("Myriad Pro", 9, "italic"))
    a.pack()
def runB():
    def runE():
        returnedA, returnedB = generatePassword()
        
        result = Label(rootB, text=returnedA)
        result.pack()

        result = Label(rootB, text=returnedB)
        result.pack()
        
    rootB = tk.Tk()
    rootB.title("Generate Password")

    canvas = Canvas(rootB, width=500, height=200, bg="lightblue")
    canvas.pack(expand=YES, fill=BOTH)

    #iconA = PhotoImage(file="bc-brands-small.png")
    #rootA.iconphoto(False, iconA)

    go = Button(rootB, text="Generate", compound=LEFT, command=runE)
    go.pack()

    back = Button(rootB, text="Back", command=rootB.destroy)
    back.pack()

    a = Label(rootB, text="\nCoded by Ben C. Copyright (C) 2021. All rights reserved", pady=20, font=("Myriad Pro", 9, "italic"))
    a.pack()
    
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
