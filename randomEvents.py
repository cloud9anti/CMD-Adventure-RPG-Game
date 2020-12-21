import random
import changestats
import time
import math
from playsound import playsound






def todo():

    print('''
    
    
    
    
    
    To-Do list:
    
    -Create tournaments
    -Create fishing tournaments and prizes or a special treasure.
    -Create new lands
    -Create a shop
    -Castle maze.
    -Treasure Chest
    -Card pack???
    
    
    ''')
    myVar = input("Type anything to leave.")
    
def progress(percentage, gain):
    gain = str(gain)
    while len(gain)<4:
        gain+=' '
    
    barString=''
    percentage = math.floor(percentage/2.5)
    for i in range(percentage):
        barString+='█'
    while len(barString)<40:
        barString+='░'
    print("XP gained:",gain,barString,end='\r')
    
def digGame(duration):

    meters = int(changestats.get("meters"))
    chance = 2
    level = int(changestats.get("level"))

    print("Welcome to the digsite! You have currently dug",meters,"meters.")



    def dig(meters, chance):
        prize = False
      
        
        

        
        if chance>= random.randrange(100):
            #time.sleep(1)
            chance = .1+(meters/300)
            prize = True
            playsound("money.wav", block=False)

        chance*=(1.1+(level/1000))
        if chance>100:
            chance = 100
            
        
        
        return chance, prize
    amount=0

    t_end = time.time() + duration #60 seconds
    xpGain = duration/4
    for i in range(100):
        while time.time() < t_end:
            digSound = random.choice(['dig.wav','dig2.wav','dig3.wav','dig4.wav'])
            if meters>350:
                digSound = random.choice(['pickaxe.wav','pickaxe2.wav','pickaxe3.wav','pickaxe4.wav'])
            playsound(digSound, block=False)
            chance = int(math.ceil(chance))
            underground(meters)
            print("Time left: less than",math.ceil(int(t_end-time.time())/60),"minute(s).")    
            print("You keep digging... You have found",amount,"card pack(s) on this trip.")
            print("you have a",chance,"% chance of finding treasure.")  
            
            time.sleep(2.8*meters/10/level)
            
            chance, prize = dig(meters,chance)
            
            
            
            if prize==True:
                amount+=1
            meters+=1
            xpGain+=int(5+(meters/100))
            
            
    print("You have found:",amount,"Card pack(s)!")
    print("You receive",int(xpGain),"experience!")
    input("Press ENTER to continue.")
    #save stats
    packs = int(changestats.get("packs"))
    changestats.save(packs+amount, "packs")
    changestats.save(meters, "meters")
    
    return xpGain

def battle(num):
    strength=0
    if num==1:
        strength = random.randint(3, 5)
        print("An angry bear has appeared!!! It did",strength,"damage.")
    elif num==2:
        strength = random.randint(2, 4)
        print("A wild boar has appeared!!! It did",strength,"damage.")
    elif num==3:
        strength = random.randint(7, 10)
        print("A large dragon has appeared!!! It did",strength,"damage.")
    elif num==4:
        strength = 1
        print("A small toad has appeared!!! It did",strength,"damage.")
    elif num==5:
        strength = random.randint(4, 6)
        print("A crazy witch has appeared!!! It did",strength,"damage.")
    else:
        print("No events???")
    return strength

def gamble():
    inv = changestats.get("inv").strip('][').split(', ') 
    inv = [int(s) for s in inv]
    inv.sort()
    
    print("Here are your cards:")
    counter=1
    myString=""
    sevenCards=""
    for i in range(len(inv)):
        if i+1<len(inv) and inv[i]==inv[i+1]:
            counter+=1
        elif inv[i]==7:
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
            sevenCards+=str(counter)
            myString+=str(counter)
            counter = 1
    print("-------------------------------------------------------------------------------------------------------------")
    print(myString)
    print("-------------------------------------------------------------------------------------------------------------")
    print("You have",changestats.get("money"),"gold!")
    print("-------------------------------------------------------------------------------------------------------------")    
    print("Want to gamble? bet a 7 card and 1 coin. If you win, you get a Queen card.")
    print("If you lose, I get your 7 card!")
    sevenCards=int(sevenCards)
    xpGain = 0
    cont=0
    choice='g'
    while cont==0:
        choice = input("Press 'g' to gamble or 'r' to return. \n")
        if choice=='r':
            cont=1
        elif choice =='g' and int(changestats.get("money"))>0:
            print("You bet one 7 card.\n")
            #pay one gold
            money = int(changestats.get("money"))
            changestats.modify("money",str(money-1))
            time.sleep(1)
            print('\n'*30)
            if random.randrange(2) ==1:
                playsound('money.wav', block=False)
                
                print("YOU WIN! You get a 10 card. You have",changestats.get("money"),"gold and",str(sevenCards)+'x',"'7 cards' left.\n")
                xpGain+=20
                inv.append(10)
                changestats.save(inv, "inv")
            else:
                sevenCards-=1
                playsound('ducky.wav', block=False)
                print("You lose! You have",changestats.get("money"),"gold and",str(sevenCards)+'x',"'7 cards' left.\n")
                xpGain+=10
                inv.remove(7)
                changestats.save(inv, "inv")
        elif int(changestats.get("money"))<1:
            print("\nYou don't have any money!\n")
        else:
            cont=0
    return xpGain
    

def openPack(card1,card2,card3,card4,card5):

    tempSound = []
    tempSound = ['ducky.wav']*5
    card1 = str(card1)
    card2 = str(card2)
    card3 = str(card3)
    card4 = str(card4)
    card5 = str(card5)
 
    if card1=='11':
        card1='J'
        tempSound[0] = 'goodCard.wav'
    elif card1=='12':
        card1='Q'
        tempSound[0] = 'goodCard.wav'
    elif card1=='13':
        card1='K'
        tempSound[0] = 'goodCard.wav'

    if card2=='11':
        card2='J'
        tempSound[1] = 'goodCard.wav'
    elif card2=='12':
        card2='Q'
        tempSound[1] = 'goodCard.wav'
    elif card2=='13':
        card2='K'
        tempSound[1] = 'goodCard.wav'
        
    if card3=='11':
        card3='J'
        tempSound[2] = 'goodCard.wav'
    elif card3=='12':
        card3='Q'
        tempSound[2] = 'goodCard.wav'
    elif card3=='13':
        card3='K'
        tempSound[2] = 'goodCard.wav'
        
    if card4=='11':
        card4='J'
        tempSound[3] = 'goodCard.wav'
    elif card4=='12':
        card4='Q'
        tempSound[3] = 'goodCard.wav'
    elif card4=='13':
        card4='K'
        tempSound[3] = 'goodCard.wav'

    if card5=='11':
        card5='J'
        tempSound[4] = 'goodCard.wav'
    elif card5=='12':
        card5='Q'
        tempSound[4] = 'goodCard.wav'
    elif card5=='13':
        card5='K'
        tempSound[4] = 'goodCard.wav'
        
    if card1!='10':
        card1='░'+card1
    if card2!='10':
        card2='░'+card2
    if card3!='10':
        card3='░'+card3
    if card4!='10':
        card4='░'+card4
    if card5!='10':
        card5='░'+card5
    blank1 = '░░'
    blank2 = '░░'
    blank3 = '░░'
    blank4 = '░░'
    blank5 = '░░'

    for i in range(6):
    
  
        if i==1:
            blank1 = card1
        if i==2:
            blank2 = card2
        if i==3:
            blank3 = card3      
        if i==4:
            blank4 = card4
        if i==5:
            blank5 = card5
        print('\n \n \n \n \n \n \n  '*2)

        lines =  ['                                  ┌─────────┐      ┌─────────┐']
        lines += ['                                  │░{}░░░░░░│      │░{}░░░░░░│'.format(blank1,blank2)]
        lines += ['                                  │░░░░░░░░░│      │░░░░░░░░░│'] * 5
        lines += ['                                  │░░░░░░{}░│      │░░░░░░{}░│'.format(blank1,blank2)]
        lines += ['                                  └─────────┘      └─────────┘']
        lines += ['                                          ┌─────────┐']
        lines += ['                                          │░{}░░░░░░│'.format(blank3)]
        lines += ['                                          │░░░░░░░░░│'] * 5
        lines += ['                                          │░░░░░░{}░│'.format(blank3)]
        lines += ['                                          └─────────┘']
        lines += ['                                  ┌─────────┐      ┌─────────┐']
        lines += ['                                  │░{}░░░░░░│      │░{}░░░░░░│'.format(blank4,blank5)]
        lines += ['                                  │░░░░░░░░░│      │░░░░░░░░░│'] * 5
        lines += ['                                  │░░░░░░{}░│      │░░░░░░{}░│'.format(blank4,blank5)]
        lines += ['                                  └─────────┘      └─────────┘']
        
            # make each line into a single list
        for index, x in enumerate(lines):
            lines[index] = ''.join(x)

        # convert the list into a single string
        lines = '\n'.join(lines)
        #print("(1)              (2)              (3)")
        print(lines, '\n')
        print("                                  You have ",changestats.get("packs"),"more pack(s)!")
        myVar = input("                               Press any key to open the packs!")
        if i<5:
            mySound = tempSound[i]
            playsound(mySound, block=False)
    
def showHand(card1, card2, card3):
    card1 = str(card1)
    card2 = str(card2)
    card3 = str(card3)
    if card1=='11':
        card1='J'
    elif card1=='12':
        card1='Q'
    elif card1=='13':
        card1='K'

    if card2=='11':
        card2='J'
    elif card2=='12':
        card2='Q'
    elif card2=='13':
        card2='K'
        
    if card3=='11':
        card3='J'
    elif card3=='12':
        card3='Q'
    elif card3=='13':
        card3='K'
        
    if card1!='10':
        card1='░'+card1
    if card2!='10':
        card2='░'+card2
    if card3!='10':
        card3='░'+card3
    lines =  ['┌─────────┐      ┌─────────┐      ┌─────────┐']
    lines += ['│░{}░░░░░░│      │░{}░░░░░░│      │░{}░░░░░░│'.format(card1,card2,card3)]
    lines += ['│░░░░░░░░░│      │░░░░░░░░░│      │░░░░░░░░░│'] * 5
    lines += ['│░░░░░░{}░│      │░░░░░░{}░│      │░░░░░░{}░│'.format(card1,card2,card3)]
    lines += ['└─────────┘      └─────────┘      └─────────┘']
        # make each line into a single list
    for index, x in enumerate(lines):
        lines[index] = ''.join(x)

    # convert the list into a single string
    lines = '\n'.join(lines)
    print("(1)              (2)              (3)")
    print(lines)
    
def ocean():
    print('''
    

                                                    ___   ____
                                                  /' --;^/ ,-_\     \ | /
                                                 / / --o\ o-\ \\\   --(_)--
                                                /-/-/|o|-|\-\\\|\\\   / | \\
                                                       |-|
                 v  ~.      v                          |-|
   v            /|                                     |-|O
               / |          v                          |-(\,__
        v     /__|__                                ...|-|\--,\_....
            \--------/                        ,;;;;;;;;;;;;;;;;;;;;;;;;,.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,
  ______   ---------   _____     ------  ~;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,
                                            ''')
                                            
def ocean2():
    print('''
    

                                              
                                          \ | /
                                         --(_)--
      v                                   / | \\
                            v                       
             v      /|\\                                         v                    v
                  /__| )
                /____| ))       v         v      v
      v       /______| )))                                                 v
            /________|  )))                               v
                    _|____))          
            \======| o o /                    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ______   ---------   _____     ------         ______   -------   _____     ---------      -----
                                            ''')
def fishing(min,max,neg,t,inv, map='ocean'):
    
    

    cardNum = random.randint(min,max)
    xpReward = (cardNum-neg)*t
    spacer=""
    if map=='ocean':
        ocean()
        spacer = "  "
    if map == 'ocean2':
        ocean2()
        spacer = "      "
    print(spacer,"           |")
    for i in range(cardNum):
        #time is faster at higher levels.
        time.sleep(t*(1-(int(changestats.get("level"))/150)))
        print(spacer,"           |")
    print(spacer,"           |  -------------------------------------------------------")
    print(spacer,"           |                 You caught something!")
    print(spacer,"           |  -------------------------------------------------------")
    playsound('money.wav', block=False)
    #use proper a/an articles
    if cardNum-neg == 8:
        print(spacer,"           |               It's an", cardNum-neg,"card!")
    elif cardNum-neg == 11:
        print(spacer,"           |               It's a Jack!")
    elif cardNum-neg == 12:
        print(spacer,"           |               It's a Queen!!")
    elif cardNum-neg == 13:
        print(spacer,"           |               It's a King!!!")
    else:
        print(spacer,"           |               It's a", cardNum-neg,"card!")
    print("")
        
    # Save the cards to the .ini file.
    inv.append(cardNum-neg)
    inv = [int(s) for s in inv]
    inv.sort()
    changestats.save(inv, "inv")
    
    return xpReward

def dead():
    print('''

            /   \\        
       /\\ | . . \\       
     ////\\|     ||       
   ////   \\ ___//\       
  ///      \\      \      
 ///       |\\      |     
//         | \\  \   \    
/          |  \\  \   \   
           |   \\ /   /   
           |    \/   /    
           |     \\/|     
           |      \\|     
           |       \\     
           |        |     
           |_________\    
      
    ''')
def win():
    print('''
        (͡ ° ͜ʖ ͡ °)
    ''')

def map():
    print('''
 +--------------------------------------------------------------------------------------------------------------+
!                                                                                 X  North Pole                !
!                                                                                                              !
!   |___| |___|  X   Castle                                                                                    !
!   |---| |---|                                                                                                !
!   |   | |   |                                                  X                                             !
!                                                          Monster Field                                       !
!                                                                                                              !
!                    .- - - - - - - - - - - - -.                                 ^  ^                          !
!                .--'      The River            `--..                         ^^ X ^ ^                         !
!             .-'    .- - - - - - - - - - - - -.     `-.                      ^^^  Digsite                     !
!           .'   ..-'                           `-.     `--..                                                  !
!         .'   .'                                  `..       `..                                               !
!        .   .'                                       `--.      `--.                                           !
!       .   .                                             `-.       `-.                                        !
!      .   .                                                 `--.      `-.                                     !
!     .   .                                                      `-.      `---.                                !
!    .   .                                                          `--.       `--.                            !
!   .   .  |-| |-| |-|                                                  `-.        `-.                         !
!  .   .  |-| |-| |-|                                                      `.         `.                       !
!     .       X                                                              .          `.                     !
!    .    LARGE CITY                                                          `. ..       -                    !
!                                                                               : :`-.     `.                  !
!                                                                                : :  `-.    `.                !
!                                                                                .  `.   `--.  `.              !
!                                                                                 :   \      `.  `.            !
!                                                                                  `.  `.     `.   `           !
!                                                                                    `-.`.   X :   HOME        !
!                                                                                       -.`-...:.              !
+--------------------------------------------------------------------------------------------------------------+

    ''')
def underground(meters):

    if meters<=100:
        print("\n"*30)
        print('''
        ________________________   ________________________
                        
                DEPTH: {}m      YOU
        ___________________________________________________
             
                        ...DEPTH 100???
             
             
            '''.format(meters))
    elif meters>100 and meters<=250:
        print("\n"*30)
        print('''
        ________________________   ________________________
                        
                DEPTH: 100m     
        ________________________   ________________________
        ........................   ........................
        ........................   ........................
                DEPTH: {}m    YOU
        ........................   ........................
        ........................   ........................
        ___________________________________________________
        
                        ...DEPTH 250???
            
            
            '''.format(meters))   
    elif meters>250 and meters<=500:
        print("\n"*30)
        print('''
        ________________________   ________________________
                        
                DEPTH: 100m     
        ________________________   ________________________
        ........................   ........................
        ........................   ........................
                DEPTH: 250m     
        ........................   ........................
        ........................   ........................
        ________________________   ________________________
        ^-^-^-^-^-^-^-^-^-^-^-^-   -^-^-^-^-^-^-^-^-^-^-^-^
        ^-^-^-^-^-^-^-^-^-^-^-^-   -^-^-^-^-^-^-^-^-^-^-^-^
                DEPTH: {}m     YOU  
        ^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^
        ^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^
        ___________________________________________________
        
                        ...DEPTH 500???
            
            
            '''.format(meters))   
    elif meters>500 and meters<=800:
        print("\n"*30)
        print('''
        ________________________   ________________________
                        
                DEPTH: 100m     
        ________________________   ________________________
        ........................   ........................
        ........................   ........................
                DEPTH: 250m     
        ........................   ........................
        ........................   ........................
        ________________________   ________________________
        ^-^-^-^-^-^-^-^-^-^-^-^-   -^-^-^-^-^-^-^-^-^-^-^-^
        ^-^-^-^-^-^-^-^-^-^-^-^-   -^-^-^-^-^-^-^-^-^-^-^-^
                DEPTH: 500m        
        ^-^-^-^-^-^-^-^-^-^-^-^-   -^-^-^-^-^-^-^-^-^-^-^-^
        ^-^-^-^-^-^-^-^-^-^-^-^-   -^-^-^-^-^-^-^-^-^-^-^-^
        ________________________   ________________________
        ^^^^^^^^^^^^^^^^^^^^^^^^   ^^^^^^^^^^^^^^^^^^^^^^^^
        ^^^^^^^^^^^^^^^^^^^^^^^^   ^^^^^^^^^^^^^^^^^^^^^^^^
        ^^^^^^^^^^^^^^^^^^^^^^^^   ^^^^^^^^^^^^^^^^^^^^^^^^
                DEPTH: {}m     YOU
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        ___________________________________________________        
        
                        ...DEPTH 800???
            
            
            '''.format(meters))  
    elif meters>800 and meters<=1000:
        print("\n"*30)
        print('''
        ________________________   ________________________
                        
                DEPTH: 100m     
        ________________________   ________________________
        ........................   ........................
        ........................   ........................
                DEPTH: 250m     
        ........................   ........................
        ........................   ........................
        ________________________   ________________________
        ^-^-^-^-^-^-^-^-^-^-^-^-   -^-^-^-^-^-^-^-^-^-^-^-^
        ^-^-^-^-^-^-^-^-^-^-^-^-   -^-^-^-^-^-^-^-^-^-^-^-^
                DEPTH: 500m        
        ^-^-^-^-^-^-^-^-^-^-^-^-   -^-^-^-^-^-^-^-^-^-^-^-^
        ^-^-^-^-^-^-^-^-^-^-^-^-   -^-^-^-^-^-^-^-^-^-^-^-^
        ________________________   ________________________
        ^^^^^^^^^^^^^^^^^^^^^^^^   ^^^^^^^^^^^^^^^^^^^^^^^^
        ^^^^^^^^^^^^^^^^^^^^^^^^   ^^^^^^^^^^^^^^^^^^^^^^^^
        ^^^^^^^^^^^^^^^^^^^^^^^^   ^^^^^^^^^^^^^^^^^^^^^^^^
                DEPTH: 800m        
        ^^^^^^^^^^^^^^^^^^^^^^^^   ^^^^^^^^^^^^^^^^^^^^^^^^
        ^^^^^^^^^^^^^^^^^^^^^^^^   ^^^^^^^^^^^^^^^^^^^^^^^^
        ^^^^^^^^^^^^^^^^^^^^^^^^   ^^^^^^^^^^^^^^^^^^^^^^^^
        ________________________   ________________________        
        DODOODODOOODODOODODODDOO   DOODODOOODODOODOODODODOD
        ODDOODODOOODODOODOODODOD   DOODODODOODOODODODOODODO
        DODODOODODODOODOODODOODO   ODDODOODODOODOODODOODODD
        DODOODODOOODODOODODODDOO   DOODODOOODODOODOODODODOD
                DEPTH: {}m     YOU  
        DODODOODODODOODOODODOODODODODDODOODODOODOODODOODODD
        DODODOODODODOODOODODOODOODOODDODOODODOODOODODOODODD
        DODODOODODODOODOODODOODODDOODDODOODODOODOODODOODODD   
        DODOODODOOODODOODODODDOOOODDOODODOOODODOODOODODODOD
        ___________________________________________________     

                        ...DEPTH 1,000???
            
            
            '''.format(meters))  

def house():
    print('''
       |                            *                  (
    | #|            *        .                                          .
      ||         .                        . .        .
       |                .                ` ' `               *
    #  |                             .' '. ' .' '.                   *
      "|  *           .                .. ' ' ..      .
    '  |                         *    '  '.'.'  '              .
       |                              .' '.'.' '.
     " |       .----------.          ' .''.'.''. '
       |       |__________|            . . : . .
       |_{}_{}/|__________|\{}_{}_{} _'___':'___'_ {}_{}_{}_{}_{}_{}_{}_{}
    ' #| || ||/____________\|| || ||(_____________)|| || || || || || || ||
    lc'\""""""||          ||""""""""""""(     )"""""""""""""""""""""""""""
    """""     |            |            _)   (_             .^-^.  ~""~
                             ~""~      (_______)~~"""~~     '._.'
        ~~""~~                     ~""~                     .' '.
                                                            '.,.'
                                                               `'`'
    ''')
    
def north():
    print('''
  ` : | | | |:  ||  :     `  :  |  |+|: | : : :|   .        `              .
      ` : | :|  ||  |:  :    `  |  | :| : | : |:   |  .                    :
         .' ':  ||  |:  |  '       ` || | : | |: : |   .  `           .   :.
                `'  ||  |  ' |   *    ` : | | :| |*|  :   :               :|
        *    *       `  |  : :  |  .      ` ' :| | :| . : :         *   :.||
             .`            | |  |  : .:|       ` | || | : |: |          | ||
      '          .         + `  |  :  .: .         '| | : :| :    .   |:| ||
         .                 .    ` *|  || :       `    | | :| | :      |:| |
 .                .          .        || |.: *          | || : :     :|||
        .            .   . *    .   .  ` |||.  +        + '| |||  .  ||`
     .             *              .     +:`|!             . ||||  :.||`
 +                      .                ..!|*          . | :`||+ |||`
     .                         +      : |||`        .| :| | | |.| ||`     .
       *     +   '               +  :|| |`     :.+. || || | |:`|| `
                            .      .||` .    ..|| | |: '` `| | |`  +
  .       +++                      ||        !|!: `       :| |
              +         .      .    | .      `|||.:      .||    .      .    `
          '                           `|.   .  `:|||   + ||'     `
  __    +      *                         `'       `'|.    `:
"'  `---"""----....____,..^---`^``----.,.___          `.    `.  .    ____,.,-
    ___,--'""`---"'   ^  ^ ^        ^       """'---,..___ __,..---""'
--"'                           ^                         ``--..,__ 
    ''')