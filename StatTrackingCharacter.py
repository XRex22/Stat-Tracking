"""
Program: StatTrackingCharacter.py
Author: Hunter Moss
Last date Modified: 4/11/2024
"""

#User input for file name
fileName = input("Enter name of file: ")

#List of user decisions // To be replaced with Buttons in the GUI
decisionOptions = {
    "1": "Create a character",
    "2": "Edit a character"
}

#Ask if user would like to continue making characters 
def characterCreate():
    finish = "no"
    while True:

        #User is not done creating new characters
        if finish.lower() == "no":
            name = input("Enter character name: ")
            health = input("Enter character health: ")
            will = input("Enter character will: ")
            per = input("Enter character perception: ")
            strength = input("Enter character strength: ")
            dex = input("Enter character dexterity: ")
            intel = input("Enter character intelligence: ")
            newCharacter = [name, health, will, per, strength, dex, intel]

            #open file for appending
            file = open(fileName, 'a')

            #Write stats to file
            for stat in newCharacter:
                file.write(stat)

            #Clear newCharacter list for the next character's stats
            file.write('\n')
            file.close()
            newCharacter.clear
            finish = input("Are you finished making characters?: ")

        #User is finished creating characters
        elif finish.lower() == "yes":
            print("Done creating new characters.")
            break
        
        #User has entered an invalid input
        else:
            print("You have inserted an incorrect response. Please input Yes or No.")
            finish = input("Are you finished making characters?: ")
    return

def characterEdit():
    while True:
        file = open(fileName, 'r')
        for name, health, will, per, strength, dex, intel in file:
            print(name, health, will, per, strength, dex, intel)
            break
        return

for num, option in decisionOptions.items():
    print(num, option)
userDecision = input("Select an option: ")

#Have a way to get out of while loop. Better while condition?
while True:
    if userDecision == "1":
        characterCreate()
        break
    elif userDecision == "2":
        characterEdit()