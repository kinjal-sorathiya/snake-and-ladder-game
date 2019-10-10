import random

pos = 0
cnt = 0

while(pos<100):
    dice = random.randrange(1,7)

    
    if((pos + dice) <= 100):
        pos = pos + dice
        if((dice == 6) and (dice + pos) <= 100):
            print(" Extra Chance ")
            pos = pos + dice 
    else:
        pos = pos


    if(pos == 3):
        print(" Ladder from 3 to 45")
        pos = 45

    if(pos == 32):
        print(" Ladder from 32 to 88")
        pos == 88

    if(pos == 54):
        print(" Snake from 54 to 8")
        pos = 8

    if(pos == 92):
        print(" Snake from 92 to 27")
        pos = 27
    
    
    if((pos == 95) and (dice > 5)):
        continue
    elif((pos == 96) and (dice > 4)):
        continue
    elif((pos == 97) and (dice > 3)):
        continue
    elif((pos == 98) and (dice > 2)):
        continue
    elif((pos == 99) and (dice > 1)):
        continue

    cnt = cnt + 1

    print(cnt , "========> ",dice, "======> ", pos )


    
    
   



