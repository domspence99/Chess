import random
from chess_functions import *

def main():
    #SET GAME VARIABLES
    endgame = False #Initiate false condition for continual game loop
    
    #GET NAMES
    p1,p2 = get_player_info() #Gets p1 and p2 names
    
    #INSTANTIATE PLAYER OBJECTS
    player1 = Player(p1) #Creates player 1 and 2 objects
    player2 = Player(p2)

    #SET STARTING PLAYER & PIECE COLOURS
    starter = Player.choose_p1(player1,player2) #Select b/w & choose who plays first
    #print(player1.name,player1.colour,player2.name,player2.colour)
    current_player = starter #Sets current player(obj) to play first
    
    #SET STARTING BOARD
    set_starting_board() #Initate starting board positions
    
    #GAME LOOP
    while (endgame == False):
        print("Current player is: " + current_player.name + "\n") #Print current player
        board_print() #Print current state of board
        new_move = get_move() #Returns valid player input as "Pa7a5"
        if (Board.selectPiece(new_move,current_player) == False): #Passes move & player obj to select piece
            print("Please enter a valid move \n")
            pass
        else:
            #Board.move_pawn(current_player,new_move)
            current_player = setPlayer(current_player,player1,player2)







main()
