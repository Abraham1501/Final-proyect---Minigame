import pygame
from sys import exit
import random

pygame.init()

# Levels & game
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 650
CENTER = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
GAME_NAME = "Juego"
Game_active = False

# Basic configuration
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(GAME_NAME)
clock = pygame.time.Clock()
font = pygame.font.Font('PyGame_Graphics/font/Pixeltype.ttf', 50)

#Alien
ALIEN_SPAWN_RIGHT = 1
ALIEN_SPAWN_LEFT = 2
SPAWN_SIDE = [ALIEN_SPAWN_LEFT,ALIEN_SPAWN_RIGHT]
random_spawn1_side = random.choice(SPAWN_SIDE)
random_spawn2_side = random.choice(SPAWN_SIDE)
random_spawn3_side = random.choice(SPAWN_SIDE)

EJE_1_X_ALIEN1 = -15
EJE_2_X_ALIEN1 = 515
EJE_1_X_ALIEN2 = -15
EJE_2_X_ALIEN2 = 515
EJE_1_X_ALIEN3 = -15
EJE_2_X_ALIEN3 = 515

EJE_Y_ALIEN1 = SCREEN_HEIGHT - SCREEN_HEIGHT// 10 * 7
EJE_Y_ALIEN2 = SCREEN_HEIGHT - SCREEN_HEIGHT// 10 * 8
EJE_Y_ALIEN3 = SCREEN_HEIGHT - SCREEN_HEIGHT// 10 * 9

ALIEN_RECT_WIDTH = 30
ALIEN_RECT_HEIGHT = 30

ALIEN_SPEED_MOVEMENT1 = 5
ALIEN_SPEED_MOVEMENT2 = 5.5
ALIEN_SPEED_MOVEMENT3 = 6

def ALIEN1_LEFT():
    pygame.draw.rect(screen, 'Red', (EJE_1_X_ALIEN1, EJE_Y_ALIEN1, ALIEN_RECT_WIDTH, ALIEN_RECT_HEIGHT), 25)
def ALIEN1_RIGHT():
    pygame.draw.rect(screen, 'Red', (EJE_2_X_ALIEN1, EJE_Y_ALIEN1, ALIEN_RECT_WIDTH, ALIEN_RECT_HEIGHT), 25)
def ALIEN2_LEFT():
    pygame.draw.rect(screen, 'Blue', (EJE_1_X_ALIEN2, EJE_Y_ALIEN2, ALIEN_RECT_WIDTH, ALIEN_RECT_HEIGHT), 25)
def ALIEN2_RIGHT():
    pygame.draw.rect(screen, 'Blue', (EJE_2_X_ALIEN2, EJE_Y_ALIEN2, ALIEN_RECT_WIDTH, ALIEN_RECT_HEIGHT), 25)
def ALIEN3_LEFT():
    pygame.draw.rect(screen, 'Yellow', (EJE_1_X_ALIEN3, EJE_Y_ALIEN3, ALIEN_RECT_WIDTH, ALIEN_RECT_HEIGHT), 25)
def ALIEN3_RIGHT():
    pygame.draw.rect(screen, 'Yellow', (EJE_2_X_ALIEN3, EJE_Y_ALIEN3, ALIEN_RECT_WIDTH, ALIEN_RECT_HEIGHT), 25)

#Player
EJE_X_PLAYER = SCREEN_WIDTH // 2
EJE_Y_PLAYER = SCREEN_HEIGHT - 100
POSITION = [EJE_X_PLAYER, EJE_Y_PLAYER]
Move_left = False
Move_right = False
SPEED_MOVEMENT = 4
player_surf = pygame.image.load('PyGame_Graphics/Player/player_1.png').convert_alpha()
player_rect = player_surf.get_rect(center = (EJE_X_PLAYER, EJE_Y_PLAYER))

#Shoot
Shoot = False
EJE_X_SHOOT = POSITION[0]
EJE_Y_SHOOT = POSITION[1]
SHOOT_TIME = 20
Shoot_time = SHOOT_TIME
SPEED_SHOOT = 10
bullet_player_surf = pygame.image.load('PyGame_Graphics/Player/bullet_player_1.png').convert_alpha()
bullet_player_rect = bullet_player_surf.get_rect(center = (EJE_X_SHOOT, EJE_Y_SHOOT))
bullets = []

#Scene start
instructions_surf = font.render('Press SPACE for start', False, 'White')
instructions_rect = instructions_surf.get_rect(center = (CENTER[0], SCREEN_HEIGHT//2))

#levels
LEVEL = 0
LEVEL_CHANGES = 100
SCORE = 0
Score = 0

#level changes
score_surf = font.render(f'Score: {Score}', False, 'White')
score_rect = score_surf.get_rect(midtop = (85, 25))
level_surf = font.render(f'Level {LEVEL}', False, 'White')
level_rect = level_surf.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT/2))

#Scene level 1

#Scene Gamer over and victory
game_over_surf = font.render('Game Over', False, 'White')
game_over_rect = game_over_surf.get_rect(center = (CENTER[0], SCREEN_HEIGHT//4))
completed_surf = font.render('COMPLETED!', False, 'White')
completed_rect = completed_surf.get_rect(center = (CENTER[0], SCREEN_HEIGHT//4))
score_rect_final = score_surf.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
instructions_2_surf = font.render('Press SPACE for continue', False, 'White')
instructions_2_rect_game_over = instructions_surf.get_rect(center = (CENTER[0], SCREEN_HEIGHT//4 * 3))

#fuctions
def move_bullets():
    for rect in bullets:
        rect.y -= SPEED_SHOOT
    rects = []
    for rect in bullets:
        if rect.y > 0:
            rects.append(rect)
    return rects

def screen_bullets():
    for rect in bullets:
        screen.blit(bullet_player_surf, rect)

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
                        EJE_PLAYER = SCREEN_WIDTH // 2
                        LEVEL = 1
                        LEVEL_CHANGES = 100
                    else:
                        LEVEL = 0
                #teclas especiales
                if event.key == pygame.K_0:
                    LEVEL = -1
                if event.key == pygame.K_1:
                    LEVEL = 1
                    LEVEL_CHANGES = 100
                if event.key == pygame.K_2:
                    LEVEL = 2
                    LEVEL_CHANGES = 100
                if event.key == pygame.K_3:
                    LEVEL = 3
                    LEVEL_CHANGES = 100
                if event.key == pygame.K_4:
                    LEVEL = -2
                    LEVEL_CHANGES = 100

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
                # teclas especiales
                if event.key == pygame.K_0:
                    LEVEL = -1
                if event.key == pygame.K_1:
                    LEVEL = 1
                    LEVEL_CHANGES = 100
                if event.key == pygame.K_2:
                    LEVEL = 2
                    LEVEL_CHANGES = 100
                if event.key == pygame.K_3:
                    LEVEL = 3
                    LEVEL_CHANGES = 100

    # events & changes
    #move
    if EJE_X_PLAYER > 0 and EJE_X_PLAYER < SCREEN_WIDTH:
        if Move_right == True:
            EJE_X_PLAYER += SPEED_MOVEMENT
        elif Move_left == True:
            EJE_X_PLAYER -= SPEED_MOVEMENT
    else:
        if EJE_X_PLAYER <= 0:
            EJE_X_PLAYER += SPEED_MOVEMENT
        else:
            EJE_X_PLAYER -= SPEED_MOVEMENT
    player_rect = player_surf.get_rect(center=(EJE_X_PLAYER, EJE_Y_PLAYER))

    #shoot
    EJE_X_SHOOT = EJE_X_PLAYER
    if Shoot_time > 0:
        Shoot_time -= 1
    if Shoot and Shoot_time == 0:
        Shoot_time = SHOOT_TIME
        bullets.append(bullet_player_surf.get_rect(center = (EJE_X_SHOOT, EJE_Y_SHOOT)))

    # Scenes
    if Game_active == False:
        if LEVEL == 0:
            screen.fill('black')
            screen.blit(instructions_surf, instructions_rect)
        elif LEVEL == -1:
            screen.fill('black')
            screen.blit(game_over_surf, game_over_rect)
            screen.blit(score_surf, score_rect_final)
            screen.blit(instructions_2_surf,instructions_2_rect_game_over)
        elif LEVEL == -2:
            screen.fill('black')
            screen.blit(score_surf,score_rect_final)
            screen.blit(completed_surf,completed_rect)
            screen.blit(instructions_2_surf, instructions_2_rect_game_over)

    if Game_active == True:
        screen.fill('black')
        bullets = move_bullets()
        screen_bullets()
        screen.blit(player_surf, player_rect)
        screen.blit(score_surf, score_rect)
        if LEVEL == 1:
            if LEVEL_CHANGES > 0:
                level_surf = font.render(f'Level {LEVEL}', False, 'White')
                screen.blit(level_surf,level_rect)
                LEVEL_CHANGES -= 1

            # Spawning
            if random_spawn1_side == ALIEN_SPAWN_LEFT:
                ALIEN1_LEFT()
                EJE_1_X_ALIEN1 += ALIEN_SPEED_MOVEMENT1
                if EJE_1_X_ALIEN1 <= SCREEN_WIDTH - 560 or EJE_1_X_ALIEN1 >= SCREEN_WIDTH + 60:
                    ALIEN_SPEED_MOVEMENT1 *= -1 
            if random_spawn1_side == ALIEN_SPAWN_RIGHT:
                ALIEN1_RIGHT()
                EJE_2_X_ALIEN1 -= ALIEN_SPEED_MOVEMENT1
                if EJE_2_X_ALIEN1 <= SCREEN_WIDTH - 560 or EJE_2_X_ALIEN1 >= SCREEN_WIDTH + 60:
                    ALIEN_SPEED_MOVEMENT1 *= -1

            if random_spawn2_side == ALIEN_SPAWN_LEFT:
                ALIEN2_LEFT()
                EJE_1_X_ALIEN2 += ALIEN_SPEED_MOVEMENT2
                if EJE_1_X_ALIEN2 <= SCREEN_WIDTH - 560 or EJE_1_X_ALIEN2 >= SCREEN_WIDTH + 60:
                    ALIEN_SPEED_MOVEMENT2 *= -1  
            if random_spawn2_side == ALIEN_SPAWN_RIGHT:
                ALIEN2_RIGHT()
                EJE_2_X_ALIEN2 -= ALIEN_SPEED_MOVEMENT2
                if EJE_2_X_ALIEN2 <= SCREEN_WIDTH - 560 or EJE_2_X_ALIEN2 >= SCREEN_WIDTH + 60:
                    ALIEN_SPEED_MOVEMENT2 *= -1

            if random_spawn3_side == ALIEN_SPAWN_LEFT:
                ALIEN3_LEFT()
                EJE_1_X_ALIEN3 += ALIEN_SPEED_MOVEMENT3
                if EJE_1_X_ALIEN3 <= SCREEN_WIDTH - 560 or EJE_1_X_ALIEN3 >= SCREEN_WIDTH + 60:
                    ALIEN_SPEED_MOVEMENT3 *= -1        
            if random_spawn3_side == ALIEN_SPAWN_RIGHT:
                ALIEN3_RIGHT()
                EJE_2_X_ALIEN3 -= ALIEN_SPEED_MOVEMENT3
                if EJE_2_X_ALIEN3 <= SCREEN_WIDTH - 560 or EJE_2_X_ALIEN3 >= SCREEN_WIDTH + 60:
                    ALIEN_SPEED_MOVEMENT3 *= -1  

        elif LEVEL == 2:
            if LEVEL_CHANGES > 0:
                level_surf = font.render(f'Level {LEVEL}', False, 'White')
                screen.blit(level_surf,level_rect)
                LEVEL_CHANGES -= 1

        elif LEVEL == 3:
            if LEVEL_CHANGES > 0:
                level_surf = font.render(f'Level {LEVEL}', False, 'White')
                screen.blit(level_surf,level_rect)
                LEVEL_CHANGES -= 1

    pygame.display.update()
    clock.tick(60)