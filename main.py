#Shay VanLandschoot
#--DATE--#
# Pygame game template

import pygame
import sys
import config # Import the config module

def init_game ():

    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) 
   
    
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events ():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def main():
    
    screen = init_game()
    clock = pygame.time.Clock()


    
    running = True
    while running:
        running = handle_events()
        #screen.fill(config.WHITE) # Use color from config
        backround_img = pygame.image.load('saturn_family1.jpg')
        screen.blit(backround_img,[0,0])
        # Add code to draw stuff (for example) below this comment
        player_pos= pygame.mouse.get_pos()
        x=player_pos[0]
        y=player_pos[1]
        
        player_img = pygame.image.load('player.png').convert()
        screen.blit(player_img,[x,y])
        player_img.set_colorkey(config.BLACK)




        pygame.display.flip()
        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
