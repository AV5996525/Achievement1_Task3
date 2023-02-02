print("Welcome to the user name checker \nRULES: \nMaximum of 20 characters \nMininum of 2 or more characters \nMust contain one upper case character and one number value from 0 - 9")
while True:
    def checkName(str):
        fL = False
        for i in str :
            if i.isupper() :
                fL = True
        return fL
    def checkNameLc(str):
        fLc = False
        for i in str :
            if i.islower() :
                fLc = True
        return fLc            
    def checkNum(str) :
        fN = False
        for i in str :
            if i.isdigit() :
                fN = True
        return fN                    
    nameUser = input("Please enter your username: ").strip()
    if len(nameUser) <= 1 :
        print("Username requires more than one character.")
    elif len(nameUser) > 20 :
        print("Username exceeds 20 characters.")
    elif nameUser.isdigit() :
        print("Username requires atleast one uppercase letter.")
    elif nameUser.isalpha() :
        print("Username requires atleast one number.")  
    elif checkNameLc(nameUser) and checkNum(nameUser) :
        print("Username has numbers, but is missing one uppercase letter.")          
    elif len(nameUser) > 1 and len(nameUser) <= 20 :
        if checkName(nameUser) == True and checkNum(nameUser) == True :
            print("Username meets requirements, congratulations!")
            