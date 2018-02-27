# Imports
import pygame
import intersects

# Initialize game engine
pygame.init()


# Window
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
TITLE = "Maze"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)


# Make a player
player1 =  [200, 150, 25, 25]
vel1 = [0, 0]
player1_speed = 5
score1 = 0

player2 =  [400, 150, 25, 25]
vel2 = [0, 0]
player2_speed = 5
score2 = 0


# make walls
wall1 =  [300, 275, 200, 25]
wall2 =  [400, 450, 200, 25]
wall3 =  [100, 100, 25, 200]

walls = [wall1, wall2, wall3]

# Make coins
coin1 = [300, 500, 25, 25]
coin2 = [400, 200, 25, 25]
coin3 = [150, 150, 25, 25]

coins = [coin1, coin2, coin3]


# Game loop
win = False
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()

    up1 = pressed[pygame.K_UP]
    down1 = pressed[pygame.K_DOWN]
    left1 = pressed[pygame.K_LEFT]
    right1 = pressed[pygame.K_RIGHT]

    up2 = pressed[pygame.K_w]
    down2 = pressed[pygame.K_s]
    left2 = pressed[pygame.K_a]
    right2 = pressed[pygame.K_d]

    
    if left1:
        vel1[0] = -player1_speed
    elif right1:
        vel1[0] = player1_speed
    else:
        vel1[0] = 0
    
    
    if left2:
        vel2[0] = -player2_speed
    elif right2:
        vel2[0] = player2_speed
    else:
        vel2[0] = 0

    
    if up1:
        vel1[1] = -player1_speed
    elif down1:
        vel1[1] = player1_speed
    else:
        vel1[1] = 0
    
    
    if up2:
        vel2[1] = -player2_speed
    elif down2:
        vel2[1] = player2_speed
    else:
        vel2[1] = 0


        
        
    # Game logic (Check for collisions, update points, etc.)
    ''' move the player in horizontal direction '''
    player1[0] += vel1[0]
    player2[0] += vel2[0]

    ''' resolve collisions horizontally '''
    for w in walls:
        if intersects.rect_rect(player1, w):        
            if vel1[0] > 0:
                player1[0] = w[0] - player1[2]
            elif vel1[0] < 0:
                player1[0] = w[0] + w[2]

        if intersects.rect_rect(player2, w):        
            if vel2[0] > 0:
                player2[0] = w[0] - player2[2]
            elif vel2[0] < 0:
                player2[0] = w[0] + w[2]


    ''' move the player in vertical direction '''
    player1[1] += vel1[1]
    player2[1] += vel2[1]
    
    ''' resolve collisions vertically '''
    for w in walls:
        if intersects.rect_rect(player1, w):                    
            if vel1[1] > 0:
                player1[1] = w[1] - player1[3]
            if vel1[1]< 0:
                player1[1] = w[1] + w[3]


                
        if intersects.rect_rect(player2, w):                    
            if vel2[1] > 0:
                player2[1] = w[1] - player2[3]
            if vel2[1]< 0:
                player2[1] = w[1] + w[3]


    #''' here is where you should resolve player collisions with screen edges '''

    
    ''' get block edges (makes collision resolution easier to read) '''
     
    left = player1[0] 
    right = player1[0] + player1[2]
    top = player1[1]
    bottom = player1[1] + player1[3]

    ''' if the block is moved completely off of the window, reposition it on the other side '''
    if left > WIDTH:
        player1[0] = 0 - player1[2]
    elif right < 0:
        player1[0] = WIDTH
        
    if bottom < 0:
        player1[1] = HEIGHT
    elif top > HEIGHT:
        player1[1] = 0 - player1[3]







    ''' get the coins '''
    hit_list = []

    for c in coins:
        if intersects.rect_rect(player1, c):
            hit_list.append(c)

        if intersects.rect_rect(player2, c):
            hit_list.append(c)
     
    hit_list = [c for c in coins if intersects.rect_rect(player1, c)]
    
    for hit in hit_list:
        coins.remove(hit)
        score1 += 1
        print("sound!")
        
    if len(coins) == 0:
        win = True

        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    pygame.draw.rect(screen, RED, player1)    
    pygame.draw.rect(screen, BLUE, player2)

    for w in walls:
        pygame.draw.rect(screen, WHITE, w)

    for c in coins:
        pygame.draw.rect(screen, YELLOW, c)
        
    if win:
        font = pygame.font.Font(None, 48)
        text = font.render("You Win!", 5, GREEN)
        screen.blit(text, [400, 200])

    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
