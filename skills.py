#Program name: skills.py
#Author: David Easton
#Date: 5/2/2022
#Summary: Create a class for skills/attacks
#Variables:
# self.name: String for the class's name
# self.damage: Int value for base damage of attack
# self.element: Int value between 0-6 to determine skill element (0 - None, 1 - Fire, 2 - Water, 3 - Earth, 4 - Wind, 5 - Light, 6 - Dark)

#Define the class for skills
class Skills:
    #Initialization method. Involves base damage integer and 0-6 value for element.
    def __init__(self, name, damage, element):
        self.name = name
        self.damage = damage
        if element > 6 or element < 0:
            self.element = 0
        else:
            self.element = element
        
    #Accessors:
    def getName(self):
        return self.name
    def getDamage(self):
        return self.damage
    def getElement(self):
        return self.element
    #mutators
    def setSkill(self, skill):
        self.name = skill.getName()
        self.damage = skill.getDamage()
        self.element = skill.getElement()
    def setName(self, name):
        self.name = name
    def setDamage(self, damage):
        self.damage = damage
    def setElement(self, element):
        self.element = element

