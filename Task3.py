#Name:          Task3.py
#Author:        AJ Varatharajan
#Date Created:  February 1, 2023
#Date Last Modified: February 2, 2023

#Purpose: 
#
#This program will check a username for:
#Must contain 2 to 20 characters with atleast 1 uppercase character and a number.
#Will continously run and display error message if username inputed does not meet requirements.
print("Welcome to the user name checker \nRULES: \nMaximum of 20 characters \nMininum of 2 or more characters \nMust contain one upper case character and one number value from 0 - 9")
while True:                             #intializing loop.
    def checkName(str):                 #creating a function that will loop through each character in a given string and will return true if one upper character is found.
        fL = False
        for i in str :
            if i.isupper() :
                fL = True
        return fL
    def checkNameLc(str):               #creating a function that will loop through each character in a given string and will return true if one lower character is found.
        fLc = False
        for i in str :
            if i.islower() :
                fLc = True
        return fLc            
    def checkNum(str) :                 #creating a function that will loop through each character in a given string and will return true if one number is found.
        fN = False
        for i in str :
            if i.isdigit() :
                fN = True
        return fN                    
    nameUser = input("Please enter your username: ").strip()     #User will input user name to be checked and will remove any extra spaces before and after the input.
    if len(nameUser) <= 1 :                                      #Condition for empty input or one character
        print("Username requires more than one character.")
    elif len(nameUser) > 20 :                                    #Condition for input with more than 20 characters.
        print("Username exceeds 20 characters.")    
    elif nameUser.islower() :                                    #Condition for input with only lowercase characters.
        print("Username requires uppercase characters and one digit.")
    elif nameUser.isdigit() :                                    #Condition for input with only numbers.
        print("Username requires atleast one uppercase letter.")
    elif nameUser.isalpha() :                                    #Condition for input with only letters.
        print("Username requires atleast one number.")  
    elif checkNameLc(nameUser) and checkNum(nameUser) :          #Condition for input with lowercase character and one number.
        print("Username has numbers, but is missing one uppercase letter.")          
    elif len(nameUser) > 1 and len(nameUser) <= 20 :             #First layer of condition that checks if user input is between 2 to 20 characters.
        if checkName(nameUser) == True and checkNum(nameUser) == True :     #Second layer of condition that will check if user name has one uppercase character and one number.
            print("Username meets requirements, congratulations!")
            