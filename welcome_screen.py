import pygame,sys
from chess_functions3 import *



# pygame.init() will initialize all pygame modules
pygame.init()
clock = pygame.time.Clock() #defines pygame clock
screen = pygame.display.set_mode([800, 800]) #defines window with h,w as 800
base_font = pygame.font.Font(None,32) #sets a font
header_font = pygame.font.Font(None,56)
name_font = pygame.font.Font(None,24)
pygame.display.set_caption('Doms Chess Game') # set the pygame window name


p1_string = '' #sets an empty user string variable
p1_input_rect = pygame.Rect(330,435,140,32) #creates rectangle for user input text at 200,200 of w,h 140,32
p1_input_box_active = False

p2_string = '' #Sets empty user p2 variable
p2_input_rect = pygame.Rect(330,535,140,32)
p2_input_box_active = False

start_button_rect = pygame.Rect(400,650,100,32)
start_button_rect.center= (400,650)
start_button_active = False

#Chess Board
board = pygame.image.load(r'chess_img.jpeg')
board_rect = board.get_rect()
screen_rect = screen.get_rect()
board_rect.center = screen_rect.center

#Board names
player_1_string = ''
player_2_string = ''
name_1_rect = pygame.Rect(10,100,75,32)
name_2_rect = pygame.Rect(715,100,75,32)

#Error message
error_message_string = 'This is a test error message'
error_message_rect = pygame.Rect(400,700,550,32)
error_message_rect.center = (screen_rect.centerx,685)

#Input move
input_move_string = ''
input_move = ''
input_move_rect = pygame.Rect(400,720,100,32)
input_move_rect.center = (screen_rect.centerx,730)
input_move_rect_active = False

game_over = False
welcome_screen = True


    
while not game_over: #while game still running
    for event in pygame.event.get(): #Checks for any event that occurs in pygame
        if event.type == pygame.QUIT: #Checks if pygame is quit
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if p1_input_rect.collidepoint(event.pos):
                p1_input_box_active = True
            else:
                p1_input_box_active = False
            if p2_input_rect.collidepoint(event.pos):
                p2_input_box_active = True
            else:
                p2_input_box_active = False
            if input_move_rect.collidepoint(event.pos):
                input_move_rect_active = True
            else:
                input_move_rect_active = False
            
            if start_button_active == True:
                welcome_screen = False
                player1 = Player(p1_string) #Creates player 1 and 2 objects on start button press
                player2 = Player(p2_string)
                starter = Player.choose_p1(player1,player2) #Select b/w & choose who plays first
                current_player = starter #Sets current player(obj) to play first
                set_starting_board()
                start_button_active = False
          

        if event.type == pygame.KEYDOWN: #Checks if any key is pressed
            if p1_input_box_active == True:
                if event.key == pygame.K_BACKSPACE: #checks if a backspace is pressed
                    p1_string = p1_string[0:-1] #reformat the string by taking of the last key
                else:
                    p1_string += event.unicode #adds the character of keypress to user string
            
            if p2_input_box_active == True:
                if event.key == pygame.K_BACKSPACE: #checks if a backspace is pressed
                    p2_string = p2_string[0:-1] #reformat the string by taking of the last key
                else:
                    p2_string += event.unicode #adds the character of keypress to user string
            
            if input_move_rect_active == True:
                if event.key == pygame.K_BACKSPACE: #checks if a backspace is pressed
                    input_move_string = input_move_string[0:-1] #reformat the string by taking of the last key
                else:
                    input_move_string += event.unicode #adds the character of keypress to user string

                if event.key == pygame.K_RETURN:
                    input_move = input_move_string[0:-1] #Copies input move and removes hidden escape char
                    input_move_string = ''
                    if validate_input(input_move) == True:
                        #convert coords, validate piece selection & return error messages if false - true if true
                        #if valid selection, execute piece function
                        error_message_string = 'Moved allowed'
                        move_piece(input_move,current_player) #Returns true/false if move was executed
                        
                        
                        current_player = changePlayer(current_player,player1,player2)

                    else:
                        error_message_string = validate_input(input_move)
                        input_valid = False
                    

                
        
    if welcome_screen == True:
        screen.fill((0,0,0)) #fill screen
        #Render main header text
        chess_main_surface = header_font.render('Doms Chess Game',True,(255,255,255)) #Render text
        chess_main_surface_rect = chess_main_surface.get_rect(center = (400,200)) #Obtain text rect & center coordinate
        screen.blit(chess_main_surface,(chess_main_surface_rect)) #Put main text on screen

        #Render enter p1 and p2 labels
        p1_label_surface = base_font.render('Enter the name of player 1:',True,(255,255,255))
        p1_label_surface_rect = p1_label_surface.get_rect(center = (400,400))
        screen.blit(p1_label_surface, p1_label_surface_rect)
        
        p2_label_surface = base_font.render('Enter the name of player 2:',True,(255,255,255))
        p2_label_surface_rect = p2_label_surface.get_rect(center = (400,500))
        screen.blit(p2_label_surface, p2_label_surface_rect)

        #Render p1 text box
        pygame.draw.rect(screen,(255,255,255),p1_input_rect,2) #draw p1 rect onto screen with white border width 2
        p1_string_surface = base_font.render(p1_string,True,(255,255,255)) #creates a surface for the user text
        screen.blit(p1_string_surface,(p1_input_rect.x + 5,p1_input_rect.y + 5)) #.blit puts string surface at the coordinates of the input rect
        p1_input_rect.w = max(140,p1_string_surface.get_width() + 10)

        #Render p2 text box
        pygame.draw.rect(screen,(255,255,255),p2_input_rect,2) #draw p1 rect onto screen with white border width 2
        p2_string_surface = base_font.render(p2_string,True,(255,255,255)) #creates a surface for the user text
        screen.blit(p2_string_surface,(p2_input_rect.x + 5,p2_input_rect.y + 5)) #.blit puts string surface at the coordinates of the input rect
        p2_input_rect.w = max(140,p2_string_surface.get_width() + 10)

        #Render start button
        pygame.draw.rect(screen,(139,0,0),start_button_rect,0)
        start_string_surface = base_font.render('Start',True,(255,255,255))
        start_string_surface_rect = start_string_surface.get_rect(center = (400,650))
        screen.blit(start_string_surface,start_string_surface_rect)
        if start_button_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen,(255,0,0),start_button_rect,0)
                start_string_surface = base_font.render('Start',True,(255,255,255))
                start_string_surface_rect = start_string_surface.get_rect(center = (400,650))
                screen.blit(start_string_surface,start_string_surface_rect)
                start_button_active = True
        else:
            start_button_active = False

    else:
        #Print board with names
        player_1_string = p1_string #copying name strings
        player_2_string = p2_string
        screen.fill((0,0,0)) #filling screen black
        screen.blit(board, board_rect) #adding board
        #Printing names
        pygame.draw.rect(screen,(0,0,0),name_1_rect,0) #draw p1 and p2 name rects onto screen 
        pygame.draw.rect(screen,(0,0,0),name_2_rect,0)
        if (current_player.name == player_1_string):
            name1_string_surface = name_font.render(player_1_string,True,(255,255,0)) #render text for names
            name2_string_surface = name_font.render(player_2_string,True,(255,255,255))

        else:
            name1_string_surface = name_font.render(player_1_string,True,(255,255,255)) #render text for names
            name2_string_surface = name_font.render(player_2_string,True,(255,255,0))

        name1_string_surface_rect = name1_string_surface.get_rect() #get text rect
        name1_string_surface_rect.center = name_1_rect.center #center text rect same as rect box
        name2_string_surface_rect = name2_string_surface.get_rect()
        name2_string_surface_rect.center = name_2_rect.center
        screen.blit(name1_string_surface,name1_string_surface_rect) #.blit puts string surface at the coordinates of the input rect
        screen.blit(name2_string_surface,name2_string_surface_rect) #.blit puts string surface at the coordinates of the input rect
        #Printing error messages
        #pygame.draw.rect(screen,(0,0,0),error_message_rect,0)
        error_message_string_surface = name_font.render(error_message_string,True,(255,255,255))
        error_message_string_surface_rect = error_message_string_surface.get_rect()
        error_message_string_surface_rect.center = error_message_rect.center
        screen.blit(error_message_string_surface,error_message_string_surface_rect)
        #Printing input box
        pygame.draw.rect(screen,(255,255,255),input_move_rect,2)
        input_move_string_surface = name_font.render(input_move_string,True,(255,255,255))
        input_move_string_surface_rect = input_move_string_surface.get_rect()
        input_move_string_surface_rect.center = input_move_rect.center
        screen.blit(input_move_string_surface,input_move_string_surface_rect)

        #begin adding chess starting board
        for x in range(0,len(Board.board[0])):
                        for y in range(0,len(Board.board[0])):
                            Board.board[x][y].coords = (150 + y*64, 150 + x*64)
                            screen.blit(Board.board[x][y].image, Board.board[x][y].coords) #(w_pawn,matrix)
        

    pygame.display.flip() #updates the full display surface to the screen
    clock.tick(60)


