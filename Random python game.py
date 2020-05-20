import random

player1 = 0
player2 = 0
player1_current=0
player2_current=0
player1_turn = True
while player1 < 100 and player2 < 100:
    while player1_turn == True and player1+player1_current<100:
        choice = input("Player 1: to roll or not to roll(Y for yes, N for no)?")
        if choice is "Y":
            number = random.randint(1,6)
            print("you rolled: ", number)
            if number != 1:
                player1_current += number
            else:
                player1_current=0
                print ("turn over")
                print ("score: ", player1)
                player1_turn = False
        else:
            player1 += player1_current
            player1_turn = False
            player1_current = 0
            print("score: ", player1)
    if player1 + player1_current >= 100:
        print ("Player 1 wins!")
        print ("score: ")
        print ("Player 1: ", player1 + player1_current)
        print ("Player 2: ", player2)
        player1 += player1_current    

    while player1_turn == False and player2 + player2_current < 100:
        choice = input("Player 2: to roll or not to roll(Y for yes, N for no)?")
        if choice is "Y":
            number = random.randint(1,6)
            print("you rolled: ", number)
            if number != 1:
                player2_current += number
            else:
                player2_current=0
                print ("turn over")
                print ("score: ", player2)
                player1_turn = True
        else:
            player2 += player2_current
            player1_turn = True
            player2_current = 0
            print("score: ", player2)
    if player2 + player2_current >= 100:
        print ("Player 2 wins!")
        print ("score: ")
        print ("Player 1: ", player1)
        print ("Player 2: ", player2 + player2_current)
        player2 += player2_current   
