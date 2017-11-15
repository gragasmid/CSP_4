import time
import random
name = raw_input("What is your name? ")

print "Hi goody2shoes, " + name, "Time to play hangman!:^]"

print "whats happened to my life.."
Words = ['bigchickens'
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

word = (random.choice(Words))
print "Start guessing in 3"
time.sleep(1)
print "Start guessing in 2"
time.sleep(1)
print "Start guessing in 3"
print "Error 404 inbound, No way we getting out of this one boss"
time.sleep(3)
print "Sike you thought I was Counting Down HA!"


guesses = ''

turns = 10

while turns > 0:         

    failed = 0             
    
    for char in word:      

        if char in guesses:    
            print char,    

        else:

            print "_",     
       
            failed += 1    
    if failed == 0:        
        print "You won"
        break              

    guess = raw_input("guess a character:")
    guesses += guess                    
    if guess not in word:  
        turns -= 1        
        print "Wrong"    
        print "You have", + turns, 'more guesses' 
        if turns == 0:
            print "Why couldnt you pass this and make it to round 2"
Wordz= [
'CANT TOUCH RAMMUS',
'LEAGUE COPYRIGHT',
'leo loses blood pressure to his brain with them phat glasses',
'thotdestroying CAMERON',
'cantevenhitfor1mil',
'dokkanbattleteqisdBEST',
'cantget chinese food from KFC',
'Franz eats dogs',
'honey badger Dont give a ###',
'when u haventstarted ur hw for orkeny',
'orkney>insert cool hero here',
]
wordy = (random.choice(Wordz))

if failed == 0:            
    print "Alright We in my corner now, " + name, "Time to gam i mean sm i mean lets DO THIS!"
    time.sleep(5)
    print "You better get better for this one chimp"
    print "ALRIGHT NERD ITS TIME FOR HARD MODE HA THERES NO WAY OF CHANGING THE DIFFICULTEEEEE THERES CAPITALS IN THIS ONE"
    
    buritos = ''
    dubs = 25
    while dubs > 0:         
        chicken = 0                 
        for char in wordy:   
            if char in buritos:    
                print char,    
    
            else:
                print "_",     
                chicken += 1    
        if chicken == 0:        
            print "You won"  
            break           
    
    
        noodles = raw_input("guess a character:") 
        buritos += noodles                    
        if noodles not in wordy:  
            dubs -= 1        
            print "Wrong big question mark, this program is not designed to assume your gender"    
            print "You have", + dubs, 'more buritos' 
            if dubs == 0:  
                print "YOU SUCK WHY CANT YOU UNDERSTAND WHAT THIS IS YOU CHIMPANZ" + wordy
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            