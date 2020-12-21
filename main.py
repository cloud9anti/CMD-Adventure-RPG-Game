'''
I am alex! I am the best!
'''

import random
import changestats
import randomEvents
import monsters
import time
import sound
from playsound import playsound

path = 'c:/users/antic/rpg/'
path = ''


#change the strength to a random int 
def newChar():
    changestats.modify("strength",str(random.randint(6, 12)))
    basehp=changestats.modify("hitpoints",str(random.randint(20, 30)))
    changestats.modify("basehp",basehp)
    changestats.modify("luck",str(random.randint(6, 12)))
    changestats.modify("magic",str(random.randint(6, 12)))
    changestats.modify("level",str(random.randint(1)))
    changestats.modify("experience",str(random.randint(0)))
enemyNum = random.randint(2, 4)

inv = changestats.get("inv").strip('][').split(', ') 
bank = changestats.get("bank").strip('][').split(', ') 
location = changestats.get("location")


'''
1) A function that displays the inventory in a simple way, 
telling the player how many of each card they have.
2) if there's more than 1 King, Queen, or Jack, I add an 's'
'''

def determineFace(card):
    if card==11:
        print("Jack!")
    elif card==12:
        print("Queen!!")
    elif card==13:
        print("King!!!")
    else:
        print(card)

def simplify():

    inv = changestats.get("inv").strip('][').split(', ') 
    inv = [int(s) for s in inv]
    inv.sort()
    
    print("Here are your cards:")
    counter=1
    myString=""
    for i in range(len(inv)):
        if i+1<len(inv) and inv[i]==inv[i+1]:
            counter+=1
        else:
            myString+='  ['
            if inv[i]==11:
                myString+="Jack"
                #If there are more than 1 of a face card, add an 's'
                if counter>1:
                    myString+="s"
            elif inv[i]==12:
                myString+="Queen"
                if counter>1:
                    myString+="s"
            elif inv[i]==13:
                myString+="King"
                if counter>1:
                    myString+="s"                     
            else: myString+=str(inv[i])
            myString+="]"
            myString+="x"
            myString+=str(counter)
            counter = 1
    print("-------------------------------------------------------------------------------------------------------------")
    print(myString)
    print("-------------------------------------------------------------------------------------------------------------")
    print("You have",changestats.get("money"),"gold!")
        
    
    return inv

def levelUp(xpGain):
    xpGain = int(xpGain)
    changestats.get("level")

    level = int(changestats.get("level"))
    xp = int(changestats.get("experience"))
    print("XP gained:",xpGain)
    time.sleep(2)
    print('\n'*40)
    sound.play("exp.wav")
    time.sleep(.25)
    for i in range(xpGain):
        
        xp+=1.000/(1+level*.1)
        xpGain-=1
        
        randomEvents.progress(xp,xpGain)
        time.sleep(.004-(level*.00005)+(i/2000000))
        if xp>=100:
            sound.stop()

            print('\n'*30)
            print("------------------------------------------")
            print("\n Level up! Your level is now",level)
            print("------------------------------------------")
            randomEvents.progress(xp,xpGain)
            xp=0
            level+=1
            playsound("ding.wav")

            sound.play("exp.wav")
            print('\n'*40)
    sound.stop()
    time.sleep(2)
    xp = int(xp)
    changestats.modify("experience",str(xp))        
    changestats.modify("level",str(level)) 
    travel(False)


def inventory(func, inv, bank):
    bank = changestats.get("bank").strip('][').split(', ') 
    print("This is your inventory!")
    inv = simplify()
    cont = 0
    print("Bank:",bank)
    while cont==0:
        say=input('''
        Type r to return!

        ''')
        #Return to previous page.
        if say=="r":
            cont = 1
            return func(inv, bank, True)
def pack(inv, bank):
    packs = int(changestats.get("packs"))
    
    if packs>0:
        
        card1 = random.randint(1,13)
        card2 = random.randint(1,13)
        card3 = random.randint(1,13)
        card4 = random.randint(1,13)
        card5 = random.randint(1,13)
        inv.append(card1)
        inv.append(card2)
        inv.append(card3)
        inv.append(card4)
        inv.append(card5)
        packs-=1        
        changestats.save(packs, "packs")
        randomEvents.openPack(card1, card2, card3, card4, card5)


        
        # Save the cards to the .ini file.
        changestats.save(inv, "inv")
        changestats.save(bank, "bank")
        
        #open again
        choice = ""
        choice = input("                           Press 'r' to return. ENTER to keep going!")
        if choice!='r':
            pack(inv, bank)

    else:
        print("Sorry, you don't have any packs to open!")
        time.sleep(2)
    
def map():
    print('\n' * 12)


    bank = changestats.get("bank").strip('][').split(', ') 
    inv = simplify()
    randomEvents.map()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Where would you like to go? ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")

    cont = 0
    while cont==0:
        say=input('''
        Type 'city' to go downtown.                    Type 'd' to go to the digsite.
        Type 'north' to go to the North Pole.          Type 'home' to go back home.
        
        Type 'close' to close the map
  
        
        ''')

        if say=="home":
            sound.stop()
            cont = 1
            home(inv, bank)
        if say=="north":
            sound.stop()
            cont = 1
            northern(inv, bank)
        if say=="d":
            sound.stop()
            cont=1
            digsite(inv, bank)
        if say=="city":
            sound.stop()
            cont=1
            city(inv, bank)
        if say=="close":
            travel(True)


def digsite(inv,bank, music = False):

    print('\n' * 12)
    
    #Play music if it is not already playing. This prevents a restart. 
    if music==False:
        sound.play(path+"jazzrock.mp3")
    
    changestats.modify("location",'digsite')
    bank = changestats.get("bank").strip('][').split(', ') 
    inv = simplify()
    #randomEvents.house()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Back to work. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")

    cont = 0
    print("        |-------------------------------------------------------------|")
    print("        |Type 'dig' to start digging! You are currently at", changestats.get("meters"),"meters!|")
    while cont==0:
        say=input('''        |-------------------------------------------------------------|
        
        Type 'inv' to open your bag!
        Type 'map' to open the map!
        Type 'pack' to open a card pack!
        Type 'gamble' to gamble!

        
        ''')

        if say=="inv":
           print("Opening the bag!")
           time.sleep(1)
           cont = 1
           inventory(digsite, inv, bank)
        if say=="pack":
            pack(inv, bank)
            cont = 1
            digsite(inv,bank, True)

        if say =="map":
            
            cont = 1
            map()

        if say=="dig":
            answer=False
            while answer==False:
                duration = input("How many minutes would you like to dig? (1-20)")
                if int(duration)>=0 and int(duration)<21:
                    answer = True
            
            levelUp(randomEvents.digGame(int(duration)*60))
            digsite(inv,bank, True)
            cont = 1
        if say=="gamble":
            levelUp(randomEvents.gamble())
            cont = 1
            digsite(inv,bank,True)

            


def city(inv,bank, music = False):
    

    print('\n' * 12)
    
    #Play music if it is not already playing. This prevents a restart. 
    #if music==False:
        #sound.play(path+"home.wav")
    
    changestats.modify("location",'digsite')
    bank = changestats.get("bank").strip('][').split(', ') 
    inv = simplify()
    #randomEvents.house()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Back to work. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")

    cont = 0
    while cont==0:
        say=input('''

        Type 'inv' to open your bag!
        Type 'map' to open the map!
        Type 'pack' to open a card pack!

        
        ''')
        print("         Type 'dig' to start digging! You are currently at", changestats.get("meters"),"meters!")
        if say=="inv":
           print("Opening the bag!")
           time.sleep(1)
           cont = 1
           inventory(digsite, inv, bank)
        if say=="pack":
            pack(inv, bank)
            cont = 1
            city(inv,bank)

        if say =="map":
            cont = 1
            map()

        if say=="dig":
            answer=False
            while answer==False:
                duration = input("How many minutes would you like to dig? (1-20)")
                if int(duration)>0 and int(duration)<21:
                    answer = True
            
            randomEvents.digGame(duration)

            cont = 1

def home(inv, bank, music = False):
    print('\n' * 12)
    
    #Play music if it is not already playing. This prevents a restart. 
    if music==False:
        sound.play(path+"home.wav")
    
    changestats.modify("location",'home')
    bank = changestats.get("bank").strip('][').split(', ') 
    inv = simplify()
    randomEvents.house()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Welcome home! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")

    #print("Bank:",bank)
    print("Would you like to enter the town?")
    cont = 0
    while cont==0:
        say=input('''
        Type 'todo' to see to-do list.                 Type 'b' to bank! 
        Type 'north' to go to the North Pole.          Type 'c' to play cards against a monster!
        Type 'sleep' to take a rest!                   Type 'm' to create a monster!
        Type 'inv' to open your bag!                   Type 'fish' to go fishing!
        Type 'map' to open the map!
        Type 'pack' to open a card pack.
        
        ''')

        if say=="f":
            sound.stop()
            cont = 1
            fighting()
        if say=="north":
            sound.stop()
            cont = 1
            northern(inv, bank)
        if say=="sleep":
            print("zzZZzZZz...")
            time.sleep(3)
            print("You feel refreshed!")
            time.sleep(1)
            cont = 1
            home(inv, bank, True)
        if say=="todo":
            randomEvents.todo()
            cont = 1
            home(inv, bank, True)
        if say=="inv":
           print("Opening the bag!")
           time.sleep(1)
           cont = 1
           inventory(home, inv, bank)
        if say=="pack":
            pack(inv, bank)
            cont = 1
            home(inv,bank, True)
        if say =="m":
            monsters.createMonster()
            cont = 1
            time.sleep(2)
            home(inv, bank, True)
        if say =="map":
            cont = 1
            map()
        if say =="c":

            monsters.viewMonster()
            print("Choose a difficulty from 0-9: ")
            x=input("Or type 'tournament' for a challenge... 'xt' to lose all your cards!\n")
            sound.stop()
            if x=="tournament":
                for i in range(3):
                    cards(inv, bank, 1, 1)
            elif x=="xt":
                for i in range(20):
                    cards(inv, bank, 6, .1)
            else:
                cards(inv, bank, int(x), 1.5)
            cont = 1
            time.sleep(2)
            home(inv, bank)
        #Bank your items.
        if say=="b":
            sound.stop()
            cont = 1
            bank+=inv
            #inv=['Beer']
            
            # Save the stats in the .ini file.
            changestats.save(inv, "inv")
            changestats.save(bank, "bank")
            
            #refresh the inventory
            home(inv, bank, True)
        if say=="fish":
            #play music

            print("Gone fishing!")
            randomEvents.fishing(1,7,0,1,inv)
            
            #stop music
            cont = 1
            time.sleep(1.5)
            home(inv, bank, True)

    
def northern(inv, bank, music = False):

    
    #Play music if it is not already playing. This prevents a restart. 
    if music==False:
        sound.play("trip.wav")
        
    print('\n' * 12)
    changestats.modify("location",'northern')
    inv = simplify()
    randomEvents.north()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~ Welcome to the north pole!! ~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")
    cont = 0
    while cont==0:
        say=input('''
        Type f to look for a fight!             Type 'map' to open the map!
        Type home to go back home.
        Type 'sleep' to take a rest!
        Type 'inv' to open your bag!
        Type 'fish' to go fishing!
        Type 'trip' to go on a fishing trip!
        ''')
        if say=="f":
            cont = 1
            fighting()
        if say=="home":
            cont = 1
            home(inv, bank)
        if say=="sleep":
            print("zzZZzZZz...")
            time.sleep(3)
            print("You feel refreshed!")
            time.sleep(1)
            cont = 1
            northern(inv, bank, True)
        if say=="inv":
            print("Opening the bag!")
            time.sleep(1)
            cont = 1
            inventory(northern, inv, bank, True)
        if say =="map":
            cont = 1
            map()
        if say=="fish":
            #play music
            sound.stop()
            sound.play("fish.wav")
            print("Gone fishing!")
            xpReward = randomEvents.fishing(6,14,4,1.5,inv)
            time.sleep(1)
            #stop music
            sound.stop()
            levelUp(xpReward)
            
            cont = 1
            time.sleep(1)
            northern(inv, bank)
        if say=="trip":
            choice = input("How long? press '1' for minutes and '2' for much longer. \n")
            #play music
            sound.play("trip.wav")
            if choice=='1':
                print("\n We'll be back in no time!")
            else:
                print("\n Prepare for a long expedition...")
            xpReward = 0
            for i in range(5):
                if choice =='1':
                    xpReward+=randomEvents.fishing(7,15,4,2,inv)
                else:
                    xpReward+=randomEvents.fishing(16,23,10,6,inv, 'ocean2')
                if i<3:
                    print(4-i,"trips remaining.") 
                elif i==3:
                    print("1 trip remaining.")
                else:
                    print("Time to go home!")
            #stop music
            time.sleep(2)
            sound.stop()

            
            cont = 1

            levelUp(xpReward)
            northern(inv, bank)
    
def cards(inv, bank, difficulty, speed):
    #Load the inventory
    bank = changestats.get("bank").strip('][').split(', ')
    print('\n' * 6)
    print("________________________________")
    print("Let's DUEL!!!")
    print("________________________________")
    monList = monsters.getMonList()
    randMonster = random.randint(0,len(monList)-1)
    print("You will fight:",monList[randMonster].get('name'))
    monsterCard = int(monList[randMonster].get('hp')) + difficulty
    print("He has",monsterCard,"HP!")
    
    card1 = int(random.choice(inv))
    card2 = int(random.choice(inv))
    card3 = int(random.choice(inv))
    print("Drawing three cards...")
    print('\n')
    time.sleep(speed)
    #print your hand
    randomEvents.showHand(card1, card2, card3)
    choice = input("Choose a card: \n")

    yourCard = 0
    if choice == '1':
        yourCard = card1
    elif choice == '2':
        yourCard = card2
    else:
        yourCard = card3

    
    #print the name of the card
    print("-------------------------------------------------------")
    determineFace(yourCard)
    print("-------------------------------------------------------")
    time.sleep(1.5*speed)
    if yourCard>monsterCard:
        print("you win! You get their card!")
        inv.append(monsterCard)
    elif yourCard<monsterCard:
        print("you lost! You lose your card...")
        inv.remove(yourCard)
        
        #second chance!
        print("Adding another card! It's a...")
        newCard = int(random.choice(inv))
        time.sleep(speed)
        
        #print the name of the card
        print("-------------------------------------------------------")
        determineFace(newCard)
        print("-------------------------------------------------------")
        time.sleep(speed)
        cardTotal = yourCard+newCard
        print("Your total is...",cardTotal,"!")
        time.sleep(.5*speed)
        if cardTotal>monsterCard:
            print("you win! You get their card!")
            if monsterCard>13:
                #earn excess gold
                money = int(changestats.get("money"))
                bonus = money+monsterCard-13
                changestats.modify("money",str(money+monsterCard-13))
                print("You also earned a bonus",monsterCard-13,"gold!")
                monsterCard=13
            
            inv.append(monsterCard)
        else:
            print("Not enough! You lost your other card... =(")
            inv.remove(newCard)
    else: print("It's a draw!")
    
    
    # Save the cards to the .ini file.
    changestats.save(inv, "inv")
    changestats.save(bank, "bank")
  
  
#fighting() 
def battle():
    enemyNum = random.randint(4, 6) + int(changestats.get("danger"))
    place="nowhere"
    print("________________________________")
    print("Prepare yourself!", enemyNum,"enemies are coming!")
    print("________________________________")
    time.sleep(2)
    for i in range(enemyNum):
        time.sleep(.200)
        enemyStrength=randomEvents.battle(random.randint(1, 5))
        hp = int(changestats.get("hitpoints"))
        money = int(changestats.get("money"))
        changestats.modify("hitpoints",str(hp-enemyStrength))
        print("You earned",enemyStrength-1,"gold. HP:",changestats.get("hitpoints"))
        print("________________________________")
        changestats.modify("money",str(money+enemyStrength-1))
    if int(changestats.get("hitpoints")) >=1:
        print("Congratulations! You survived!")
        randomEvents.win()
        cont = 0
        while cont==0:
            say=input('''
            Type g to continue grinding...
            Type i to increase difficulty...
            Type r to reduce difficulty...
            Type 'home' to return home!
            ''')
            if say=="g":
                cont = 1
            if say=="i":
                changestats.modify("danger",str(int(changestats.get("danger"))+1))
                cont = 1
            if say=="r":
                if int(changestats.get("danger"))>=1:
                    changestats.modify("danger",str(int(changestats.get("danger"))-1))
                cont = 1
            if say=="home":
                place="home"
                return place
    else:
        print("I'm sorry to say that you are dead.")
        randomEvents.dead()
    print("you have",int(changestats.get("money")),"gold.")
    return place


#newChar()
basehp=changestats.get("basehp")

# changestats.read("strength")
# changestats.read("hitpoints")
# changestats.read("luck")
# changestats.read("magic")


#battle loop
def fighting():
    fight=True
    while int(changestats.get("hitpoints"))>=0 and fight==True:

        changestats.modify("hitpoints",basehp)  #reset hp
        if battle()=="home":
            fight=False
            home(inv, bank)
        money = int(changestats.get("money"))   #check if you can spent money
        if money>=500:
            #level up!
            
            print("would you like to advance a level for 500g? Press enter!")
            changestats.modify("money",str(money-500))
            changestats.modify("basehp",str(int(changestats.get("basehp"))+1))
            print("Congratulations! Your HP is now",changestats.get("basehp"),"!!!")
    #reset hp
    changestats.modify("hitpoints",basehp)
    
   
def travel(bool):
    location = changestats.get("location")
    if location == 'home':
        home(inv, bank, bool)
    elif location == 'northern':
        northern(inv, bank, bool)
    elif location == 'digsite':
        digsite(inv,bank, bool)
    elif location == 'city':
        city(inv, bank, bool)
def main():
    

    travel(False)


if __name__ == "__main__":
    main()