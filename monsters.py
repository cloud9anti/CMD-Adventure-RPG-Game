import json
import os

class Monsters:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    def declare(self):
        print(self.name,"'s HP is:",self.hp)


def getMonList():
    

    if os.stat('MonsterList.txt').st_size:
        with open('MonsterList.txt', 'r') as f:
            monList = json.loads(f.read())


    for i in range(len(monList)):
        monList[i] = json.loads(monList[i])
    return monList
    
def viewMonster():
    monList = getMonList()
    print('\n' * 6)
    print("You peer into the cage and see the following monsters:")
    print("///////////////////////////////////////////////////")
    for i in range(len(monList)):
        print("Name:",monList[i].get('name'),"HP:", monList[i].get('hp'))
    print("///////////////////////////////////////////////////")
    print('\n' * 2)
def createMonster():
    print("What is the monster's name?")
    name = input()
    
    print("What is the monster's hp?")
    hp = input()
    monList = []
    #Get existing monsters from file
    
    monList = getMonList()
        
    '''
    Create and save a new monster.
    '''
    monList.append(Monsters(name,hp).__dict__)
    for i in range(len(monList)):
        monList[i] = json.dumps(monList[i])
       
    with open('MonsterList.txt', 'w') as f:
        f.write(json.dumps(monList))

    '''
    Load the monster from the file.
    '''
    #Now read the file back into a Python list object
    monList = getMonList()
        
    print("These are your monsters:")
    for i in range(len(monList)):
        print("Name:",monList[i].get('name'),"HP:", monList[i].get('hp'))
        
