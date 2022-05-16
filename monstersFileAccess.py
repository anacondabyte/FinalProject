#Program name: monstersFileAccess.py
#Author: David Easton
#Date: 5/15/2022
#Summary: Operates for file access regarding skills
#addMonster adds monsters
#deleteMonster deletes monsters
#searchMonster searches for a monster
#modifyMonster modifies monsters
import os

def addMonster():
    # Create a variable to control the loop.
    another = 'y'

    # Open the skills.txt file in append mode.
    monster_file = open('monsters.txt', 'a')

    # Add records to the file.
    while another == 'y' or another == 'Y':
        # Get the monster's record data.
        print('Enter the following monster data:')
        name = input('Name of new Monster: ')
        print('0 = None, 1 = Fire, 2 = Water, 3 = Earth, 4 = Wind, 5 = Light, 6 = Dark') 
        element = int(input('Element of monster (0-6 integer): '))
        while element <= -1 and element >= 7:
            element = int(input('Invalid element. Enter the element of monster(0-6 integer): '))
        # Append the data to the file.
        monster_file.write(name + '\n')
        monster_file.write(str(element) + '\n')

        # Determine whether the user wants to add
        # another record to the file.
        print('Do you want to add another skill?')
        another = input('Y = yes, anything else = no: ')

    # Close the file.
    monster_file.close()
    print('Monster successfully added to monsters.txt.')
def deleteMonster():
    # Create a bool variable to use as a flag.
    found = False

    # Get the monster to delete.
    search = input('Which monster do you want to delete? ')
    
    # Open the original monsters.txt file.
    monster_file = open('monsters.txt', 'r')

    # Open the temporary file.
    temp_file = open('temp.txt', 'w')

    # Read the first monster's name field.
    name = monster_file.readline()

    # Read the rest of the file.
    while name != '':
        # Read the quantity fields.
        element = int(monster_file.readline())

        # Strip the \n from the name.
        name = name.rstrip('\n')

        # If this is not the monster to delete, then
        # write it to the temporary file.
        if name != search:
            # Write the monster to the temp file.
            temp_file.write(name + '\n')
            temp_file.write(str(element) + '\n')
        else:
            # Set the found flag to True.
            found = True

        # Read the next monster name.
        name = monster_file.readline()

    # Close the coffee file and the temporary file.
    monster_file.close()
    temp_file.close()

    # Delete the original monsters.txt file.
    os.remove('monsters.txt')

    # Rename the temporary file.
    os.rename('temp.txt', 'monsters.txt')

    # If the search value was not found in the file
    # display a message.
    if found:
        print('The file has been updated.')
    else:
        print('That monster was not found in the file.')
# This program allows the user to search the
# coffee.txt file for records matching a
# description.

def searchMonster():
    # Create a bool variable to use as a flag.
    found = False

    # Get the search value.
    search = input('Enter a monster name to search for: ')

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

        # Determine whether this record matches
        # the search value.
        if name == search:
            # Display the record.
            print('Name:', name)
            print('Element:', str(element))
            print()
            # Set the found flag to True.
            found = True

        # Read the next description.
        name = monster_file.readline()

    # Close the file.
    monster_file.close()

    # If the search value was not found in the file
    # display a message.
    if not found:
        print('That monster was not found in the file.')

def modifyMonster():
    # Create a bool variable to use as a flag.
    found = False

    # Get the search value and the new quantity.
    search = input('Enter a monster name to search for: ')
    print('0 = None, 1 = Fire, 2 = Water, 3 = Earth, 4 = Wind, 5 = Light, 6 = Dark')
    new_element = int(input('Enter the new element: '))
    while new_element <= -1 and new_element >= 7:
        new_element = int(input('Invalid element. Enter the new element(0-6 integer): '))
    # Open the original monsters.txt file.
    monster_file = open('monsters.txt', 'r')

    # Open the temporary file.
    temp_file = open('temp.txt', 'w')

    # Read the first monster's name field.
    name = monster_file.readline()

    # Read the rest of the file.
    while name != '':
        # Read the quantity field.
        element = int(monster_file.readline())
        # Strip the \n from the name.
        name = name.rstrip('\n')

        # Write either this record to the temporary file,
        # or the new record if this is the one that is
        # to be modified.
        if name == search:
            # Write the modified record to the temp file.
            temp_file.write(name + '\n')
            temp_file.write(str(new_element) + '\n')
            # Set the found flag to True.
            found = True
        else:
            # Write the original record to the temp file.
            temp_file.write(name + '\n')
            temp_file.write(str(element) + '\n')

        # Read the next description.
        name = monster_file.readline()

    # Close the monster file and the temporary file.
    monster_file.close()
    temp_file.close()

    # Delete the original monsters.txt file.
    os.remove('monsters.txt')

    # Rename the temporary file.
    os.rename('temp.txt', 'monsters.txt')

    # If the search value was not found in the file
    # display a message.
    if found:
        print('The file has been updated.')
    else:
        print('That item was not found in the file.')


