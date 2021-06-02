#Make a two-player Rock-Paper-Scissors game. 
def rps():
    while True:
        player1 = input("Please enter a number of your choice (1: rock , 2: paper, 3: scissor):  ")
        player2 = input("Please make a number of your choice (1: rock , 2: paper, 3: scissor): ")
        
        player1 = int(player1)
        player2 = int(player2)
       
        if player1 == 1 : 
            if player2 == 2:
                print("Player2 wins")
                return False
            elif player2 == 3:
                print("Player1 wins")
                return False
            else:
                print("Draw, go again")
        elif player1 == 2 : 
            if player2 == 3:
                print("Player2 wins")
                return False
            elif player2 == 1:
                print("Player1 wins")
                return False
            else:
                print("Draw, go again")
        elif player1 == 3 : 
            if player2 == 1:
                print("Player2 wins")
                return False
            elif player2 == 2:
                print("Player1 wins")
                return False
            else:
                print("Draw, go again")
        elif  player2 not in (1, 2, 3):
            print("Invalid input, try again")
        else:
            print("Invalid input, try again")

    return False

rps()