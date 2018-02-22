import time #Allowed to make a counter go down fow an error to occur. Just a Joke though
import random#Allows us to make use of the random function. Able to pick a random word from the list.

name = raw_input("What is your name? ")

print "Hi goody2shoes, " + name, "Time to play hangman!:^]"#Intro. Allows for player to imput their name
time.sleep(1)
print "whats happened to my life.."#Soemthing  random. Comedic effect
time.sleep(2)
Words = ['bigchickens'    #The entire list of words
'fatgorillas',
'spellingcheese',
'breathingdoritodust',
'noonecantouchdis',
'_',
'hwastsDword',
'spelloutchicken',
'1$drinkfrommickeyDs',
'whosaidthiswaseasy',
'cringycringiscringe',
'one2threeohnowhatsleft',
'cameronsmiddlename',
'dinobrand',
'kaynmain',
'twitchisdumb',
'bigphatchickens',
'wheredogsaremade',
' ',
'',
'1',
'nokheating',
'trentsucksatleague',
'silverforlife',
'friedpotatoe',
'wherethemicat',
'leosucksatsmash',
'ThIsHaSTo B e Th E HArDe sT WoDr HeyA',
]

word = (random.choice(Words))#Selects a random word from the lsit
print "Start guessing in 3"#joke
time.sleep(1)#time until the next text appears
print "Start guessing in 2" #joke
time.sleep(1)#time until the next text appears
print "Start guessing in 3"#joke
print "Error 404 inbound, No way we getting out of this one boss"#joke
time.sleep(3)#time until the next text appears
print "Sike you thought I was Counting Down HA!"#joke


guesses = ''

turns = 10 #Amount of tries you have 

while turns > 0:#The conditions         

    failed = 0    #you win         
    
    for char in word: #conditions for a character in words     

        if char in guesses: #What happens after character in word
   
            print char,#puts the character in to blank    

        else:

            print "_",     #keep the blank
       
            failed += 1    #does not fail if it is = or more than one
    if failed == 0:     #what happens of it reaches zero   
        print "You won"#prints if you are successful
        break              

    guess = raw_input("guess a character:")#conditions if guess is wrong
    guesses += guess                    
    if guess not in word:  #conditions if guess is wrong
        turns -= 1   #take away one turn if you are wrong     
        print "Wrong"    #Appears if wrong
        print "You have", + turns, 'more guesses' #Says the amount of turns 
        if turns == 0:#What happens once you out of turns
            print "Why couldnt you pass this and make it to round 2... and the answer was ->", Words#if you lose, this appears
Wordz= [#word bank
'CANT TOUCH RAMMUS',
'LEAGUE COPYRIGHT',
'leo loses blood pressure to his brain with them phat glasses',
'thotdestroying CAMERON',
'cantevenhitfor1mil',
'dokkanbattleteqisdBEST',
'cant get chinese food from KFC',
'Franz eats dogs',
'honey badger Dont give a ###',
'when u havent started ur hw for orkeny',
'orkney>insert cool hero here',
]
wordy = (random.choice(Wordz))#picks a random word from the word bank

if failed == 0:          #if you win the previous one, You move on to this one  
    print "Alright We in my corner now, " + name, "Time to gam i mean sm i mean lets DO THIS!"#joke
    time.sleep(5)#time it takes for the next text to appear
    print "You better get better for this one chimp"#joke
    print "ALRIGHT NERD ITS TIME FOR HARD MODE HA THERES NO WAY OF CHANGING THE DIFFICULTEEEEE THERES CAPITALS IN THIS ONE"#joke
    
    buritos = ''#Buritos is the same thing as guesses from line49
    dubs = 25#dubs is equal to turn from line51
    while dubs > 0: #Same as line53        
        chicken = 0        #chicken is equal to fail. Same as line55         
        for char in wordy:   #Condition if the characters being in the word 
            if char in buritos:    #If the the charcter is in the word, then...
                print char,  #fills in the blank  
    
            else:
                print "_", #if its wrong, keep the blank    
                chicken += 1    #adds a point to your tries
        if chicken == 0: #amount required to win       
            print "You won"  #appears if one
            break           
    
    
        noodles = raw_input("guess a character:") #noodels equals guesses. Works the same as line72
        buritos += noodles   #Same way line 73 works just with different name                 
        if noodles not in wordy:  #if guess is incorrect, then...
            dubs -= 1  #dubs equals turn. Takes a way a turn if wrong      
            print "Wrong big question mark, this program is not designed to assume your gender" or "GET YOUR HEAD OUT OF YOUR. *Loudspeaker*'This is the FBI'.. nevermind your doing great"#joke   
            print "You have", + dubs, 'more buritos' #informs you how many turns you have left
            if dubs == 0:  #What happens once your dub counter equals zero
                print "YOU SUCK WHY CANT YOU UNDERSTAND WHAT THIS IS YOU CHIMPANZ " + wordy#Joke


            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            