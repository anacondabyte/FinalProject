#Program name: EASTON_DAVID_FINAL_PROJECT.py
#Author: David Easton
#Date: 5/2/2022
#Summary: Run RPG simulator on python that can be modified and used via a menu
#Variables: - Displayed with Each Function
# QUIT - sentinel value used to quit program
#Functions
#FileModification() - modifies text files
#generateSkills() - helps generate skills for battleSystem
#damageCalculator() - helps calculate damage with skills for battleSystem using input
#battleSystem() - operates as a battle system
#mainLoop() - helps run the program in amenu structure
#main() - Main
from skills import Skills
from monster import StoredMonster
import skillsFileAccess
import monstersFileAccess
import os
import random
QUIT = 9

#File Modification function
#Variables:
# fileMenu - int used for menu options
# skillsMenu - int used for menu options
# monstersMenu - int used for menu options
def fileModification():
    #Declare fileMenu variable for menu choice
    fileMenu = -1
    #Runs menu as long as fileMenu is not 9
    while fileMenu != QUIT:
        print("Enter 1 to modify skills.")
        print("Enter 2 to modify monsters.")
        print("Enter 9 to exit to main menu.")
        fileMenu = int(input("Enter your choice: "))
        #When accessing skills menu
        if fileMenu == 1:
            #Declare skillsMenu variable for menu choice
            skillsMenu = -1
            #Runs menu as long as skillsMenu is not 9
            while skillsMenu != QUIT:
                print("Enter 1 to add a skill.")
                print("Enter 2 to delete a skill.")
                print("Enter 3 to search for a skill.")
                print("Enter 4 to modify a skill.")
                print("Enter 9 to exit to modifications menu.")
                skillsMenu = int(input("Enter your choice: "))
                #Adding a new skill (1)
                if skillsMenu == 1:
                    skillsFileAccess.addSkill()
                #Deleting a skill (2)
                elif skillsMenu == 2:
                    skillsFileAccess.deleteSkill()
                #Searching fo a skill (3)
                elif skillsMenu == 3:
                    skillsFileAccess.searchSkill()
                #Modifiying an existing Skill (4)
                elif skillsMenu == 4:
                    skillsFileAccess.modifySkill()
                #For any unused values
                elif skillsMenu != 9:
                    print("Invalid Option. Type 1, 2, 3, 4, or 9.")
        #When accessing monsters menu
        elif fileMenu == 2:
            #Declare monstersMenu variable for menu choice
            monstersMenu = -1
            #Runs menu as long as monstersMenu is not 9
            while monstersMenu != QUIT:
                print("Enter 1 to add a monster.")
                print("Enter 2 to delete a monster.")
                print("Enter 3 to search for a monster.")
                print("Enter 4 to modify a monster.")
                print("Enter 9 to exit to modifications menu.")
                monstersMenu = int(input("Enter your choice: "))
                #Adding a new monster (1)
                if monstersMenu == 1:
                    monstersFileAccess.addMonster()
                #Deleting a monster (2)
                elif monstersMenu == 2:
                    monstersFileAccess.deleteMonster()
                #Searching for a monster (3)
                elif monstersMenu == 3:
                    monstersFileAccess.searchMonster()
                #Modifying a monster (4)
                elif monstersMenu == 4:
                    monstersFileAccess.modifyMonster()
                #For any values without any usage
                elif monstersMenu != 9:
                    print("Invalid Option. Type 1, 2, 3, 4, or 9.")
        #For any invalid integers
        elif fileMenu != 9:
                    print("Invalid Option. Type 1, 2, or 9.")
                    
#Generate skills for battle:
#Variables:
# randomSkill - int used for random number generation
# lengthSkill - int used for the length of input list
# storedValue1, storedValue2, storedValue3, storedValue4 - ints used to prevent duplication
# skill_1, skill_2, skill_3, skill_4 - Skills objects used for return value
def generateSkills(skillsList):
    #skill objects are skill objects 4 in total
    #randomSkill acts for RNG
    #storedValue variables prevent duplication
    #declare basic variables
    lengthSkill = len(skillsList)
    randomSkill = random.randint(0, lengthSkill - 1)
    storedValue1 = randomSkill
    #skill 1 declared
    skill_1 = skillsList[randomSkill]
    #Number generation
    randomSkill = random.randint(0, lengthSkill - 1)
            
    #multiple of these loops occur to prevent duplicates
    while randomSkill == storedValue1:
        randomSkill = random.randint(0, lengthSkill - 1)
    storedValue2 = randomSkill

    #skill 2 declared
    skill_2 = skillsList[randomSkill]
            
    #Number generation
    randomSkill = random.randint(0, lengthSkill - 1)
            
    #multiple of these loops occur to prevent duplicates
    while randomSkill == storedValue1 or randomSkill == storedValue2:
        randomSkill = random.randint(0, lengthSkill - 1)
    storedValue3 = randomSkill
            
    #skill 3 declared
    skill_3 = skillsList[randomSkill]

    #Number generation
    randomSkill = random.randint(0, lengthSkill - 1)
            
    #multiple of these loops occur to prevent duplicates
    while randomSkill == storedValue1 or randomSkill == storedValue2 or randomSkill == storedValue3:
            randomSkill = random.randint(0, lengthSkill - 1)
            
    #skill 4 declared
    skill_4 = skillsList[randomSkill]
    #return all four skills
    return skill_1, skill_2, skill_3, skill_4

#Element String function
#Variables:
# stringElement - string used for returning a string value
def elementToString(element):
    #Declare stringElement
    stringElement = "None"
    #If statements determining stringElement
    if element == 0:
        stringElement = "None"
    elif element == 1:
        stringElement = "Fire"
    elif element == 2:
        stringElement = "Water"
    elif element == 3:
        stringElement = "Earth"
    elif element == 4:
        stringElement = "Wind"
    elif element == 5:
        stringElement = "Light"
    elif element == 6:
        stringElement = "Dark"
    #return stringElement
    return stringElement   
#Damage function
#Variables:
# isStrong - Boolean used to determine damage multiplier
# multDamage - int used to determine damage multiplier
# finalDamage - int for calculating final damage
# newHealth final damage subtracted from health. Returned int
def damageCalculator(targetHealth, baseDamage, skillElement, targetElement, attackerAtk, targetDef):
    #determines damage calculation based on element
    isStrong = False
    if skillElement != 0:
        #Skill is Fire
        if skillElement == 1:
            #if Target is Wind
            if targetElement == 4:
                isStrong = True
        #Skill is Water
        elif skillElement == 2:
            #if Target is Fire
            if targetElement == 1:
                isStrong = True
        #Skill is Earth
        elif skillElement == 3:
            #if Target is Water
            if targetElement == 2:
                isStrong = True
        #Skill is Wind
        elif skillElement == 4:
            #if Target is Earth
            if targetElement == 3:
                isStrong = True
        #Skill is Light
        elif skillElement == 5:
            #if Target is Dark
            if targetElement == 6:
                isStrong = True
        #Skill is Dark
        elif skillElement == 6:
            #if Target is Light
            if targetElement == 1:
                isStrong = True
        #Damage multiplier declared and determined by isStrong
        multDamage = 1
        if isStrong == True:
            multDamage = 2
        #Calculate damage ((Base Damage + ((attack * 2) - defense) ) * multiplier)
        finalDamage = (baseDamage + ((attackerAtk * 2) - targetDef)) * multDamage
        # 0 damage or values less than 0
        if finalDamage <= 0:
            finalDamage = 0
            print("The attack was ineffective")
        else:
            print("The attack dealt ", str(finalDamage), " damage.")
        newHealth = targetHealth - finalDamage
        return newHealth
    
#Battle System function
#Variables:
# skills[] - list of skills (Skills)
# monstersName[] - list of monsters name (Strings)
# monstersElement[] - list of monsters elements (ints)
# skill_file - file opened for access of monsters
#   name - string for reading name string variables
#   damage - int for reading damage int variables
#   element - int for reading element int variables
# monster_file - file opened for access of monsters
#   name - string for reading name string variables
#   element - int for reading element int variables
#sizeSkills - int size of skills[]
#sizeMonsters - int size of monsters[]
#battleChoice - int for menu of monsters
    #mSkill_1, mSkill_2, mSkill_3, mSkill_4 = generated monster skills (Skills class)           
    #generated stats for monster:
        #monsterSelect = int for randomly picked monster
        #chosenMonster = StoredMonster class for data
        #mHealth - int for health
        #mAttack - int for attack
        #mDefense - int for defense
        #mSpeed - int for speed
        #mName - monster name string
        #mElement - int for element
        #mStringElement - string version of element
        #monsterSelect = input("Enter the monster's name: ")
                #monsterSearch = int that runs loop
                #doesExist = Boolean and loop to check if monster exists
                #searchMonster = stores a StoredMonster class
                        #If the monster's name matches monsterSelect
    #player attributes
        #pChosen: y/n string to check if player chose stats
        #pName: name of player string
        #pElement: int for element
        #pStringElement: string version of element
        #pHealth - int for health
        #pAttack - int for attack
        #pDefense - int for defense
        #pSpeed - int for speed
        #pSkill_1, pSkill_2, pSkill_3, pSkill_4 = generated player skills (Skills class)
    #Player wins! - pWin bool
    #Monster wins! - mWin bool
    #turnOrder = int that determines turn order
def battleSystem():
    #Declare empty lists
    skills = []
    monstersName = []
    monstersElement = []
    #------------Skill List--------------
        # Open the skills.txt file.
    skill_file = open('skills.txt', 'r')

    # Read the first monster's name field.
    name = skill_file.readline()

    # Read the rest of the file.
    while name != '':
        # Read the quantity field.
        damage = int(skill_file.readline())
        element = int(skill_file.readline())

        # Strip the \n from the name.
        name = name.rstrip('\n')
        #Create skill for list
        newSkill = Skills(name, damage, element)

        #add skill to list
        skills.append(newSkill)
        name = skill_file.readline()
    # Close the file.
    skill_file.close()
    #------------Monster List--------------
        # Open the monsters.txt file.
    monster_file = open('monsters.txt', 'r')

    # Read the first monster's name field.
    name = monster_file.readline()

    # Read the rest of the file.
    while name != '':
        # Read the quantity field.
        element = int(monster_file.readline())

        # Strip the \n from the name.
        name = name.rstrip('\n')
        #Create Stored Monster for list
        storedMonster = StoredMonster(name, element)

        #add stored monster to list
        monstersName.append(storedMonster.getStoredName())
        monstersElement.append(storedMonster.getStoredElement())
        name = monster_file.readline()

    # Close the file.
    monster_file.close()
    #declare number of monster/skill values
    sizeSkills = len(skills)
    sizeMonsters = len(monstersElement)
    #------------Menu-------------
    #declare battleChoice to establish a menu for battling
    battleChoice = -1
    #display options and create loop for menu
    if sizeSkills == 0 or sizeMonsters == 0:
        print("Insufficient Data. Please add monsters and skills.")
        battleChoice = 9
    while battleChoice != 9:
        print("Enter 1 to start battle with random monster.")
        print("Enter 2 to start battle with monster of choice.")
        print("Enter 9 to exit to main menu.")
        
        battleChoice = int(input("Enter your choice: "))
        #If entry is 1 or 2
        if battleChoice == 1 or battleChoice == 2:
        #---------Monster Generation--------------------------------------------
            #generate skills for monster
            mSkill_1, mSkill_2, mSkill_3, mSkill_4 = generateSkills(skills)
            
            #generate stats for monster
            mHealth = 500
            mAttack = random.randint(10, 40)
            mDefense = random.randint(10, 40)
            mSpeed = random.randint(10, 40)
            mName = ''
            mElement = 0
            #For monster Name/Element
            #If monster is randomly chosen
            if battleChoice == 1:
                monsterNum = random.randint(0, sizeMonsters)
                chosenMonster = StoredMonster(monstersName[monsterNum], monstersElement[monsterNum])
                mName = chosenMonster.getStoredName()
                mElement = chosenMonster.getStoredElement()
            #If monster is selected
            else:
                #Get input for monster name
                monsterSelect = input("Enter the monster's name: ")
                #Checks if monster exists
                monsterSearch = 0
                #Boolean and loop to check if monster exists
                doesExist = False
                while doesExist == False:
                    while monsterSearch != sizeMonsters and doesExist == False:
                        searchMonster = StoredMonster(monstersName[monsterSearch], monstersElement[monsterSearch])
                        #If the monster's name matches monsterSelect
                        if searchMonster.getStoredName() == monsterSelect:
                            doesExist = True
                            mName = searchMonster.getStoredName()
                            mElement = searchMonster.getStoredElement()
                        else:
                            monsterSearch += 1
                    if doesExist != True:
                        #Error message and get input for monster name
                        print(monsterSelect, " does not exist.")
                        monsterSelect = input("Enter the monster's name: ")
                        
            #create battleMonster Class      

            #provides string for element of monster
            #Display Monster info:
            mStringElement = elementToString(mElement)                  
            print("Monster Name: ", mName)
            print("Monster Element: ", mStringElement)
            print("Monster Health: ", str(mHealth))
            print("Monster Attack: ", str(mAttack))
            print("Monster Defense: ", str(mDefense))
            print("Monster Speed: ", str(mSpeed))            
           #-------Player creation--------------------------------
            #input for stats/attributes
            pName = input("Enter Player name: ")
            print('0 = None, 1 = Fire, 2 = Water, 3 = Earth, 4 = Wind, 5 = Light, 6 = Dark')
            pElement = int(input("Enter Player element (0-6): "))
            while pElement <= -1 and pElement >= 7:
                pElement = int(input("Invalid element. Enter Player element (0-6): "))
            pStringElement = elementToString(pElement)
            pHealth = 500
            pAttack = random.randint(10, 40)
            pDefense = random.randint(10, 40)
            pSpeed = random.randint(10, 40)
            #display stats
            print("Attack: ", str(pAttack))
            print("Defense: ", str(pDefense))
            print("Speed: ", str(pAttack))
            #allows player to change stats                 
            pChosen = input("Do you like these stats? (y/n): ")
            while pChosen != 'y' and pChosen != 'Y':
                if pChosen == 'n' or pChosen == 'N':
                    pAttack = random.randint(10, 40)
                    pDefense = random.randint(10, 40)
                    pSpeed == random.randint(10, 40)
                    #display stats
                    print("Attack: ", str(pAttack))
                    print("Defense: ", str(pDefense))
                    print("Speed: ", str(pAttack))
                    #allows player to change stats                 
                    pChosen = input("Do you like these stats? (y/n): ")
                else:
                    pChosen = ("Only y/Y or n/N allowed. Answer again: ")
                    
            #generate skills for player
            pSkill_1, pSkill_2, pSkill_3, pSkill_4 = generateSkills(skills)
            #Battle BEGINS!!!!
            pWin = False
            mWin = False
            turnOrder = 0
            #speed determines turn order
            if mSpeed > pSpeed:
                turnOrder = 0
            else:
                turnOrder = 1
            #BattleLoop
            while pWin == False and mWin == False:
                #Display Info
                print("____________________________________________")
                print(mName, " | ",mStringElement, " | ",mHealth)
                print(pName, " | ", pStringElement, " | ", pHealth)
                print("____________________________________________")
                if turnOrder == 0:
                    #Choose Monster's Attack
                    skillNum = random.randint(1, 4)
                    #Check random input
                    if skillNum == 1:
                        print(mName + " used " + mSkill_1.getName())
                        pHealth = damageCalculator(pHealth, mSkill_1.getDamage(), mSkill_1.getElement(), pElement, mAttack, pDefense)
                         
                    elif skillNum == 2:
                        print(mName + " used " + mSkill_2.getName())
                        pHealth = damageCalculator(pHealth, mSkill_2.getDamage(), mSkill_2.getElement(), pElement, mAttack, pDefense)
                    elif skillNum == 3:
                        print(mName + " used " + mSkill_3.getName())
                        pHealth = damageCalculator(pHealth, mSkill_3.getDamage(), mSkill_3.getElement(), pElement, mAttack, pDefense)
                    else:
                        print(mName + " used " + mSkill_4.getName())
                        pHealth = damageCalculator(pHealth, mSkill_4.getDamage(), mSkill_4.getElement(), pElement, mAttack, pDefense)
                    turnOrder = 1
                    
                    if pHealth <= 0:
                        mWin = True
                elif turnOrder == 1:
                    #Choose Player's Attack
                    #Display skills for choice
                    print("Skill #: Name | Element | Damage")
                    print("Skill 1: ", pSkill_1.getName(), " | ", elementToString(pSkill_1.getElement()), " | ", str(pSkill_1.getDamage()))
                    print("Skill 2: ", pSkill_2.getName(), " | ", elementToString(pSkill_2.getElement()), " | ", str(pSkill_2.getDamage()))
                    print("Skill 3: ", pSkill_3.getName(), " | ", elementToString(pSkill_3.getElement()), " | ", str(pSkill_3.getDamage()))
                    print("Skill 4: ", pSkill_4.getName(), " | ", elementToString(pSkill_4.getElement()), " | ", str(pSkill_4.getDamage()))
                    skillNum = int(input("Input skill number you want to use (1-4):"))
                    #Catch for bad Values
                    while skillNum <= 0 or skillNum >= 5:
                        skillNum = int(input("Invalid Entry. Input skill number you want to use (1-4):"))
                    #Check user input
                    if skillNum == 1:
                        print(pName + " used " + pSkill_1.getName())
                        mHealth = damageCalculator(mHealth, pSkill_1.getDamage(), pSkill_1.getElement(), mElement, pAttack, mDefense)
                         
                    elif skillNum == 2:
                        print(pName + " used " + pSkill_2.getName())
                        mHealth = damageCalculator(mHealth, pSkill_2.getDamage(), pSkill_2.getElement(), mElement, pAttack, mDefense)
                    elif skillNum == 3:
                        print(pName + " used " + pSkill_3.getName())
                        mHealth = damageCalculator(mHealth, pSkill_3.getDamage(), pSkill_3.getElement(), mElement, pAttack, mDefense)
                    else:
                        print(pName + " used " + pSkill_4.getName())
                        mHealth = damageCalculator(mHealth, pSkill_4.getDamage(), pSkill_4.getElement(), mElement, pAttack, mDefense)
                    turnOrder = 0
                    #Check for victory
                    if mHealth <= 0:
                        pWin = True
                #message for victory or loss
                if pWin == True:
                    print(mName, " successfully defeated!")
                if mWin == True:
                    print("Too bad! ", mName , " wins.")
                
                              
                
        elif battleChoice != 9:
            print("Invalid Option. Type 1, 2, or 9.")
def mainLoop():
    choice = -1
    #Run menu with sentinel value
    while choice != QUIT:
        print("Enter 1 to modify skill and monster data.")
        print("Enter 2 to access the battle simulator.")
        print("Enter 9 to quit.")
         #Check and accept input     
        choice = int(input("Enter your choice: "))
        if choice == 1:
            fileModification()
        elif choice == 2:
            battleSystem()
        elif choice != 9:
            print("Invalid Option. Type 1, 2, or 9.")
def main():
    mainLoop()
main()
