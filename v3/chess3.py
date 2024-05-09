from chess_functions3 import *
import pygame
def main():
    #Pygame initialisation
    #convert_matrix_to_img_coords()
    # initialising Pyame library.
    pygame.init()

    # assigning values to displayHeight and displayWidth
    displayHeight = 800
    displayWidth = 800

    screen = pygame.display.set_mode((displayHeight, displayWidth ))

    # set the pygame window name
    pygame.display.set_caption('Doms Chess Game')

    # create a surface object, image is drawn on it.
    image = pygame.image.load(r'chess_img.jpeg')
    w_pawn = pygame.image.load(r'256px/w_pawn_png_shadow_256px.png')
    b_pawn = pygame.image.load(r'256px/b_pawn_png_shadow_256px.png')
    w_pawn = pygame.transform.scale(w_pawn,(55,55))
    b_pawn = pygame.transform.scale(b_pawn,(55,55))
    #Obtains the coordinates (left, top, width, height)
    image_rect = image.get_rect()
    print(image_rect)
    #set inital image center coords to 0,0
    x = 0
    y = 0
    image_rect.center = (x,y) 
    print(x,y)

    screen_rect = screen.get_rect() #Get screen rect coordinates
    print("screen rect: ",screen_rect)
    image_rect.center = screen_rect.center #set the center of image to center of screen
    
    # infinite loop
    while True:
        #  fill the surface object with white colour
        screen.fill((255, 255, 255))

        # to display surface object at (0, 0) coordinate.
        screen.blit(image, image_rect)
        screen.blit(w_pawn,(150,150)) #(w_pawn,matrix)
        screen.blit(b_pawn,(150,214))
        screen.blit(w_pawn,(150,278))
        screen.blit(b_pawn,(150,342))
        screen.blit(w_pawn,(150,406))
        screen.blit(b_pawn,(150,470))
        screen.blit(w_pawn,(150,534))
        screen.blit(b_pawn,(150,598))

        screen.blit(w_pawn,(150,150))
        screen.blit(b_pawn,(214,150))
        screen.blit(w_pawn,(278,150))
        screen.blit(b_pawn,(342,150))
        screen.blit(w_pawn,(406,150))
        screen.blit(b_pawn,(470,150))
        screen.blit(w_pawn,(534,150))
        screen.blit(b_pawn,(598,150))
        
        #IF Player closes window, quit the application
        for event in pygame.event.get() :
            # if the event object type is QUIT then quitting the pygame
            if event.type == pygame.QUIT :
                    pygame.quit()
                    # quit the program also.
                    quit()

            # Draws the surface object to the screen.
            pygame.display.update()  
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
        print("Current player is: " + current_player.name + " (" + current_player.colour + ")" "\n") #Print current player
        board_print() #Print current state of board
        new_move = get_move() #Returns valid player input as "Pa7a5"
        valid_move = move_piece(new_move,current_player) #Returns true/false if move was executed
        if (valid_move == False): #If move was not executed (due to incorrect move) ask again
            print("Please enter a valid move \n")
            pass
        else:
           current_player = changePlayer(current_player,player1,player2) ####

main()
