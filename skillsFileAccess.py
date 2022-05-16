#Program name: skillsFileAccess.py
#Author: David Easton
#Date: 5/15/2022
#Summary: Operates for file access regarding skills
#addSkill adds skills
#deleteSkill deletes skills
#searchSkill searches for a skill
#modifySkill modifies skills
import os

def addSkill():
    # Create a variable to control the loop.
    another = 'y'

    # Open the skills.txt file in append mode.
    skill_file = open('skills.txt', 'a')

    # Add records to the file.
    while another == 'y' or another == 'Y':
        # Get the skill's data.
        print('Enter the following skill data:')
        name = input('Name of new Skill: ')
        damage = int(input('Base damage of skill (integer): '))
        print('0 = None, 1 = Fire, 2 = Water, 3 = Earth, 4 = Wind, 5 = Light, 6 = Dark')
        
        element = int(input('Element of skill (0-6 integer): '))
        while element <= -1 and element >= 7:
            element = int(input('Invalid element. Element of skill (0-6 integer): '))

        # Append the data to the file.
        skill_file.write(name + '\n')
        skill_file.write(str(damage) + '\n')
        skill_file.write(str(element) + '\n')
        # Determine whether the user wants to add
        # another record to the file.
        print('Do you want to add another skill?')
        another = input('Y = yes, anything else = no: ')

    # Close the file.
    skill_file.close()
    print('Skill successfully added to skills.txt.')
def deleteSkill():
    # Create a bool variable to use as a flag.
    found = False

    # Get the skill to delete.
    search = input('Which skill do you want to delete? ')
    
    # Open the original skill.txt file.
    skill_file = open('skills.txt', 'r')

    # Open the temporary file.
    temp_file = open('temp.txt', 'w')

    # Read the first skill's name field.
    name = skill_file.readline()

    # Read the rest of the file.
    while name != '':
        # Read the quantity fields.
        damage = int(skill_file.readline())
        element = int(skill_file.readline())

        # Strip the \n from the name.
        name = name.rstrip('\n')

        # If this is not the skill to delete, then
        # write it to the temporary file.
        if name != search:
            # Write the skill to the temp file.
            temp_file.write(name + '\n')
            temp_file.write(str(damage) + '\n')
            temp_file.write(str(element) + '\n')
        else:
            # Set the found flag to True.
            found = True

        # Read the next skill name.
        name = skill_file.readline()

    # Close the coffee file and the temporary file.
    skill_file.close()
    temp_file.close()

    # Delete the original skill.txt file.
    os.remove('skills.txt')

    # Rename the temporary file.
    os.rename('temp.txt', 'skills.txt')

    # If the search value was not found in the file
    # display a message.
    if found:
        print('The file has been updated.')
    else:
        print('That skill was not found in the file.')
def searchSkill():
    # Create a bool variable to use as a flag.
    found = False

    # Get the search value.
    search = input('Enter a skill name to search for: ')

    # Open the skills.txt file.
    skill_file = open('skills.txt', 'r')

    # Read the first skill's name field.
    name = skill_file.readline()

    # Read the rest of the file.
    while name != '':
        # Read the quantity field.
        damage = int(skill_file.readline())
        element = int(skill_file.readline())

        # Strip the \n from the description.
        name = name.rstrip('\n')

        # Determine whether this record matches
        # the search value.
        if name == search:
            # Display the record.
            print('Name:', name)
            print('Damage:', str(damage))
            print('Element:', str(element))
            print()
            # Set the found flag to True.
            found = True

        # Read the next description.
        name = skill_file.readline()

    # Close the file.
    skill_file.close()

    # If the search value was not found in the file
    # display a message.
    if not found:
        print('That skill was not found in the file.')
def modifySkill():
    # Create a bool variable to use as a flag.
    found = False

    # Get the search value and the new quantity.
    search = input('Enter a skill name to search for: ')
    new_damage = int(input('Enter the new damage amount: '))
    print('0 = None, 1 = Fire, 2 = Water, 3 = Earth, 4 = Wind, 5 = Light, 6 = Dark')
    new_element = int(input('Enter the new element(0-6 integer): '))
    while new_element <= -1 and new_element >= 7:
        new_element = int(input('Invalid element. Enter the new element(0-6 integer): '))
    # Open the original skills.txt file.
    skill_file = open('skills.txt', 'r')

    # Open the temporary file.
    temp_file = open('temp.txt', 'w')

    # Read the first skill's name field.
    name = skill_file.readline()

    # Read the rest of the file.
    while name != '':
        # Read the quantity field.
        damage = int(skill_file.readline())
        element = int(skill_file.readline())
        # Strip the \n from the name.
        name = name.rstrip('\n')

        # Write either this record to the temporary file,
        # or the new record if this is the one that is
        # to be modified.
        if name == search:
            # Write the modified record to the temp file.
            temp_file.write(name + '\n')
            temp_file.write(str(new_damage) + '\n')
            temp_file.write(str(new_element) + '\n')
            # Set the found flag to True.
            found = True
        else:
            # Write the original record to the temp file.
            temp_file.write(name + '\n')
            temp_file.write(str(damage) + '\n')
            temp_file.write(str(element) + '\n')

        # Read the next name.
        name = skill_file.readline()

    # Close the skill file and the temporary file.
    skill_file.close()
    temp_file.close()

    # Delete the original skills.txt file.
    os.remove('skills.txt')

    # Rename the temporary file.
    os.rename('temp.txt', 'skills.txt')

    # If the search value was not found in the file
    # display a message.
    if found:
        print('The file has been updated.')
    else:
        print('That item was not found in the file.')


