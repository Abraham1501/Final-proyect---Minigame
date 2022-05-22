import pygame
from sys import exit
import random 

pygame.init()

# Configuration
# Variables

# Levels & game
SCREEN_WIDTH = 550
SCREEN_HEIGHT = 650
CENTER = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
GAME_NAME = "Juego"
LEVEL = 0
Game_active = False
Score = 0

#Player
EJE_X_PLAYER = SCREEN_WIDTH // 2 - 50
EJE_Y_PLAYER = SCREEN_HEIGHT - 100
POSITION = [EJE_X_PLAYER, EJE_Y_PLAYER]
Move_left = False
Move_right = False
SPEED_MOVEMENT = 3

#Shoot
Shoot = False
EJE_X_SHOOT = POSITION[0]
EJE_Y_SHOOT = POSITION[1]
SHOOT_TIME = 30
SPEED_SHOOT = 20

#Alien
ALIEN_COUNT = 1
EJE_X_ALIEN1 = random.choice(range(SCREEN_WIDTH - 450, SCREEN_WIDTH - 100))
EJE_X_ALIEN2 = random.choice(range(SCREEN_WIDTH - 450, SCREEN_WIDTH - 100))
EJE_X_ALIEN3 = random.choice(range(SCREEN_WIDTH - 450, SCREEN_WIDTH - 100))
    #Alien_Heights = [SCREEN_HEIGHT - 325, SCREEN_HEIGHT - 280, SCREEN_HEIGHT - 235]
    #EJE_Y_ALIEN = random.choice(Alien_Heights)
EJE_Y_ALIEN1 = SCREEN_HEIGHT - 575
EJE_Y_ALIEN2 = SCREEN_HEIGHT - 530
EJE_Y_ALIEN3 = SCREEN_HEIGHT - 485
ALIEN_RECT_WIDTH = 30
ALIEN_RECT_HEIGHT = 30
    #ALIEN_POSITION = [EJE_X_ALIEN, EJE_Y_ALIEN]
ALIEN_SPEED_MOVEMENT1 = random.uniform(6,7) 
ALIEN_SPEED_MOVEMENT2 = random.uniform(5,6)
ALIEN_SPEED_MOVEMENT3 = random.uniform(4,5)
    #RANDOM_SPEED = random.uniform(0,1)
    #SPAWNING_ALIEN_Y = SCREEN_HEIGHT - 325
    
# Basic configuration
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(GAME_NAME)
clock = pygame.time.Clock()
font = pygame.font.Font('PyGame_Graphics/font/Pixeltype.ttf', 50)

# Scene start
instructions_surf = font.render('Press SPACE for start', False, 'White')
instructions_rect = instructions_surf.get_rect(center = (CENTER[0], SCREEN_HEIGHT//2))

#Scene level 1
score_surf = font.render(f'Score: {Score}', False, 'White')
score_rect = score_surf.get_rect(center = (SCREEN_WIDTH//6, SCREEN_HEIGHT//14))

#Scene Gamer over
game_over_surf = font.render('Game Over', False, 'White')
game_over_rect = game_over_surf.get_rect(center = (CENTER[0], SCREEN_HEIGHT//4))
score_rect_game_over = score_surf.get_rect(center = (CENTER[0], SCREEN_HEIGHT//2))
instructions_2_surf = font.render('Press SPACE for continue', False, 'White')
instructions_2_rect_game_over = instructions_surf.get_rect(center = (CENTER[0], SCREEN_HEIGHT - 50))

while True:
    # Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if not Game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if LEVEL == 0:
                        Game_active = True
                        EJE_PLAYER = SCREEN_WIDTH // 2 - 25
                    else:
                        LEVEL = 0
                if event.key == pygame.K_0:
                    LEVEL = -1
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and Shoot == False:
                    Shoot = True
                if event.key == pygame.K_a:
                    Move_left = True
                if event.key == pygame.K_d:
                    Move_right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    Move_left = False
                if event.key == pygame.K_d:
                    Move_right = False
                if event.key == pygame.K_SPACE and Shoot == True:
                    Shoot = False
    # events & changes
    #move
    if Move_right == True:
        EJE_X_PLAYER += SPEED_MOVEMENT
    elif Move_left == True:
        EJE_X_PLAYER -= SPEED_MOVEMENT
    #shoot
    if SHOOT_TIME > 0:
        EJE_Y_SHOOT -= SPEED_SHOOT
        SHOOT_TIME -= 1
    elif SHOOT_TIME == 0:
        EJE_X_SHOOT = EJE_X_PLAYER + 22
        EJE_Y_SHOOT = SCREEN_HEIGHT - 110
        if Shoot == True:
            SHOOT_TIME = 30

    # Scenes
    if Game_active == False:  
        if LEVEL == 0:
            screen.fill('black')
            screen.blit(instructions_surf, instructions_rect)
        elif LEVEL == -1:
            screen.fill('black')
            screen.blit(game_over_surf, game_over_rect)
            screen.blit(score_surf, score_rect_game_over)
            screen.blit(instructions_2_surf,instructions_2_rect_game_over)

    if Game_active == True:
        
        screen.fill('Black')
        pygame.draw.rect(screen, 'White', (EJE_X_PLAYER, EJE_Y_PLAYER, 50, 50), 25)
        screen.blit(score_surf, score_rect)
        if SHOOT_TIME > 0:
            pygame.draw.rect(screen, 'White', (EJE_X_SHOOT, EJE_Y_SHOOT, 6, 10), 5)

        #Spawning
        pygame.draw.rect(screen, 'Red', (EJE_X_ALIEN1, EJE_Y_ALIEN1, ALIEN_RECT_WIDTH, ALIEN_RECT_HEIGHT), 25)
        pygame.draw.rect(screen, 'Purple', (EJE_X_ALIEN2, EJE_Y_ALIEN2, ALIEN_RECT_WIDTH, ALIEN_RECT_HEIGHT), 25)
        pygame.draw.rect(screen, 'Blue', (EJE_X_ALIEN3, EJE_Y_ALIEN3, ALIEN_RECT_WIDTH, ALIEN_RECT_HEIGHT), 25)

        #Alien Movement
        EJE_X_ALIEN1 -= ALIEN_SPEED_MOVEMENT1
        EJE_X_ALIEN2 -= ALIEN_SPEED_MOVEMENT2
        EJE_X_ALIEN3 -= ALIEN_SPEED_MOVEMENT3
        if EJE_X_ALIEN1 <= SCREEN_WIDTH - 500 or EJE_X_ALIEN1 >= SCREEN_WIDTH - 50:
            ALIEN_SPEED_MOVEMENT1 *= -1
        if EJE_X_ALIEN2 <= SCREEN_WIDTH - 500 or EJE_X_ALIEN2 >= SCREEN_WIDTH - 50:
            ALIEN_SPEED_MOVEMENT2 *= -1
        if EJE_X_ALIEN3 <= SCREEN_WIDTH - 500 or EJE_X_ALIEN3 >= SCREEN_WIDTH - 50:
            ALIEN_SPEED_MOVEMENT3 *= -1

    pygame.display.update()
    clock.tick(60)