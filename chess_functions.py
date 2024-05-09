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
    
    def check_piece_location(piece, move_matrix):
        #Location of position requested by move is Board.board[move_matrix[0][move_matrix[1]]]
        piece_name = getPieceName(piece) #Converts piece input 'P' to 'pawn
        print("Wanting to move piece: " + piece_name)
        print("Actual piece at location: " + Board.board[move_matrix[0]][move_matrix[1]].type) #Prints the piece at og location
        if (Board.board[move_matrix[0]][move_matrix[1]].type == piece_name):
            return True
        else:
            return False
    def check_player_piece(player, move_matrix):
        print("Colour of selected piece: " + Board.board[move_matrix[0]][move_matrix[1]].team)
        print("Colour of player: " + player.colour + "\n")
        if (Board.board[move_matrix[0]][move_matrix[1]].team == player.colour): #If the piece they are trying to move is not theirs
           return True
        else:
            return False
    def move_piece(player, piece, move):
        #Obtain piece object for player
        coloured_piece = Board.colourPiece(player,piece) #Obtains piece object for selected piece e.g. bp "black pawn"
        print(coloured_piece.type)
        print(coloured_piece.team)
        print(coloured_piece.char)

        #print(piece)
        #print(move)

        #Change og position to blank
        #print(Board.board[move[0]][move[1]].char) #Prints piece at og location
        Board.board[move[0]][move[1]] = np #Sets original position blank(moved piece)

        #sets piece board (obj) position to new location
        Board.board[move[2]][move[3]] = coloured_piece


    def move_pawn(player,current_move):        
        #1. CONVERT COORDINATES

        #Convert chess coords d4 to matrix nums [3][3] 
        matrix_move = Board.convert_coords(current_move) #Obtains matrix array for moves
        piece = current_move[0]
        #print("Piece: " + piece + "\n")
        original_pos = current_move[1] + current_move[2]
        #print("Og: " + original_pos + "\n")
        og_coords = str(matrix_move[0]) + str(matrix_move[1])
        #print("Og coords:" + og_coords + "\n")
        new_pos = current_move[3] + current_move[4]
        #print("New: " + new_pos + "\n")
        new_coords = str(matrix_move[2]) + str(matrix_move[3])
        #print("New coords:" + new_coords + "\n")
        #print(matrix_move)
        
        #2.CHECK VALID SELECTION OF PLAYERS PAWN
        #Check if piece is actually in og position
        if (Board.check_piece_location(piece,matrix_move) == True): #Checks if piece you are trying to move is at the correct coord
            #Check if piece belongs to that person
            if (Board.check_player_piece(player, matrix_move) == True):
                Board.move_piece(player, piece, matrix_move) #Move the piece ##MOVES PIECE
                print("Sucessfully moved pawn from " + current_move[1] + current_move[2] + " to " + current_move[3] + current_move[4] + "\n")
                return True
            else:
                print("The piece you are trying to select is either not there or is an opponents piece")
                return False
        else:
            print("The piece you are trying to move is not at that location")
            return False
        
        #3. CHECK RULES OF PAWN MOVE
        #3.1 CAN MOVE 2 FORWARD FROM 2 OR 7
        #3.1 CAN ONLY MOVE 1 FORWARD FROM >2 OR <7
        #3.2 CAN MOVE DIAGONALLY ONLY IF TAKING A PIECE
        #Ensure when an error in either of these occurs, to make the opponent try again
        #When successful error loop implemented, begin to actually move piece
        
    
    def move_castle(player, current_move):
        print("Moved castle")
    
    def move_horse(player, current_move):
        print("Moved horse")
    
    def move_bishop(player, current_move):
        print("Moved bishop")
    
    def move_king(player, current_move):
        print("Moved king")
    
    def move_queen(player, current_move):
        print("Moved queen")
    
        #Check if piece is actually in og position
        #Check if piece belongs to that person
    
    def selectPiece(move,player):
        match move[0]:
            case 'P':
                return Board.move_pawn(player,move)
            case 'C':
                return Board.move_castle(player, move)
            case 'H':
                return Board.move_horse(player, move)
            case 'B':
                return Board.move_bishop(player, move)
            case 'K':
                return Board.move_king(player, move)
            case 'Q':
                return Board.move_queen(player, move)
            case '_':
                return "Error in switch case - piece not found"
    
    def colourPiece(player, piece):
        print("colourPiece function: \n")
        print("Player: ",player)
        print("Piece: ",piece)
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



def setPlayer(current_player,p1,p2):
    if current_player == p1:
        return p2
    else:
        return p1

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
                print(" | " + Board.board[x][y].char + " ", end="")
                if (y == len(Board.board[0]) - 1):
                    print("| \n")
                    print("  "+ chr(8254)* 40)
        
        print("\n")

#Requests input move from user "i.e Pa7a5"
def get_move():
            move = input("Enter move: ")
            while(validate_input(move) != True):
                print(validate_input(move))
                move = input("Enter move: ") 
            return move

#Verifies the formate of move ("Piece,letter,number,letter,number" i.e. Pa7a5)
def validate_input(move):
    allowed_chars = 'abcdefgh'
    if (len(move) == 5):
        if (move[0] in Board.pieces):
            if (move[2].isdigit() == True and move[4].isdigit() == True and move[1] in allowed_chars and move[3] in allowed_chars):
                if(int(move[2]) in range(1,9) and int(move[4]) in range(1,9)):
                    return True
                else: 
                    return "Coordinates must be between 1-8"
            else:
                return "Please enter valid coordinate on the board E.g Pe4e5"
        else:
            return "Must enter a valid piece"
    else:
        return "Must have an input length of 5"