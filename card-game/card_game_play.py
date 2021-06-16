#Celebrity Dogs Source Code (Part 2): Game GUI
#Copyright (C) Ben C 2021.

#Import Modules
from tkinter import *
import tkinter as tk
import random
import secrets

#Open file for no cards in play
file = open("game_presets.txt", "r")
noCards = int(file.read())
file.close()

#Open dogs.txt for names of cards
file = open("dogs.txt", "r")
contents = file.read()
file.close()

#Shuffle array of dog names
items = contents.split("\n")
random.shuffle(items)

#Prepare dog class to structure information
class Dog:
    def __init__(self, name, exer, frie, inte, droo):
        self.name = name
        self.exer = exer
        self.frie = frie
        self.inte = inte
        self.droo = droo

#Arrays used to store cards in-game
cardsT = []
cardsA = []
cardsB = []

#Generate random details for each card
for i in range(noCards):
    exerR = random.randint(1, 5)
    frieR = random.randint(1, 10)
    inteR = random.randint(1, 100)
    drooR = random.randint(1, 10)
    info = Dog(items[i], exerR, frieR, inteR, drooR)
    cardsT.append(info)

#Shuffle cards
random.shuffle(cardsT)

#Split cards between two players
for i in range(len(cardsT)):
    if (i % 2) == 0:
        cardsA.append(cardsT[i])
    else:
        cardsB.append(cardsT[i])

#Define Global Variables
turn = "u"
loop = True
winner = "n"
global played
played = "n"

#Keep Looping
while loop == True:
    #Break loop when a player has won
    if (len(cardsA) == noCards):
        winner = "u"
        loop = False
        break
    elif (len(cardsB) == noCards):
        winner = "c"
        loop = False
        break

    if turn == "u":    
        #Start User-Turn GUI
        card = cardsA[0]

        #Prepare Window
        board = Tk()
        board.title("Celebrity Dogs")

        #Add icon
        icon = PhotoImage(file="induction.png")
        board.iconphoto(False, icon)

        #Prepare Canvas
        canvas = Canvas(width=900, height=600, bg="lightblue")
        canvas.pack()

        #Add background and card image
        banner = PhotoImage(file="induction.png")
        canvas.create_image(0, 0, image=banner, anchor=NW)

        bannerA = PhotoImage(file="dog.png")
        canvas.create_image(510, 120, image=bannerA, anchor=NW)

        #Format strings for display
        cardName= card.name
        exercise =     "Exercise:         0" + str(card.exer)
        if int(card.frie) < 10:
            card.frie = "0" + str(card.frie)
        if int(card.inte) < 10:
            card.inte = "00" + str(card.inte)
        elif int(card.inte) < 100:
            card.inte = "0" + str(card.inte)
        if int(card.droo) < 10:
            card.droo = "0" + str(card.droo)
        friendliness = "Friendliness:   " + str(card.frie)
        intelligence = "Intelligence: " + str(card.inte)
        drool =        "Drool:             " + str(card.droo)
        photo = ""

        #Establish font size to use
        if len(cardName) > 26:
            nameFS = 15
        else:
            nameFS = 18

        #Insert Card Details
        canvas.create_text(630, 360, text=cardName, font=("Tempus Sans ITC", nameFS, "bold"))
        canvas.create_text(580, 420, text=exercise, font=("Tempus Sans ITC", 16, "bold"))
        canvas.create_text(580, 440, text=friendliness, font=("Tempus Sans ITC", 16, "bold"))
        canvas.create_text(580, 460, text=intelligence, font=("Tempus Sans ITC", 16, "bold"))
        canvas.create_text(580, 480, text=drool, font=("Tempus Sans ITC", 16, "bold"))

        #Show scores
        hCards = "Your Cards: " + str(len(cardsA))
        canvas.create_text(850, 20, text=hCards)

        cCards = "Computer Cards: " + str(len(cardsB))
        canvas.create_text(850, 30, text=cCards)

        #Show Option Text
        a = Label(board, text="Your Turn", font=("Segoe Print", 20, "bold"))
        a.pack()

        a = Label(board, text="Please select an option:")
        a.pack()

        #Functions for tasks on button click
        def playE():
            global played
            played = "E"
            board.destroy()

        def playF():
            global played
            played = "F"
            board.destroy()

        def playI():
            global played
            played = "I"
            board.destroy()

        def playD():
            global played
            played = "D"
            board.destroy()

        #Buttons to select category
        btn = Button(board, text="Exercise", compound=LEFT, command=playE)
        btn.pack()

        btn = Button(board, text="Friendliness", compound=LEFT, command=playF)
        btn.pack()

        btn = Button(board, text="Intelligence", compound=LEFT, command=playI)
        btn.pack()

        btn = Button(board, text="Drool", compound=LEFT, command=playD)
        btn.pack()

        #Footer Notice
        a = Label(board, text="\nCoded by Ben C. Copyright (C) 2021. All rights reserved", pady=20, font=("Myriad Pro", 9, "italic"))
        a.pack()

        #Repeat until user input
        mainloop()

    elif turn == "c":
        #Start Computer-Turn GUI

        #Choose a category to play randomly
        options = ["E", "F", "I", "D"]
        played = secrets.choice(options)
        
        card = cardsA[0]

        #Create Window
        board = Tk()
        board.title("Celebrity Dogs")

        #Add Window Icon
        icon = PhotoImage(file="induction.png")
        board.iconphoto(False, icon)

        #Prepare Canvas
        canvas = Canvas(width=900, height=600, bg="lightblue")
        canvas.pack()

        #Add Background and Card Image
        banner = PhotoImage(file="induction.png")
        canvas.create_image(0, 0, image=banner, anchor=NW)

        bannerA = PhotoImage(file="dog.png")
        canvas.create_image(510, 120, image=bannerA, anchor=NW)

        #Format Strings ready for display
        cardName= card.name
        exercise =     "Exercise:         0" + str(card.exer)
        if int(card.frie) < 10:
            card.frie = "0" + str(card.frie)
        if int(card.inte) < 10:
            card.inte = "00" + str(card.inte)
        elif int(card.inte) < 100:
            card.inte = "0" + str(card.inte)
        if int(card.droo) < 10:
            card.droo = "0" + str(card.droo)
        friendliness = "Friendliness:   " + str(card.frie)
        intelligence = "Intelligence: " + str(card.inte)
        drool =        "Drool:             " + str(card.droo)
        photo = ""

        #Establish font sizes
        if len(cardName) > 26:
            nameFS = 15
        else:
            nameFS = 18

        #Insert card details
        canvas.create_text(630, 360, text=cardName, font=("Tempus Sans ITC", nameFS, "bold"))
        canvas.create_text(580, 420, text=exercise, font=("Tempus Sans ITC", 16, "bold"))
        canvas.create_text(580, 440, text=friendliness, font=("Tempus Sans ITC", 16, "bold"))
        canvas.create_text(580, 460, text=intelligence, font=("Tempus Sans ITC", 16, "bold"))
        canvas.create_text(580, 480, text=drool, font=("Tempus Sans ITC", 16, "bold"))

        #Show current score
        hCards = "Your Cards: " + str(len(cardsA))
        canvas.create_text(850, 20, text=hCards)

        cCards = "Computer Cards: " + str(len(cardsB))
        canvas.create_text(850, 30, text=cCards)

        #Show options (for user)
        a = Label(board, text="Computer's Turn", font=("Segoe Print", 20, "bold"))
        a.pack()

        a = Label(board, text="Please select an option:")
        a.pack()

        #Define what to do on button click
        def playC():
            board.destroy()

        #Show Buttons
        btn = Button(board, text="Continue", compound=LEFT, command=playC)
        btn.pack()

        #Footer Notice
        a = Label(board, text="\nCoded by Ben C. Copyright (C) 2021. All rights reserved", pady=20, font=("Myriad Pro", 9, "italic"))
        a.pack()

        #Loop until user input
        mainloop()

    #Start Card Comparison

    #Get user and computer cards
    cardH = cardsA[0]
    cardC = cardsB[0]

    #Create Window
    board = Tk()
    board.title("Celebrity Dogs")

    #Add Window Icon
    icon = PhotoImage(file="induction.png")
    board.iconphoto(False, icon)

    #Prepare Canvas
    canvas = Canvas(width=900, height=600, bg="lightblue")
    canvas.pack()

    #Add background and card images
    banner = PhotoImage(file="induction_compare.png")
    canvas.create_image(0, 0, image=banner, anchor=NW)

    bannerA = PhotoImage(file="dog.png")
    canvas.create_image(510, 120, image=bannerA, anchor=NW)

    bannerB = PhotoImage(file="dog.png")
    canvas.create_image(190, 120, image=bannerB, anchor=NW)

    #Format Strings ready for display
    cardName= cardH.name
    exercise =     "Exercise:         0" + str(cardH.exer)
    #if cardH.frie < 10:
    #    cardH.frie = "0" + str(cardH.frie)
    #if cardH.inte < 10:
    #    cardH.inte = "00" + str(cardH.inte)
    #elif cardH.inte < 100:
    #    cardH.inte = "0" + str(cardH.inte)
    #if cardH.droo < 10:
    #    cardH.droo = "0" + str(cardH.droo)
    friendliness = "Friendliness:   " + str(cardH.frie)
    intelligence = "Intelligence: " + str(cardH.inte)
    drool =        "Drool:             " + str(cardH.droo)
    photo = ""

    cardNameC= cardC.name
    exerciseC =     "Exercise:         0" + str(cardC.exer)
    if int(cardC.frie) < 10:
        cardC.frie = "0" + str(cardC.frie)
    if int(cardC.inte) < 10:
        cardC.inte = "00" + str(cardC.inte)
    elif int(cardC.inte) < 100:
        cardC.inte = "0" + str(cardC.inte)
    if int(cardC.droo) < 10:
        cardC.droo = "0" + str(cardC.droo)
    friendlinessC = "Friendliness:   " + str(cardC.frie)
    intelligenceC = "Intelligence: " + str(cardC.inte)
    droolC =        "Drool:             " + str(cardC.droo)
    photoC = ""

    #Establish font size
    if len(cardName) > 26:
        nameFS = 15
    else:
        nameFS = 18

    #Show User Card Details
    canvas.create_text(630, 70, text="Your Card", font=("Segoe Print", 20, "bold"))
    canvas.create_text(630, 360, text=cardName, font=("Tempus Sans ITC", nameFS, "bold"))
    canvas.create_text(580, 420, text=exercise, font=("Tempus Sans ITC", 16, "bold"))
    canvas.create_text(580, 440, text=friendliness, font=("Tempus Sans ITC", 16, "bold"))
    canvas.create_text(580, 460, text=intelligence, font=("Tempus Sans ITC", 16, "bold"))
    canvas.create_text(580, 480, text=drool, font=("Tempus Sans ITC", 16, "bold"))

    #Establish font size (computer's card)
    if len(cardNameC) > 26:
        nameFSC = 15
    else:
        nameFSC = 18

    #Show Computer Card Details
    canvas.create_text(300, 70, text="Computer's Card", font=("Segoe Print", 20, "bold"))
    canvas.create_text(310, 360, text=cardNameC, font=("Tempus Sans ITC", nameFSC, "bold"))
    canvas.create_text(260, 420, text=exerciseC, font=("Tempus Sans ITC", 16, "bold"))
    canvas.create_text(260, 440, text=friendlinessC, font=("Tempus Sans ITC", 16, "bold"))
    canvas.create_text(260, 460, text=intelligenceC, font=("Tempus Sans ITC", 16, "bold"))
    canvas.create_text(260, 480, text=droolC, font=("Tempus Sans ITC", 16, "bold"))

    #Show Current Score
    hCards = "Your Cards: " + str(len(cardsA))
    canvas.create_text(850, 20, text=hCards)

    cCards = "Computer Cards: " + str(len(cardsB))
    canvas.create_text(850, 30, text=cCards)

    #Work out who won
    if played == "E":
        if int(cardH.exer) >= int(cardC.exer):
            a = Label(board, text="You Win", font=("Segoe Print", 20, "bold"))
            a.pack()

            a = Label(board, text="You had a higher exercise", font=("Tempus Sans ITC", 16, "bold"))
            a.pack()

            roundWin = "p"
        else:
            a = Label(board, text="Computer Wins", font=("Segoe Print", 20, "bold"))
            a.pack()

            a = Label(board, text="You had a lower exercise", font=("Tempus Sans ITC", 16, "bold"))
            a.pack()

            roundWin = "c"
    elif played == "F":
        if int(cardH.frie) >= int(cardC.frie):
            a = Label(board, text="You Win", font=("Segoe Print", 20, "bold"))
            a.pack()

            a = Label(board, text="You had a higher friendliness", font=("Tempus Sans ITC", 16, "bold"))
            a.pack()

            roundWin = "p"
        else:
            a = Label(board, text="Computer Wins", font=("Segoe Print", 20, "bold"))
            a.pack()

            a = Label(board, text="You had a lower friendliness", font=("Tempus Sans ITC", 16, "bold"))
            a.pack()

            roundWin = "c"
    elif played == "I":
        if int(cardH.inte) >= int(cardC.inte):
            a = Label(board, text="You Win", font=("Segoe Print", 20, "bold"))
            a.pack()

            a = Label(board, text="You had a higher intelligence", font=("Tempus Sans ITC", 16, "bold"))
            a.pack()

            roundWin = "p"
        else:
            a = Label(board, text="Computer Wins", font=("Segoe Print", 20, "bold"))
            a.pack()

            a = Label(board, text="You had a lower intelligence", font=("Tempus Sans ITC", 16, "bold"))
            a.pack()

            roundWin = "c"
    elif played == "D":
        if int(cardH.droo) <= int(cardC.droo):
            a = Label(board, text="You Win", font=("Segoe Print", 20, "bold"))
            a.pack()

            a = Label(board, text="You had a lower drool", font=("Tempus Sans ITC", 16, "bold"))
            a.pack()
            
            roundWin = "p"
        else:
            a = Label(board, text="Computer Wins", font=("Segoe Print", 20, "bold"))
            a.pack()

            a = Label(board, text="You had a higher drool", font=("Tempus Sans ITC", 16, "bold"))
            a.pack()

            roundWin = "c"

    #Add cards to the winner's deck
    if roundWin == "p":
        memoryA = cardsA[0]
        memoryB = cardsB[0]
        
        cardsA.pop(0)
        cardsB.pop(0)

        cardsA.append(memoryA)
        cardsA.append(memoryB)

        turn = "u"
    elif roundWin == "c":
        memoryA = cardsA[0]
        memoryB = cardsB[0]
        
        cardsA.pop(0)
        cardsB.pop(0)

        cardsB.append(memoryA)
        cardsB.append(memoryB)

        turn = "c"

    #Show user their options
    a = Label(board, text="Please select an option:")
    a.pack()

    #Define what to do on button click
    def playC():
        board.destroy()

    #Show Buttons
    btn = Button(board, text="Continue", compound=LEFT, command=playC)
    btn.pack()

    #Footer Note
    a = Label(board, text="\nCoded by Ben C. Copyright (C) 2021. All rights reserved", pady=20, font=("Myriad Pro", 9, "italic"))
    a.pack()

    #Loop until user input
    mainloop()

#Show Win/Loose Final Message
if winner == "c":
    #Prepare Window
    root = Tk()
    root.title("Celebrity Dogs")

    #Add Window Icon
    icon = PhotoImage(file="induction.png")
    root.iconphoto(False, icon)

    a = Label(root, text="You lost!", font=("Segoe Print", 20, "bold"))
    a.pack()

    a = Label(root, text="\nCoded by Ben C. Copyright (C) 2021. All rights reserved", pady=20, font=("Myriad Pro", 9, "italic"))
    a.pack()
elif winner == "u":
    #Prepare Window
    root = Tk()
    root.title("Celebrity Dogs")

    #Add Window Icon
    icon = PhotoImage(file="induction.png")
    root.iconphoto(False, icon)

    #Show Text
    a = Label(root, text="You won!", font=("Segoe Print", 20, "bold"))
    a.pack()

    #Footer Note
    a = Label(root, text="\nCoded by Ben C. Copyright (C) 2021. All rights reserved", pady=20, font=("Myriad Pro", 9, "italic"))
    a.pack()
else:
    #Prepare Window
    root = Tk()
    root.title("Celebrity Dogs")

    #Add Window Icon
    icon = PhotoImage(file="induction.png")
    root.iconphoto(False, icon)

    #Show Text
    a = Label(root, text="Game Closed", font=("Segoe Print", 20, "bold"))
    a.pack()

    #Footer Note
    a = Label(root, text="\nCoded by Ben C. Copyright (C) 2021. All rights reserved", pady=20, font=("Myriad Pro", 9, "italic"))
    a.pack()
