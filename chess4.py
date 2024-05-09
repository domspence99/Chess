from v3.welcome_screen import *
import pygame,sys

welcome_screen_init()

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
            
            if start_button_active == True:
                welcome_screen = False          

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
        screen.fill((0,0,0))

    pygame.display.flip() #updates the full display surface to the screen
    clock.tick(60)