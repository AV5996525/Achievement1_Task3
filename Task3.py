print("Welcome to the user name checker \nRULES: \nMaximum of 20 characters \nMininum of 2 or more characters \nMust contain one upper case character and one number value from 0 - 9")
while True:
    def checkName(str):
        fL = False
        for i in str :
            if i.isupper() :
                fL = True
        return fL
    def checkNum(str) :
        fN = False
        for i in str :
            if i.isdigit() :
                fN = True
        return fN                    
    nameUSER = input("Please enter your username: ").strip()
    if len(nameUSER) <= 1 :
        print("not big enough")
    elif len(nameUSER) > 20 :
        print("too big ")
    elif len(nameUSER) > 1 and len(nameUSER) <= 20 :
        if checkName(nameUSER) and checkNum(nameUSER) :
            print("valid input")
