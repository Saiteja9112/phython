import random

t = ["rock", "paper", "scissor"]
us=0
cs=0

computer = t[random.randint(0,2)]

player = False

while player == False:
    player = input("rock, paper, scissor : ")
    if player == "quit":
        print("User Score is ",us)
        print("Computer Score is ",cs)
        if us == cs:
            print("Tie!")
        elif us > cs:
            print("You win the game!,congratulations")
        else:
            print("You loose the game!,Better luck next time")
        exit()
    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print(computer, "covers", player)
            cs=cs+1
            print("cs=",cs)
        else:
            print(player, "smashes", computer)
            us=us+1
            print("us=",us)
    elif player == "paper":
        if computer == "scissor":
            print(computer, "cut", player)
            cs=cs+1
            print("cs=",cs)
        else:
            print(player, "covers", computer)
            us=us+1
            print("us=",us)
    elif player == "scissor":
        if computer == "rock":
            print(computer, "smashes", player)
            cs=cs+1
            print("cs=",cs)
        else:
            print( player, "cut", computer)
            us=us+1
            print("us=",us)
    else:
        print("That's not a valid play. Check your spelling!")
    player = False
    computer = t[random.randint(0,2)]