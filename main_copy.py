#Hour 3: Finished Extension.
#This is a copy of main that the graphics uses.
def generatePassword():
    import random
    import secrets
    num = random.randint(8, 12)
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    other = [33, 36, 37, 94, 38, 42, 40, 41, 45, 95, 61, 43]

    score = 0

    while score < 35:
        password = []

        for i in range(0, num):
            what = random.randint(1, 4)

            if what == 1:
                val = secrets.choice(letters)
            elif what == 2:
                val = secrets.choice(letters).lower()
            elif what == 3:
                val = chr(secrets.choice(other))
            elif what == 4:
                val = random.randint(0, 9)

            password.append(str(val))

        password = "".join(password)
        score = checkPassword(password)

    returnA = "Your password is: " + str(password)
    returnB = "It scored: " + str(score)

    return returnA, returnB
    
def checkPassword(password=""):
    if password == "":
        password = input("Enter Password: ")

    if (len(password) < 8) or (len(password) > 24):
        print("Password too short or too long.")
    else:
        allowed = [33, 36, 37, 94, 38, 42, 40, 41, 45, 95, 61, 43]
        score = len(password)
        count = [0, 0, 0, 0]
        
        digits = list(password)
        for i in range(len(digits)):
            val = ord(digits[i])
            accept = False
            
            if (val >= 65) and (val <= 90):
                #Uppercase Letter
                accept = True
                count[0] += 1
            elif (val >= 97) and (val <= 122):
                #Lowercase Letter
                accept = True
                count[1] += 1
            elif (val >= 48) and (val <= 57):
                #Digit
                accept = True
                count[2] += 1

            if accept == False:
                for r in range(len(allowed)):
                    if allowed[r] == val:
                        #Alloed Symbol
                        accept = True
                        count[3] += 1

            if accept == False:
                print("Password contains unexpected value.")
                break
        
        if (count[0] >= 1):
            score +=5
        if (count[1] >= 1):
            score += 5
        if (count[2] >= 1):
            score += 5
        if (count[3] >= 1):
            score += 5
        if (count[0] >= 1) and (count[1] >= 1) and (count[2] >=1) and (count[3] >= 1):
            score += 10
        if (count[2] == 0) and (count[3] == 0):
            score -= 5
        if (count[0] == 0) and (count[1] == 0) and (count[3] == 0):
            score -= 5
        if (count[0] == 0) and (count[1] == 0) and (count[2] == 0):
            score -= 5

        #Look for consecutive
        rows = [["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
                ["a", "s", "d", "f", "g", "h", "j", "k", "l"],
                ["z", "x", "c", "v", "b", "n", "m"]]
        deduct = 0
        conCount = 0
        start = ""

        for a in range(len(digits)):
            for b in range(len(rows)):
                for c in range(len(rows[b])):
                    if rows[b][c] == digits[a].lower():
                        start = rows[b][c]
                        conCount += 1

                        try:
                            if (digits[a+1].lower() == rows[b][c+1]) and (digits[a+2].lower() == rows[b][c+2]):
                                conCount += 2
                                deduct +=1
                            else:
                                conCount = 0
                        except IndexError:
                            conCount = 0

        score -= deduct * 5
        return score
