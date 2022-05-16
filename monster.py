#Program name: monster.py
#Author: David Easton
#Date: 5/2/2022
#Summary: Create a base class for battlers. This is the base for the hero and
# monsters.
#Variables:

#-------Monster Storage Class (StoredMonster)---------
# self.name - string name of monster
# self.element - 0-6 value to determine element
                
#define Monster data storage class. Only Accessed by system
class StoredMonster:
    #initialize function
    def __init__(self, name, element):
        self.name = name
        self.element = element
    #Mutators
    def setStoredName(self, name):
        self.name = name
    def setStoredElement(self, element):
        self.element = element
    #Accessors
    def getStoredName(self):
        return self.name
    def getStoredElement(self):
        return self.element
    
