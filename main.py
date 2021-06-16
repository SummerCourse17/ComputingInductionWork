#Hour 1: completed up to step 4
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
            

while True:
    menu = """Please select an option:
    [1] Check Password
    [2] Generate Password
    [3] Quit"""

    print(menu)

    run = input(" > ")

    if run == "1":
        val = checkPassword()
        if (val <= 0):
            print("Very Weak")
        elif (val <= 5):
            print("Weak")
        elif (val <= 20):
            print("Medium")
        elif (val <= 40):
            print("Strong")
        else:
            print("Very Strong")
