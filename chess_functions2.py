#Gets player names
import random


def get_player_info():
    p1 = input("Enter first players name: ")    
    p2 = input("Enter second players name: ")
    print("\n")
    return p1,p2

#Class for each player including name & team
class Player():
    def __init__(self, name, colour="blank"):
        self.name = name
        self.colour = colour
    def choose_p1(player1,player2):
        num = random.randint(0,1)
        if (num == 0):
            player1.colour ='w'
            player2.colour = 'b'
            print(player1.name, "will play as white \n")
            return player1
        else:
            player1.colour = 'b'
            player2.colour = 'w'
            print(player2.name, "will play as white \n")
            return player2

#Class for pieces
class Pieces:
    def __init__(self, type, team, char):
        self.type = type
        self.team = team
        self.char = char
bp = Pieces('pawn','b','P')
wp = Pieces('pawn','w','p')
bc = Pieces('castle','b','C')
wc = Pieces('castle','w','c')
bh = Pieces('horse','b','H')
wh = Pieces('horse','w','h')
bb = Pieces('bishop','b','B')
wb = Pieces('bishop','w','b')
bq = Pieces('queen','b','Q')
wq = Pieces('queen','w','q')
bk = Pieces('king','b','K')
wk = Pieces('king','w','k')
np = Pieces('none','0',' ')

class Board():
    pieces = ["P","C","H","B","Q","K"]
    board = [[' ' for i in range(8)] for i in range(8)]    #for x in range(0,len(pieces)):
    
    def move_pawn(player, matrix_move, board_move):
        valid_pawn_move = False #Initialises valid move return type to false
        piece = board_move[0]
        og_row = matrix_move[0] 
        og_column = matrix_move[1]
        new_row = matrix_move[2]
        new_column = matrix_move[3]
        current_game_colour = player.colour
        original_position = Board.board[matrix_move[0]][matrix_move[1]]
        new_position = Board.board[matrix_move[2]][matrix_move[3]]
        
        #print("Game colour: ",current_game_colour)
        #print("OG position ",original_position.char,original_position.team)
        #print("New position: ",new_position.char, original_position.team)
        #print("current matrix move is: ",matrix_move)
        
        #SETTING VERTICAL AND HORIZONTAL DISTANCES REQUESTED BY MOVE
        vertical_distance_travelled = abs(og_row - new_row)
        horizontal_distance_travelled = abs(og_column - new_column)
        #print("Vertical distance: ", vertical_distance_travelled)
        #print("Horizontal distance: ", horizontal_distance_travelled)

        
        #3. CHECK RULES OF PAWN MOVE
        #3.1 PAWNS CAN ONLY MOVE A MAXIMUM OF 2 SQUARES
        if (vertical_distance_travelled > 2): #Checks for max of 2 vertical places
            print("ERROR: Pawns can only move a maximum of 2 vertical places")
        elif(horizontal_distance_travelled > 1): #Ensures pawns can only move 1 square horizontally (in the case of diagonal kill)
            print("ERROR: Pawns can only move a maximum of 1 square")
        #3.2 PAWNS CAN ONLY MOVE FORWARD
        elif(player.colour == 'w' and new_row > og_row): #Checks that white pawns are only moving forwards
             print("ERROR: Pawns can only move forward")
        elif(player.colour == 'b' and new_row < og_row): #Checks that black pawns are only moving forwards
             print("ERROR: Pawns can only move forward")
        #3.3 PAWNS CAN ONLY MOVE 1 SQUARE FORWARDS FROM ANYWHERE ELSE ON BOARD
        elif((og_row != 6 and player.colour == 'w') and vertical_distance_travelled > 1): #Checks that white can only move 1 square from anywhere on board except starting row 7
             print("ERROR: Pawn can only move 1 square")
        elif((og_row != 1 and player.colour == 'b') and vertical_distance_travelled > 1): #Checks that black can only move 1 square from anywhere on board except starting row 2
            print("ERROR: Pawn can only move 1 square")
        #3.3 PAWNS CAN ONLY MOVE VERTICALLY UNLESS TAKING A PIECE
        elif(horizontal_distance_travelled == 1 and vertical_distance_travelled != 1):
            print("ERROR: Can only move diagonally by 1 square")
        #3.4 PAWNS CAN ONLY MOVE DIAGONALLY IF TAKING AN OPPONENTS PIECE 
        elif (horizontal_distance_travelled == 1 and Board.board[new_row][new_column] == np or Board.board[new_row][new_column].team == current_game_colour):
            print("ERROR: Can't move pawn diagonally when not taking an opponents piece")
        #3.5 PAWNS ON STARTING ROWS CANNOT JUMP OVER OPPONENTS PIECES WHEN MOVING 2 SQUARES
        elif (og_row == 6 and player.colour == 'w' and Board.board[new_row+1][new_column] != np and vertical_distance_travelled > 1):
             print("ERROR: Pawn can't jump over an opponents piece")
        elif (og_row == 1 and player.colour == 'b' and Board.board[new_row-1][new_column] != np and vertical_distance_travelled > 1):
             print("ERROR: Pawn can't jump over an opponents piece")
        #3.6 PAWNS CAN ONLY MOVE VERTICALLY ONTO AN EMPTY SQUARE
        elif(Board.board[new_row][new_column] != np and horizontal_distance_travelled == 0):
             print("ERROR: Pawns cannot take a piece vertically")
        else:
            #VALID MOVE BY PAWN
            print("MOVE: Moved " + player.colour + " pawn from " + board_move[1] + board_move[2] + " to " + board_move[3] + board_move[4] + "\n")
            
            #CHANGE ORIGINAL PAWN POSITION TO EMPTY
            #print("OG position char before move: ",Board.board[move[0]][move[1]].char) #Prints piece at og location
            Board.board[og_row][og_column] = np #Sets original position blank(moved piece)
            #print("OG position char after move: ",original_position.char)
            
            #print("Piece already at proposed new location",Board.board[new_row][new_column].char,Board.board[new_row][new_column].type,Board.board[new_row][new_column].team)
            if(Board.board[new_row][new_column] != np):
                print("CAPTURE!: " + player.name + " takes " + Board.board[new_row][new_column].team + " " + Board.board[new_row][new_column].type + " at " + board_move[3] + board_move[4] + " with pawn\n" )
            #CHANGE NEW PAWN (obj) POSITION TO NEW LOCATION
            Board.board[new_row][new_column] = getPieceObject(player,piece)
            #print("New position char after move: ",new_position.char)
            
            ## ADD En passaunt
            valid_pawn_move = True
        
        return valid_pawn_move
            
    def move_castle(player, matrix_move, board_move):
        valid_castle_move = False #Initialises valid move return type to false
        piece = board_move[0]
        og_row = matrix_move[0] 
        og_column = matrix_move[1]
        new_row = matrix_move[2]
        new_column = matrix_move[3]
        current_game_colour = player.colour

        #SETTING VERTICAL AND HORIZONTAL DISTANCES REQUESTED BY MOVE
        vertical_distance_travelled = abs(og_row - new_row)
        horizontal_distance_travelled = abs(og_column - new_column)
        
        #ENSURES CASTLE CAN ONLY MOVE HORIZONTALLY/VERTICALLY ONLY
        if (matrix_move[0] != matrix_move[2] and matrix_move[1] != matrix_move[3] or matrix_move[0] != matrix_move[2] and matrix_move[1] != matrix_move[3]):
            print("ERROR: Castle can only move in the same vertical or horizontal path")
            valid_castle_move = False
            return valid_castle_move
        
        #CHECK IF CASTLE CAN MOVE UP THE BOARD(i.e if any pieces are blocking, then return error)
        #If castle moving up the board
        if (og_row > new_row):
            for x in range(1,vertical_distance_travelled+1):
                #print("current row: " ,og_row-x) 
                #print("Pieces in upward path are: ",Board.board[og_row - x][og_column].char)
                if (Board.board[og_row-x][og_column] != np): #If there is a piece in the path
                    #print(Board.board[og_row-x][og_column].char) #Print piece in the way
                    blocked_piece_coord = convert2_to_ascii([og_row-x,og_column]) #Obtain coordinates of piece in the way of path
                    #IF PIECE BLOCKED BY YOUR OWN PIECE
                    if (Board.board[og_row-x][og_column].team == player.colour): #If the piece you are trying to move over is your own piece
                        print("ERROR: Castle can't jump over your own piece (" + Board.board[og_row-x][og_column].type + ") at " + blocked_piece_coord[0] + blocked_piece_coord[1])
                        valid_castle_move = False
                        return valid_castle_move                        
                    #IF PIECE BLOCKED BY OPPONENTS PIECE
                    elif(Board.board[og_row-x][og_column].team != player.colour):
                         #print("X: " + str(x) + " vdt: " + str(vertical_distance_travelled))
                         if(x != vertical_distance_travelled): #If trying to move the castle past the opponent piece (if the move ends at the castle at opponent piece, you can take)
                            print("ERROR: Castle can't jump over an opponents piece (" + Board.board[og_row-x][og_column].type + ") at " + blocked_piece_coord[0] + blocked_piece_coord[1])
                            valid_castle_move = False
                            return valid_castle_move 
                
        #CHECK IF CASTLE CAN MOVE DOWN THE BOARD (WITHOUT BEING BLOCKED BY ANY PIECES)
        if (new_row > og_row): #Moving down the board
            for x in range(1,vertical_distance_travelled+1):
                if (Board.board[og_row+x][og_column] != np): #If there is a piece in the path
                    blocked_piece_coord = convert2_to_ascii([og_row+x,og_column]) #Obtain coordinates of piece in the way of path
                    #IF PIECE BLOCKED BY YOUR OWN PIECE
                    if (Board.board[og_row+x][og_column].team == player.colour): #If the piece you are trying to move over is your own piece
                        print("ERROR: Castle can't jump over your own piece (" + Board.board[og_row+x][og_column].type + ") at " + blocked_piece_coord[0] + blocked_piece_coord[1])
                        valid_castle_move = False
                        return valid_castle_move                        
                    #IF PIECE BLOCKED BY OPPONENTS PIECE
                    elif(Board.board[og_row+x][og_column].team != player.colour):
                         if(x != vertical_distance_travelled): #If trying to move the castle past the opponent piece (if the move ends at the castle at opponent piece, you can take)
                            print("ERROR: Castle can't jump over an opponents piece (" + Board.board[og_row+x][og_column].type + ") at " + blocked_piece_coord[0] + blocked_piece_coord[1])
                            valid_castle_move = False
                            return valid_castle_move
        
        #CHECK IF CASTLE CAN MOVE RIGHT ON THE BOARD (WITHOUT BEING BLOCKED BY ANY PIECES)
        if (new_column > og_column): #Moving right on the board
            for y in range(1,horizontal_distance_travelled+1):
                if (Board.board[og_row][og_column + y] != np): #If there is a piece in the path
                    blocked_piece_coord = convert2_to_ascii([og_row,og_column + y]) #Obtain coordinates of piece in the way of path
                    #IF PIECE BLOCKED BY YOUR OWN PIECE
                    if (Board.board[og_row][og_column + y].team == player.colour): #If the piece you are trying to move over is your own piece
                        print("ERROR: Castle can't jump over your own piece (" + Board.board[og_row][og_column + y].type + ") at " + blocked_piece_coord[0] + blocked_piece_coord[1])
                        valid_castle_move = False
                        return valid_castle_move                        
                    #IF PIECE BLOCKED BY OPPONENTS PIECE
                    elif(Board.board[og_row][og_column + y].team != player.colour):
                         if(y != horizontal_distance_travelled): #If trying to move the castle past the opponent piece (if the move ends at the castle at opponent piece, you can take)
                            print("ERROR: Castle can't jump over an opponents piece (" + Board.board[og_row][og_column + y].type + ") at " + blocked_piece_coord[0] + blocked_piece_coord[1])
                            valid_castle_move = False
                            return valid_castle_move  
                         
        #CHECK IF CASTLE CAN MOVE LEFT ON THE BOARD (WITHOUT BEING BLOCKED BY ANY PIECES)
        if (og_column > new_column): #Moving down the board
            for y in range(1,horizontal_distance_travelled+1):
                if (Board.board[og_row][og_column - y] != np): #If there is a piece in the path
                    blocked_piece_coord = convert2_to_ascii([og_row,og_column - y]) #Obtain coordinates of piece in the way of path
                    #IF PIECE BLOCKED BY YOUR OWN PIECE
                    if (Board.board[og_row][og_column - y].team == player.colour): #If the piece you are trying to move over is your own piece
                        print("ERROR: Castle can't jump over your own piece (" + Board.board[og_row][og_column - y].type + ") at " + blocked_piece_coord[0] + blocked_piece_coord[1])
                        valid_castle_move = False
                        return valid_castle_move                        
                    #IF PIECE BLOCKED BY OPPONENTS PIECE
                    elif(Board.board[og_row][og_column - y].team != player.colour):
                         if(y != horizontal_distance_travelled): #If trying to move the castle past the opponent piece (if the move ends at the castle at opponent piece, you can take)
                            print("ERROR: Castle can't jump over an opponents piece (" + Board.board[og_row][og_column - y].type + ") at " + blocked_piece_coord[0] + blocked_piece_coord[1])
                            valid_castle_move = False
                            return valid_castle_move
        #IF NO PIECE IN ANY PATH (VALID CASTLE MOVE)
        print("MOVE: Moved " + player.colour + " castle from " + board_move[1] + board_move[2] + " to " + board_move[3] + board_move[4] + "\n") #Print move validation message
        #IF A PIECE IS TAKEN (PRINT CAPTURE MESSAGE)
        if(Board.board[new_row][new_column] != np):
                print("CAPTURE!: " + player.name + " takes " + Board.board[new_row][new_column].team + " " + Board.board[new_row][new_column].type + " at " + board_move[3] + board_move[4] + " with castle \n" )
            
        #SET NEW BOARD PIECE LOCATIONS
        Board.board[og_row][og_column] = np #Sets original position blank(moved piece)
        Board.board[new_row][new_column] = getPieceObject(player,piece)
        valid_castle_move = True
        return valid_castle_move
                         
    def move_horse(player, matrix_move, board_move):
        valid_horse_move = False #Initialises valid move return type to false
        piece = board_move[0]
        og_row = matrix_move[0] 
        og_column = matrix_move[1]
        new_row = matrix_move[2]
        new_column = matrix_move[3]
        current_game_colour = player.colour


        #SETTING VERTICAL AND HORIZONTAL DISTANCES REQUESTED BY MOVE
        vertical_distance_travelled = abs(og_row - new_row)
        horizontal_distance_travelled = abs(og_column - new_column)

        #HORSE CAN ONLY MOVE IN AN L SHAPE
        if(vertical_distance_travelled > 2):
            print("Knights can only move a maximum vertical distance of 2 squares")
            return valid_horse_move            
        elif(horizontal_distance_travelled > 2):
            print("Knights can only move a maximum horizontal distance of 2 squares")
            return valid_horse_move            
        elif(vertical_distance_travelled == 2):
            if(horizontal_distance_travelled != 1):
                print("Kights can move two squares in any direction vertically followed by one square horizontally, or two squares in any direction horizontally followed by one square vertically.")
                return valid_horse_move            
        elif(vertical_distance_travelled == 1):
            if(horizontal_distance_travelled != 2):
                print("Kights can move two squares in any direction vertically followed by one square horizontally, or two squares in any direction horizontally followed by one square vertically.")
                return valid_horse_move            
        elif(horizontal_distance_travelled == 2):
            if(vertical_distance_travelled != 1):
                print("Kights can move two squares in any direction vertically followed by one square horizontally, or two squares in any direction horizontally followed by one square vertically.")
                return valid_horse_move            
        elif(horizontal_distance_travelled == 1):
            if(vertical_distance_travelled != 2):
                print("Kights can move two squares in any direction vertically followed by one square horizontally, or two squares in any direction horizontally followed by one square vertically.")
                return valid_horse_move           
        
        #CANT LAND ON OWN PIECE
        if (Board.board[new_row][new_column] != np and Board.board[new_row][new_column].team == current_game_colour): #If end square of move is your own piece
                print("ERROR: Square " + convert2_to_ascii([new_row,new_column])[0] + convert2_to_ascii([new_row,new_column])[1] + " is occupied by your " + current_game_colour + " " + Board.board[new_row][new_column].type)
                return valid_horse_move

        #IF VALID KNIGHT MOVE
        print("MOVE: Moved " + player.colour + " knight from " + board_move[1] + board_move[2] + " to " + board_move[3] + board_move[4] + "\n") #Print move validation message
        #IF A PIECE IS TAKEN (PRINT CAPTURE MESSAGE)
        if(Board.board[new_row][new_column] != np and Board.board[new_row][new_column].team != current_game_colour): #If end square of move is an opponents piece
                print("CAPTURE!: " + player.name + " takes " + Board.board[new_row][new_column].team + " " + Board.board[new_row][new_column].type + " at " + board_move[3] + board_move[4] + " with knight\n" )
            
        #SET NEW BOARD PIECE LOCATIONS
        Board.board[og_row][og_column] = np #Sets original position blank(moved piece)
        Board.board[new_row][new_column] = getPieceObject(player,piece)
        valid_horse_move = True
        return valid_horse_move    
    def move_bishop(player, matrix_move, board_move):
        valid_bishop_move = False #Initialises valid move return type to false
        piece = board_move[0]
        og_row = matrix_move[0] 
        og_column = matrix_move[1]
        new_row = matrix_move[2]
        new_column = matrix_move[3]
        current_game_colour = player.colour

        #SETTING VERTICAL AND HORIZONTAL DISTANCES REQUESTED BY MOVE
        vertical_distance_travelled = abs(og_row - new_row)
        horizontal_distance_travelled = abs(og_column - new_column)
        
        #BISHOP CAN ONLY MOVE ON A DIAGONAL
        if (vertical_distance_travelled != horizontal_distance_travelled):
            print("ERROR: Bishops can only move on diagonal squares")
            return valid_bishop_move
        else:
            diagonal_distance_travelled = horizontal_distance_travelled #Setting the diagonal distance travelled
        
        #BISHOP CAN'T JUMP OVER ANY PIECES

        #MOVING UP AND RIGHT ON THE BOARD
        if (og_row > new_row and new_column > og_column):
            for x in range(1,diagonal_distance_travelled+1): #For squares in diagonal path
                #print("Pieces in diagonal path are: ",Board.board[og_row - x][og_column + x].char)
                if (Board.board[og_row - x][og_column + x] != np): #If there is a piece in the path
                    #print(Board.board[og_row-x][og_column + x].char) #Print piece in the way
                    blocked_piece_coord = convert2_to_ascii([og_row - x, og_column + x]) #Obtain coordinates of piece in the way of path
                    #IF PIECE BLOCKED BY YOUR OWN PIECE
                    if (Board.board[og_row-x][og_column + x].team == player.colour): #If the piece you are trying to move over is your own piece
                        if(x == vertical_distance_travelled): #If final square is your own piece
                            print("ERROR: Square " + blocked_piece_coord[0] + blocked_piece_coord[1] + " is occupied by your own " + Board.board[og_row - x][og_column + x].type)
                            return valid_bishop_move
                        else: #If final square is not own piece/empty
                            print("ERROR: Bishop can't jump over your own piece (" + Board.board[og_row - x][og_column + x].type + ") at " + blocked_piece_coord[0] + blocked_piece_coord[1])
                            return valid_bishop_move                        
                    #IF PIECE BLOCKED BY OPPONENTS PIECE
                    elif(Board.board[og_row - x][og_column + x].team != player.colour):
                        if(x != diagonal_distance_travelled): #If trying to move the bisop past the opponent piece (if the move ends at the bishop at opponent piece, you can take)
                            print("ERROR: Bishop can't jump over an opponents piece (" + Board.board[og_row - x][og_column + x].type + ") at " + blocked_piece_coord[0] + blocked_piece_coord[1])
                            return valid_bishop_move 
        
        #MOVING UP AND LEFT ON THE BOARD
        if (og_row > new_row and og_column > new_column):
            for x in range(1,diagonal_distance_travelled+1): #For squares in diagonal path
                #print("Pieces in diagonal path are: ",Board.board[og_row - x][og_column + x].char)
                if (Board.board[og_row - x][og_column - x] != np): #If there is a piece in the path
                    blocked_piece_coord = convert2_to_ascii([og_row - x, og_column - x]) #Obtain coordinates of piece in the way of path
                    #IF PIECE BLOCKED BY YOUR OWN PIECE
                    if (Board.board[og_row-x][og_column - x].team == player.colour): #If the piece you are trying to move over is your own piece
                        if(x == vertical_distance_travelled): #If final square is your own piece
                            print("ERROR: Square " + blocked_piece_coord[0] + blocked_piece_coord[1] + " is occupied by your own " + Board.board[og_row - x][og_column - x].type)
                            return valid_bishop_move
                        else: #If final square is not own piece/empty
                            print("ERROR: Bishop can't jump over your own piece (" + Board.board[og_row - x][og_column - x].type + ") at " + blocked_piece_coord[0] + blocked_piece_coord[1])
                            return valid_bishop_move                        
                    #IF PIECE BLOCKED BY OPPONENTS PIECE
                    elif(Board.board[og_row - x][og_column - x].team != player.colour):
                        if(x != diagonal_distance_travelled): #If trying to move the bisop past the opponent piece (if the move ends at the bishop at opponent piece, you can take)
                            print("ERROR: Bishop can't jump over an opponents piece (" + Board.board[og_row - x][og_column - x].type + ") at " + blocked_piece_coord[0] + blocked_piece_coord[1])
                            return valid_bishop_move

        #MOVING DOWN AND LEFT ON THE BOARD
        if (new_row > og_row and og_column > new_column):
            for x in range(1,diagonal_distance_travelled+1): #For squares in diagonal path
                #print("Pieces in diagonal path are: ",Board.board[og_row - x][og_column + x].char)
                if (Board.board[og_row + x][og_column - x] != np): #If there is a piece in the path
                    blocked_piece_coord = convert2_to_ascii([og_row + x, og_column - x]) #Obtain coordinates of piece in the way of path
                    #IF PIECE BLOCKED BY YOUR OWN PIECE
                    if (Board.board[og_row + x][og_column - x].team == player.colour): #If the piece you are trying to move over is your own piece
                        if(x == vertical_distance_travelled): #If final square is your own piece
                            print("ERROR: Square " + blocked_piece_coord[0] + blocked_piece_coord[1] + " is occupied by your own " + Board.board[og_row + x][og_column - x].type)
                            return valid_bishop_move
                        else: #If final square is not own piece/empty
                            print("ERROR: Bishop can't jump over your own piece (" + Board.board[og_row + x][og_column - x].type + ") at " + blocked_piece_coord[0] + blocked_piece_coord[1])
                            return valid_bishop_move                        
                    #IF PIECE BLOCKED BY OPPONENTS PIECE
                    elif(Board.board[og_row + x][og_column - x].team != player.colour):
                        if(x != diagonal_distance_travelled): #If trying to move the bisop past the opponent piece (if the move ends at the bishop at opponent piece, you can take)
                            print("ERROR: Bishop can't jump over an opponents piece (" + Board.board[og_row + x][og_column - x].type + ") at " + blocked_piece_coord[0] + blocked_piece_coord[1])
                            return valid_bishop_move         
        
        #MOVING DOWN AND RIGHT ON THE BOARD
        if (new_row > og_row and new_column > og_column):
            for x in range(1,diagonal_distance_travelled+1): #For squares in diagonal path
                #print("Pieces in diagonal path are: ",Board.board[og_row - x][og_column + x].char)
                if (Board.board[og_row + x][og_column + x] != np): #If there is a piece in the path
                    blocked_piece_coord = convert2_to_ascii([og_row + x, og_column + x]) #Obtain coordinates of piece in the way of path
                    #IF PIECE BLOCKED BY YOUR OWN PIECE
                    if (Board.board[og_row + x][og_column + x].team == player.colour): #If the piece you are trying to move over is your own piece
                        if(x == vertical_distance_travelled): #If final square is your own piece
                            print("ERROR: Square " + blocked_piece_coord[0] + blocked_piece_coord[1] + " is occupied by your own " + Board.board[og_row + x][og_column + x].type)
                            return valid_bishop_move
                        else: #If final square is not own piece/empty
                            print("ERROR: Bishop can't jump over your own piece (" + Board.board[og_row + x][og_column + x].type + ") at " + blocked_piece_coord[0] + blocked_piece_coord[1])
                            return valid_bishop_move                        
                    #IF PIECE BLOCKED BY OPPONENTS PIECE
                    elif(Board.board[og_row + x][og_column + x].team != player.colour):
                        if(x != diagonal_distance_travelled): #If trying to move the bisop past the opponent piece (if the move ends at the bishop at opponent piece, you can take)
                            print("ERROR: Bishop can't jump over an opponents piece (" + Board.board[og_row + x][og_column + x].type + ") at " + blocked_piece_coord[0] + blocked_piece_coord[1])
                            return valid_bishop_move   

        #IF NO PIECE IN ANY PATH (VALID BISHOP MOVE)
        print("MOVE: Moved " + player.colour + " bishop from " + board_move[1] + board_move[2] + " to " + board_move[3] + board_move[4] + "\n") #Print move validation message
        #IF A PIECE IS TAKEN (PRINT CAPTURE MESSAGE)
        if(Board.board[new_row][new_column] != np):
                print("CAPTURE!: " + player.name + " takes " + Board.board[new_row][new_column].team + " " + Board.board[new_row][new_column].type + " at " + board_move[3] + board_move[4] + " with bishop \n" )
            
        #SET NEW BOARD PIECE LOCATIONS
        Board.board[og_row][og_column] = np #Sets original position blank(moved piece)
        Board.board[new_row][new_column] = getPieceObject(player,piece)
        valid_bishop_move = True
        return valid_bishop_move
    
    def move_king(player, matrix_move, board_move):
        valid_king_move = False #Initialises valid move return type to false
        piece = board_move[0]
        og_row = matrix_move[0] 
        og_column = matrix_move[1]
        new_row = matrix_move[2]
        new_column = matrix_move[3]
        current_game_colour = player.colour

        #SETTING VERTICAL AND HORIZONTAL DISTANCES REQUESTED BY MOVE
        vertical_distance_travelled = abs(og_row - new_row)
        horizontal_distance_travelled = abs(og_column - new_column)

        #RULES FOR KING MOVE
        #Can't land on own piece
        #KING CAN ONLY MOVE 1 SQUARE
        if(vertical_distance_travelled > 1 or horizontal_distance_travelled > 1):
            print("ERROR: King can only move 1 square in any direction")
            return valid_king_move

        #KING CANT LAND ON OWN PIECE
        if (Board.board[new_row][new_column] != np and Board.board[new_row][new_column].team == current_game_colour): #If end square of move is your own piece
                print("ERROR: Square " + convert2_to_ascii([new_row,new_column])[0] + convert2_to_ascii([new_row,new_column])[1] + " is occupied by your " + current_game_colour + " " + Board.board[new_row][new_column].type)
                return valid_king_move
        
        #IF VALID KING MOVE
        print("MOVE: Moved " + player.colour + " king from " + board_move[1] + board_move[2] + " to " + board_move[3] + board_move[4] + "\n") #Print move validation message
        #IF A PIECE IS TAKEN (PRINT CAPTURE MESSAGE)
        if(Board.board[new_row][new_column] != np and Board.board[new_row][new_column].team != current_game_colour): #If end square of move is an opponents piece
                print("CAPTURE!: " + player.name + " takes " + Board.board[new_row][new_column].team + " " + Board.board[new_row][new_column].type + " at " + board_move[3] + board_move[4] + " with the king" "\n" )
            
        #SET NEW BOARD PIECE LOCATIONS
        Board.board[og_row][og_column] = np #Sets original position blank(moved piece)
        Board.board[new_row][new_column] = getPieceObject(player,piece)
        valid_king_move = True
        return valid_king_move    
    
    def move_queen(player, matrix_move, board_move):
        #QUEEN RULES
        #CAN MOVE FORWARDS/BACKWARDS ANY SPACES
        #CAN MOVE SIDEWAYS ANY SPACES
        #CAN MOVE DIAGONALLY ANY SPACES

        #MOVING UP THE BOARD
    
        valid_queen_move = False #Initialises valid move return type to false
        piece = board_move[0]
        og_row = matrix_move[0] 
        og_column = matrix_move[1]
        new_row = matrix_move[2]
        new_column = matrix_move[3]
        current_game_colour = player.colour

        #SETTING VERTICAL AND HORIZONTAL DISTANCES REQUESTED BY MOVE
        vertical_distance_travelled = abs(og_row - new_row)
        horizontal_distance_travelled = abs(og_column - new_column)
        

        #ENSURES QUEEN CAN ONLY MOVE HORIZONTALLY/VERTICALLY/DIAGONAL PATH ONLY
        if (matrix_move[0] != matrix_move[2] and matrix_move[1] != matrix_move[3] or matrix_move[0] != matrix_move[2] and matrix_move[1] != matrix_move[3]):
            if(vertical_distance_travelled != horizontal_distance_travelled):
                print("ERROR: Queen can only move in vertical, horizontal or diagonal paths")
                return valid_queen_move
        
        #DIAGONAL MOVEMENT#

        #IF QUEEN MOVING DIAGONALLY UP AND RIGHT ON THE BOARD
        if (og_row > new_row and new_column > og_column):
            for x in range(1,vertical_distance_travelled+1): #For squares in diagonal path
                #print("Pieces in diagonal path are: ",Board.board[og_row - x][og_column + x].char)
                if (Board.board[og_row - x][og_column + x] != np): #If there is a piece in the path
                    #print(Board.board[og_row-x][og_column + x].char) #Print piece in the way
                    blocked_piece_coord = convert2_to_ascii([og_row - x, og_column + x]) #Obtain coordinates of piece in the way of path
                    #IF PIECE BLOCKED BY YOUR OWN PIECE
                    if (Board.board[og_row-x][og_column + x].team == player.colour): #If the piece you are trying to move over is your own piece
                        if(x == vertical_distance_travelled): #If final square is your own piece
                            print("ERROR: Square " + blocked_piece_coord[0] + blocked_piece_coord[1] + " is occupied by your own " + Board.board[og_row - x][og_column + x].type)
                            return valid_queen_move
                        else: #If final square is not own piece/empty
                            print("ERROR: Queen can't jump over your own piece (" + Board.board[og_row - x][og_column + x].type + ") at " + blocked_piece_coord[0] + blocked_piece_coord[1])
                            return valid_queen_move                        
                    #IF PIECE BLOCKED BY OPPONENTS PIECE
                    elif(Board.board[og_row - x][og_column + x].team != player.colour):
                        if(x != vertical_distance_travelled): #If trying to move the bisop past the opponent piece (if the move ends at the bishop at opponent piece, you can take)
                            print("ERROR: Queen can't jump over an opponents piece (" + Board.board[og_row - x][og_column + x].type + ") at " + blocked_piece_coord[0] + blocked_piece_coord[1])
                            return valid_queen_move 
        
        #QUEEN MOVING DIAGONALLY UP AND LEFT ON THE BOARD
        if (og_row > new_row and og_column > new_column):
            for x in range(1,vertical_distance_travelled+1): #For squares in diagonal path
                #print("Pieces in diagonal path are: ",Board.board[og_row - x][og_column + x].char)
                if (Board.board[og_row - x][og_column - x] != np): #If there is a piece in the path
                    blocked_piece_coord = convert2_to_ascii([og_row - x, og_column - x]) #Obtain coordinates of piece in the way of path
                    #IF PIECE BLOCKED BY YOUR OWN PIECE
                    if (Board.board[og_row-x][og_column - x].team == player.colour): #If the piece you are trying to move over is your own piece
                        if(x == vertical_distance_travelled): #If final square is your own piece
                            print("ERROR: Square " + blocked_piece_coord[0] + blocked_piece_coord[1] + " is occupied by your own " + Board.board[og_row - x][og_column - x].type)
                            return valid_queen_move
                        else: #If final square is not own piece/empty
                            print("ERROR: Queen can't jump over your own piece (" + Board.board[og_row - x][og_column - x].type + ") at " + blocked_piece_coord[0] + blocked_piece_coord[1])
                            return valid_queen_move                        
                    #IF PIECE BLOCKED BY OPPONENTS PIECE
                    elif(Board.board[og_row - x][og_column - x].team != player.colour):
                        if(x != vertical_distance_travelled): #If trying to move the queen past the opponent piece (if the move ends at the queen at opponent piece, you can take)
                            print("ERROR: Queen can't jump over an opponents piece (" + Board.board[og_row - x][og_column - x].type + ") at " + blocked_piece_coord[0] + blocked_piece_coord[1])
                            return valid_queen_move

        #QUEEN MOVING DIAGONALLY DOWN AND LEFT ON THE BOARD
        if (new_row > og_row and og_column > new_column):
            for x in range(1,vertical_distance_travelled+1): #For squares in diagonal path
                #print("Pieces in diagonal path are: ",Board.board[og_row - x][og_column + x].char)
                if (Board.board[og_row + x][og_column - x] != np): #If there is a piece in the path
                    blocked_piece_coord = convert2_to_ascii([og_row + x, og_column - x]) #Obtain coordinates of piece in the way of path
                    #IF PIECE BLOCKED BY YOUR OWN PIECE
                    if (Board.board[og_row + x][og_column - x].team == player.colour): #If the piece you are trying to move over is your own piece
                        if(x == vertical_distance_travelled): #If final square is your own piece
                            print("ERROR: Square " + blocked_piece_coord[0] + blocked_piece_coord[1] + " is occupied by your own " + Board.board[og_row + x][og_column - x].type)
                            return valid_queen_move
                        else: #If final square is not own piece/empty
                            print("ERROR: Queen can't jump over your own piece (" + Board.board[og_row + x][og_column - x].type + ") at " + blocked_piece_coord[0] + blocked_piece_coord[1])
                            return valid_queen_move                        
                    #IF PIECE BLOCKED BY OPPONENTS PIECE
                    elif(Board.board[og_row + x][og_column - x].team != player.colour):
                        if(x != vertical_distance_travelled): #If trying to move the queen past the opponent piece (if the move ends at the queen at opponent piece, you can take)
                            print("ERROR: Queen can't jump over an opponents piece (" + Board.board[og_row + x][og_column - x].type + ") at " + blocked_piece_coord[0] + blocked_piece_coord[1])
                            return valid_queen_move 

        #QUEEN MOVING DIAGONALLY DOWN AND RIGHT ON THE BOARD
        if (new_row > og_row and new_column > og_column):
            for x in range(1,vertical_distance_travelled+1): #For squares in diagonal path
                #print("Pieces in diagonal path are: ",Board.board[og_row - x][og_column + x].char)
                if (Board.board[og_row + x][og_column + x] != np): #If there is a piece in the path
                    blocked_piece_coord = convert2_to_ascii([og_row + x, og_column + x]) #Obtain coordinates of piece in the way of path
                    #IF PIECE BLOCKED BY YOUR OWN PIECE
                    if (Board.board[og_row + x][og_column + x].team == player.colour): #If the piece you are trying to move over is your own piece
                        if(x == vertical_distance_travelled): #If final square is your own piece
                            print("ERROR: Square " + blocked_piece_coord[0] + blocked_piece_coord[1] + " is occupied by your own " + Board.board[og_row + x][og_column + x].type)
                            return valid_queen_move
                        else: #If final square is not own piece/empty
                            print("ERROR: Queen can't jump over your own piece (" + Board.board[og_row + x][og_column + x].type + ") at " + blocked_piece_coord[0] + blocked_piece_coord[1])
                            return valid_queen_move                        
                    #IF PIECE BLOCKED BY OPPONENTS PIECE
                    elif(Board.board[og_row + x][og_column + x].team != player.colour):
                        if(x != vertical_distance_travelled): #If trying to move the queen past the opponent piece (if the move ends at the queen at opponent piece, you can take)
                            print("ERROR: Queen can't jump over an opponents piece (" + Board.board[og_row + x][og_column + x].type + ") at " + blocked_piece_coord[0] + blocked_piece_coord[1])
                            return valid_queen_move  
                        
        #VERTICAL MOVEMENT#

        #QUEEN MOVING UP THE BOARD(i.e if any pieces are blocking, then return error)
        if (og_row > new_row and vertical_distance_travelled != horizontal_distance_travelled):
            for x in range(1,vertical_distance_travelled+1):
                if (Board.board[og_row-x][og_column] != np): #If there is a piece in the path
                    blocked_piece_coord = convert2_to_ascii([og_row-x,og_column]) #Obtain coordinates of piece in the way of path
                    #IF PIECE BLOCKED BY YOUR OWN PIECE
                    if (Board.board[og_row-x][og_column].team == player.colour): #If the piece you are trying to move over is your own piece
                        print("ERROR: Queen can't jump over your own piece (" + Board.board[og_row-x][og_column].type + ") at " + blocked_piece_coord[0] + blocked_piece_coord[1])
                        return valid_queen_move                        
                    #IF PIECE BLOCKED BY OPPONENTS PIECE
                    elif(Board.board[og_row-x][og_column].team != player.colour):
                         if(x != vertical_distance_travelled): #If trying to move the queen past the opponent piece (if the move ends at the queen at opponent piece, you can take)
                            print("ERROR: Queen can't jump over an opponents piece (" + Board.board[og_row-x][og_column].type + ") at " + blocked_piece_coord[0] + blocked_piece_coord[1])
                            return valid_queen_move 
    
        #QUEEN MOVING DOWN THE BOARD (WITHOUT BEING BLOCKED BY ANY PIECES)
        if (new_row > og_row and vertical_distance_travelled != horizontal_distance_travelled): #Moving down the board
            for x in range(1,vertical_distance_travelled+1):
                if (Board.board[og_row+x][og_column] != np): #If there is a piece in the path
                    blocked_piece_coord = convert2_to_ascii([og_row+x,og_column]) #Obtain coordinates of piece in the way of path
                    #IF PIECE BLOCKED BY YOUR OWN PIECE
                    if (Board.board[og_row+x][og_column].team == player.colour): #If the piece you are trying to move over is your own piece
                        print("ERROR: Queen can't jump over your own piece (" + Board.board[og_row+x][og_column].type + ") at " + blocked_piece_coord[0] + blocked_piece_coord[1])
                        return valid_queen_move                        
                    #IF PIECE BLOCKED BY OPPONENTS PIECE
                    elif(Board.board[og_row+x][og_column].team != player.colour):
                         if(x != vertical_distance_travelled): #If trying to move the queen past the opponent piece (if the move ends at the queen at opponent piece, you can take)
                            print("ERROR: Queen can't jump over an opponents piece (" + Board.board[og_row+x][og_column].type + ") at " + blocked_piece_coord[0] + blocked_piece_coord[1])
                            return valid_queen_move
        
        #HORIZONTAL MOVEMENT#

        #CHECK IF CASTLE CAN MOVE RIGHT ON THE BOARD (WITHOUT BEING BLOCKED BY ANY PIECES)
        if (new_column > og_column and vertical_distance_travelled != horizontal_distance_travelled): #Moving right on the board
            for y in range(1,horizontal_distance_travelled+1):
                if (Board.board[og_row][og_column + y] != np): #If there is a piece in the path
                    blocked_piece_coord = convert2_to_ascii([og_row,og_column + y]) #Obtain coordinates of piece in the way of path
                    #IF PIECE BLOCKED BY YOUR OWN PIECE
                    if (Board.board[og_row][og_column + y].team == player.colour): #If the piece you are trying to move over is your own piece
                        print("ERROR: Queen can't jump over your own piece (" + Board.board[og_row][og_column + y].type + ") at " + blocked_piece_coord[0] + blocked_piece_coord[1])
                        return valid_queen_move                        
                    #IF PIECE BLOCKED BY OPPONENTS PIECE
                    elif(Board.board[og_row][og_column + y].team != player.colour):
                         if(y != horizontal_distance_travelled): #If trying to move the queen past the opponent piece (if the move ends at the queen at opponent piece, you can take)
                            print("ERROR: Queen can't jump over an opponents piece (" + Board.board[og_row][og_column + y].type + ") at " + blocked_piece_coord[0] + blocked_piece_coord[1])
                            return valid_queen_move  

        #CHECK IF CASTLE CAN MOVE LEFT ON THE BOARD (WITHOUT BEING BLOCKED BY ANY PIECES)
        if (og_column > new_column and vertical_distance_travelled != horizontal_distance_travelled): #Moving down the board
            for y in range(1,horizontal_distance_travelled+1):
                if (Board.board[og_row][og_column - y] != np): #If there is a piece in the path
                    blocked_piece_coord = convert2_to_ascii([og_row,og_column - y]) #Obtain coordinates of piece in the way of path
                    #IF PIECE BLOCKED BY YOUR OWN PIECE
                    if (Board.board[og_row][og_column - y].team == player.colour): #If the piece you are trying to move over is your own piece
                        print("ERROR: Queen can't jump over your own piece (" + Board.board[og_row][og_column - y].type + ") at " + blocked_piece_coord[0] + blocked_piece_coord[1])
                        return valid_queen_move                        
                    #IF PIECE BLOCKED BY OPPONENTS PIECE
                    elif(Board.board[og_row][og_column - y].team != player.colour):
                         if(y != horizontal_distance_travelled): #If trying to move the queen past the opponent piece (if the move ends at the queen at opponent piece, you can take)
                            print("ERROR: Castle can't jump over an opponents piece (" + Board.board[og_row][og_column - y].type + ") at " + blocked_piece_coord[0] + blocked_piece_coord[1])
                            return valid_queen_move        
        
        #IF VALID QUEEN MOVE
        print("MOVE: Moved " + player.colour + " queen from " + board_move[1] + board_move[2] + " to " + board_move[3] + board_move[4] + "\n") #Print move validation message
        #IF A PIECE IS TAKEN (PRINT CAPTURE MESSAGE)
        if(Board.board[new_row][new_column] != np and Board.board[new_row][new_column].team != current_game_colour): #If end square of move is an opponents piece
                print("CAPTURE!: " + player.name + " takes " + Board.board[new_row][new_column].team + " " + Board.board[new_row][new_column].type + " at " + board_move[3] + board_move[4] + " with the queen" "\n" )
            
        #SET NEW BOARD PIECE LOCATIONS
        Board.board[og_row][og_column] = np #Sets original position blank(moved piece)
        Board.board[new_row][new_column] = getPieceObject(player,piece)
        valid_queen_move = True
        return valid_queen_move 
       
def changePlayer(current_player,p1,p2):
    if current_player == p1:
        return p2
    else:
        return p1

#Sets starting positions of pieces
def set_starting_board():
        for x in range(0,len(Board.board[0])):
            Board.board[1][x] = bp
            Board.board[6][x] = wp
            Board.board[2][x] = np
            Board.board[3][x] = np
            Board.board[4][x] = np
            Board.board[5][x] = np

        Board.board[0][0] = Board.board[0][7] = bc
        Board.board[7][0] = Board.board[7][7] = wc #Setting castles
        Board.board[0][1] = Board.board[0][6] = bh
        Board.board[7][1] = Board.board[7][6] = wh #Setting knights
        Board.board[0][2] = Board.board[0][5] = bb
        Board.board[7][2] = Board.board[7][5] = wb #Setting bishops
        Board.board[0][3] = bk
        Board.board[7][3] = wk #Setting kings
        Board.board[0][4] = bq
        Board.board[7][4] = wq #Setting queens

#Prints the board with current piece objects in the matrix
def board_print():
        print(" "*4 + "a" + " "*4 + "b" + " "*4 + "c" + " "*4 + "d" + " "*4 + "e" + " "*4 + "f" + " "*4 + "g" + " "*4 + "h") #Print top coords
        print("  "+ "-"* 40) #Print top border
        for x in range(0,len(Board.board[0])): 
            print(str(x+1),end="") #Print y coords
            for y in range(0,len(Board.board[0])):
                if(Board.board[x][y].team == 'b'):
                     print(" | " + "\033[34m%s\033[0m" % Board.board[x][y].char + " ", end="") #Changes b pieces to blue
                else:
                    print(" | " + Board.board[x][y].char + " ", end="") #Prints white pieces

                if (y == len(Board.board[0]) - 1):
                    print("| \n")
                    print("  "+ chr(8254)* 40)
        
        print("\n")

#Requests input move from user "i.e Pa7a5", validates input & returns valid board move
def get_move():
            move = input("Enter move: ")
            while(validate_input(move) != True):
                print(validate_input(move)) #Prints incorrect input error message
                move = input("Enter move: ") 
            return move

#Verifies the format of move ("Piece,letter,number,letter,number" i.e. Pa7a5)
def validate_input(move):
    allowed_chars = 'abcdefgh'
    if (len(move) == 5):
        if (move[0] in Board.pieces):
            if (move[2].isdigit() == True and move[4].isdigit() == True and move[1] in allowed_chars and move[3] in allowed_chars):
                if(int(move[2]) in range(1,9) and int(move[4]) in range(1,9)):
                    if(move[1] != move[3] or move[2] != move[4]): 
                        return True
                    else:
                         return "Cannot move piece to same location"
                else: 
                    return "Coordinates must be between 1-8"
            else:
                return "Please enter valid coordinate on the board E.g Pe4e5"
        else:
            return "Must enter a valid piece"
    else:
        return "Must have an input length of 5"

#Validates piece position, colour & move
def move_piece(board_move,player):
        valid_move = False
        #1. CONVERT COORDINATES (i.e d4 -> [3][3])
        #Convert chess coords d4 to matrix nums [3][3] 
        matrix_move = convert_coords(board_move) #Obtains matrix array for moves
        piece = board_move[0] #E.g. 'P'
        #print(matrix_move) #Prints matrix_coords [6,0,4,0] for a7a5

        #2. VALIDATE PIECE LOCATION AND CORRECT COLOUR FOR PLAYER
        if (validate_player_piece_selection(player, piece, board_move, matrix_move) == True):
            
            #3. Obtain piece object for requested piece
            coloured_piece = getPieceObject(player,piece) #Obtains piece object for selected piece e.g. bp "black pawn"
            #print(coloured_piece.type) #Prints requested piece name
            #print(coloured_piece.team) #Prints requested piece colour
            #print(coloured_piece.char) #Prints requested piece char
            #4. Select which piece function to execute
            valid_move = executePieceFunction(board_move,matrix_move, player)

        return valid_move #Returns true/false if the move was successfully made or not

        

#Converts board coordinates to matrix coords
def convert_coords(ascimove):
        move_coords = [] #Empty array for new coords
        int_to_matrix = int(ascimove[2]) - 1
        move_coords.append(int_to_matrix)
        char_to_int = ord(ascimove[1])-97
        move_coords.append(char_to_int)
        int_to_matrix = int(ascimove[4]) - 1
        move_coords.append(int_to_matrix)
        char_to_int = ord(ascimove[3])-97
        move_coords.append(char_to_int)
        #print(int_to_matrix)
        #print(char_to_int)
        #print(move_coords)
        return move_coords

def validate_player_piece_selection(player, piece, board_move, matrix_move):
        #CHECK VALID SELECTION OF PLAYERS PIECE
        
        #Check if piece is actually in og position
        if (check_piece_location(piece,matrix_move) == True): #Checks if piece you are trying to move is at the correct coord
            #Check if piece belongs to that person
            if (check_player_piece(player, matrix_move) == True):
                return True
            else:
                print("Cannot move an opponents piece")
                return False
        else:
            print("The piece you are trying to move is not at that location")
            return False

#Checks if piece requested to move is actually in correct place  - returns Bool
def check_piece_location(piece, move_matrix):
        #Location of position requested by move is Board.board[move_matrix[0][move_matrix[1]]]
        piece_name = getPieceName(piece) #Converts piece input 'P' to 'pawn'
        #print("Wanting to move piece: " + piece_name) #Prints requested piece to move
        #print("Actual piece at location: " + Board.board[move_matrix[0]][move_matrix[1]].type) #Prints the piece at og location
        if (Board.board[move_matrix[0]][move_matrix[1]].type == piece_name):
            return True
        else:
            return False

#Takes piece char from [Pe5e7] & returns string name of piece
def getPieceName(piece):
    match piece:
            case 'P':
                return 'pawn'
            case 'C':
                return 'castle'
            case 'H':
                return 'horse'
            case 'B':
                return 'bishop'
            case 'K':
                return 'king'
            case 'Q':
                return 'queen'
            case '_':
                return "Error in gpn switch case - piece not found"

#Checks if the piece a player is trying to move is on the correct team - returns Bool     
def check_player_piece(player, move_matrix):
        #print("Colour of selected piece: " + Board.board[move_matrix[0]][move_matrix[1]].team) #Prints colour of requested piece
        #print("Colour of player: " + player.colour + "\n") #Prints colour of current player
        if (Board.board[move_matrix[0]][move_matrix[1]].team == player.colour): #If the piece they are trying to move is not theirs
           return True
        else:
            return False
        
#Gets the piece object from the player & piece        
def getPieceObject(player, piece):
        match piece:
            case 'P':
                if (player.colour == 'w'):
                    return wp
                else:
                    return bp
            case 'C':
                if (player.colour == 'w'):
                    return wc
                else:
                    return bc
            case 'H':
                if (player.colour == 'w'):
                    return wh
                else:
                    return bh
            case 'B':
                if (player.colour == 'w'):
                    return wb
                else:
                    return bb
            case 'K':
                if (player.colour == 'w'):
                    return wk
                else:
                    return bk
            case 'Q':
                if (player.colour == 'w'):
                    return wq
                else:
                    return bq
            case '_':
                return "Error in cp switch case - piece not found"

#Executes the function to move a valid piece
def executePieceFunction(board_move, matrix_move, player):
        match board_move[0]:
            case 'P':
                return Board.move_pawn(player,matrix_move, board_move)
            case 'C':
                return Board.move_castle(player,matrix_move, board_move)
            case 'H':
                return Board.move_horse(player, matrix_move, board_move)
            case 'B':
                return Board.move_bishop(player, matrix_move, board_move)
            case 'K':
                return Board.move_king(player, matrix_move, board_move)
            case 'Q':
                return Board.move_queen(player, matrix_move, board_move)
            case '_':
                return "Error in switch case - piece not found"

def convert2_to_ascii(matrix_coords):
     row = matrix_coords[0]
     column = matrix_coords[1]
     row = row+1
     column = chr(column+97)
     return [str(column),str(row)]
