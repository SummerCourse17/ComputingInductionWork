#Celebrity Dogs Source Code (Part 1): Game Setup
#Copyright (C) Ben C 2021.

#Imports
from tkinter import *
import tkinter as tk
import random

#If Help Button Clicked
def helpM():
    #Function to close window and return to main window
    def returnM():
        rootB.destroy()
        main()

    #Prepare window
    rootB = tk.Tk()
    rootB.title("Celebrity Dogs")

    #Add Window Icon
    icon = PhotoImage(file="induction.png")
    rootB.iconphoto(False, icon)

    #Page Title
    a = Label(rootB, text="Celebrity Dogs Help", font=("Segoe Print", 20, "bold"), pady=20)
    a.pack()

    #Help Text to Show
    helpT = '''Welcome to Celebrity Dogs!

INTRODUCTION
------------
Celebrity Dogs is a round-based comparison game. 

HOW TO PLAY
-----------
The game will start with the user taking their turn. They will be presented a card with 4 categories on it. These are:
- Exercise (out of 5)
- Intelligence (out of 100)
- Friendliness (out of 10)
- Drool (out of 10)

The user should pick the category with the best score that they think will beat the computers card.
Note that whilst a high exercise, intelligence and friendliness is better, you want the drool value to be as low as possible.

WINNING
-------
The winner of the first round takes their opponent's card.
A next round is then played, with the winner of the previous round choosing the category.
To win the game, a player needs to have possession of ALL cards, leaving the opponent without any.

CREDITS
-------
Copyright (C) Ben C 2021.'''

    #Add Help Text
    a = Text(rootB, height=30, width=150)
    a.pack()
    a.insert(tk.END, helpT)

    #Return to Main Menu Button
    back = Button(rootB, text="Back", command=returnM)
    back.pack()

    a = Label(rootB, text="\nCoded by Ben C. Copyright (C) 2021. All rights reserved", pady=20, font=("Myriad Pro", 9, "italic"))
    a.pack()

#Game Setup Function
def start():
    #Function to close window and return to main menu
    def returnM():
        rootA.destroy()
        main()

    #Check number of cards
    def checkNum():
        #Get user input
        x1 = entry.get()
        if (int(x1) < 4) or (int(x1) > 30):
            result = Label(rootA, text="Too little or too many cards", fg="red")
            result.pack()
        elif ((int(x1) % 2) != 0):
            result = Label(rootA, text="Must be an even number of cards!", fg="red")
            result.pack()
        else:
            #Add number of cards to game presets document
            file = open("game_presets.txt", "w")
            file.write(x1)
            file.close()

            #Close Window
            rootA.destroy()

            #Run Game
            import card_game_play

    #Prepare Window
    rootA = tk.Tk()
    rootA.title("Celebrity Dogs")

    #Add Window Icon
    icon = PhotoImage(file="induction.png")
    rootA.iconphoto(False, icon)

    #Window Title
    a = Label(rootA, text="Celebrity Dogs", font=("Segoe Print", 20, "bold"), pady=20)
    a.pack()

    #User Input Field Label
    a = Label(rootA, text="Enter number of cards:")
    a.pack()

    #User Input Field
    entry = Entry(rootA)
    entry.pack()

    #Submit Button
    go = Button(rootA, text="Go", compound=LEFT, command=checkNum)
    go.pack()

    #Back to Main Menu Button
    back = Button(rootA, text="Back", command=returnM)
    back.pack()

    #Footer Note
    a = Label(rootA, text="\nCoded by Ben C. Copyright (C) 2021. All rights reserved", pady=20, font=("Myriad Pro", 9, "italic"))
    a.pack()

#Function for Main Menu
def main():
    #Close Window Function
    def quit():
        root.destroy()

    #Open Game Setup Window
    def startM():
        root.destroy()
        start()

    #Open Help Window
    def help():
        root.destroy()
        helpM()
        
    #Prepare Main Window
    root = Tk()
    root.title("Celebrity Dogs")

    #Add Window Icon
    icon = PhotoImage(file="induction.png")
    root.iconphoto(False, icon)

    #Window Title
    a = Label(root, text="Celebrity Dogs", font=("Segoe Print", 20, "bold"))
    a.pack()

    #Menu Options
    a = Label(root, text="Please select an option:")
    a.pack()

    btn = Button(root, text="Play Game", compound=LEFT, command=startM)
    btn.pack()

    btn = Button(root, text="How To Play", compound=LEFT, command=help)
    btn.pack()

    btn = Button(root, text="Quit", compound=LEFT, command=quit)
    btn.pack()

    #Footer Label
    a = Label(root, text="\nCoded by Ben C. Copyright (C) 2021. All rights reserved", pady=20, font=("Myriad Pro", 9, "italic"))
    a.pack()

#Open Main Menu
main()
