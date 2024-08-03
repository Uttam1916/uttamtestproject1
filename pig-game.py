import random

def roll():
    minval=1
    maxval=6
    roll=random.randint(minval,maxval)
    return roll
while True:
    players=input("Enter the no of players(1-4): ")
    if players.isdigit():
        players=int(players)
        if 2<=players<=4:
            break
        else:
            print("Enter players between (2-4)")
    else:
        print("Invalid try again")
maxs=50
playersc=[0 for _ in range(players)]
while max(playersc)<maxs:

    for playdx in range(players):
        print("\nPlayer",playdx+1,"turn has just started\n")
        print("your total score is:",playersc[playdx])
        current_score =0

        while True:

           askroll=input("Would you like to roll?(y/n): ")
           if askroll.lower() != "y":
               break
           value=roll()
           if value==1: 
            
               print("You rolled 1 turn done")
               current_score
               break
           else:
               current_score += value 
               print("you rolled a:",value)

           print("your score is:",current_score)
        playersc[playdx]+=current_score
        print("Your total score is",playersc[playdx])  
        
max(playersc)>=maxs
win=playersc.index(maxs)
print("player number",win+1,"is a winner with a score of",maxs)