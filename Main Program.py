import pygame
from sys import exit
import random
from Object_classes import Player

pygame.init()

# Variables
# Levels & game
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 950
CENTER = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
GAME_NAME = "Juego"
Game_active = False
LEVEL = 0
LEVEL_CHANGES = 100
Score = 0

START_TIME_GAME = pygame.time.get_ticks()
current_time = pygame.time.get_ticks()

#Game
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(GAME_NAME)
clock = pygame.time.Clock()

#Elements
font = pygame.font.Font('Game_project/font/Pixeltype.ttf', 50)
font_2 = pygame.font.Font('Game_project/font/Pixeltype.ttf', 100)

#Enemies
#Alien
ALIEN_COUNT = 1
EJE_X_ALIEN1 = random.choice(range(SCREEN_WIDTH - 450, SCREEN_WIDTH - 100))
EJE_X_ALIEN2 = random.choice(range(SCREEN_WIDTH - 450, SCREEN_WIDTH - 100))
EJE_X_ALIEN3 = random.choice(range(SCREEN_WIDTH - 450, SCREEN_WIDTH - 100))
    #Alien_Heights = [SCREEN_HEIGHT - 325, SCREEN_HEIGHT - 280, SCREEN_HEIGHT - 235]
    #EJE_Y_ALIEN = random.choice(Alien_Heights)
EJE_Y_ALIEN1 = SCREEN_HEIGHT - SCREEN_HEIGHT// 10 * 7
EJE_Y_ALIEN2 = SCREEN_HEIGHT - SCREEN_HEIGHT// 10 * 8
EJE_Y_ALIEN3 = SCREEN_HEIGHT - SCREEN_HEIGHT// 10 * 9
ALIEN_RECT_WIDTH = 30
ALIEN_RECT_HEIGHT = 30
    #ALIEN_POSITION = [EJE_X_ALIEN, EJE_Y_ALIEN]
ALIEN_SPEED_MOVEMENT1 = random.uniform(6,7)
ALIEN_SPEED_MOVEMENT2 = random.uniform(5,6)
ALIEN_SPEED_MOVEMENT3 = random.uniform(4,5)
    #RANDOM_SPEED = random.uniform(0,1)
    #SPAWNING_ALIEN_Y = SCREEN_HEIGHT - 325

bullet_enemie_surf = pygame.image.load('Game_project/Graphics/Enemies/bullet_enemies.png').convert_alpha()
bullet_enemie_rect = bullet_enemie_surf.get_rect(center = (0, 0))

score_surf = font.render(f'Score: {Score}', False, 'White')
score_rect = score_surf.get_rect(midtop = (85, 25))
#backgrounds
background_surf_1 = pygame.image.load('Game_project/Graphics/background_1.png').convert_alpha()
background_surf_2 = pygame.image.load('Game_project/Graphics/background_2.png').convert_alpha()
background_surf_3 = pygame.image.load('Game_project/Graphics/background_3.png').convert_alpha()
backgrounds = [background_surf_1, background_surf_2, background_surf_1, background_surf_3]
rects_backgrounds = []
index_backgrounds = []
Eje_Y_backgrounds = SCREEN_HEIGHT
Cont = 0
for i in range(0,3):
    index_backgrounds.append(random.choice(range(0,3)))
for i in range(0,3):
    rects_backgrounds.append(backgrounds[index_backgrounds[i]].get_rect(bottomleft=(0,Eje_Y_backgrounds)))
    Eje_Y_backgrounds -= 700

#Scene start
name_game_surf = font_2.render('MINIGAME', False, 'White')
name_game_rect = name_game_surf.get_rect(center=(CENTER[0], SCREEN_HEIGHT//10))
instructions_surf = font.render('Press SPACE for start', False, 'White')
instructions_rect = instructions_surf.get_rect(center = (CENTER))
player_stand_surf = pygame.image.load('Game_project/Graphics/Player/player_1.png').convert_alpha()
player_stand_surf = pygame.transform.scale2x(player_stand_surf)
player_stand_surf = pygame.transform.scale2x(player_stand_surf)
player_stand_rect = player_stand_surf.get_rect(center=(CENTER[0], SCREEN_HEIGHT // 4 * 3))
enemy_A_stand_surf = pygame.image.load('Game_project/Graphics/Enemies/Enemies A/enemies_A_ 1.png').convert_alpha()
enemy_A_stand_surf = pygame.transform.scale2x(enemy_A_stand_surf)
enemy_A_stand_rect = enemy_A_stand_surf.get_rect(center=(SCREEN_WIDTH//4, SCREEN_HEIGHT//10 * 3))
enemy_B_stand_surf = pygame.image.load('Game_project/Graphics//Enemies/Enemies B/enemie_B_1.png').convert_alpha()
enemy_B_stand_surf = pygame.transform.scale2x(enemy_B_stand_surf)
enemy_B_stand_rect = enemy_B_stand_surf.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//10 * 3))
enemy_C_stand_surf = pygame.image.load('Game_project/Graphics/Enemies/Enemies C/enemie_C_1.png').convert_alpha()
enemy_C_stand_surf = pygame.transform.scale2x(enemy_C_stand_surf)
enemy_C_stand_rect = enemy_C_stand_surf.get_rect(center=(SCREEN_WIDTH//4 * 3, SCREEN_HEIGHT//10 * 3))

#level changes
level_surf = font.render(f'Level {LEVEL}', False, 'White')
level_rect = level_surf.get_rect(center=(CENTER))

#Scene Gamer over
game_over_surf = font.render('Game Over', False, 'White')
game_over_rect = game_over_surf.get_rect(center = (CENTER[0], SCREEN_HEIGHT//10))
score_rect_final = score_surf.get_rect(center=(CENTER[0], SCREEN_HEIGHT//10 * 3))
level_rect_game_over = level_surf.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//10 * 2))
instructions_2_surf = font.render('Press SPACE for continue', False, 'White')
instructions_2_rect_game_over = instructions_surf.get_rect(center = (CENTER[0], SCREEN_HEIGHT//10 * 5))
player_game_over_surf = pygame.image.load('Game_project/Graphics/Player/Game_over_player.png').convert_alpha()
player_game_over_surf = pygame.transform.scale2x(player_game_over_surf)
player_game_over_surf = pygame.transform.scale2x(player_game_over_surf)
player_game_over_rect = player_game_over_surf.get_rect(center = (CENTER[0], SCREEN_HEIGHT // 4 * 3))

#Scene victory
completed_surf = font.render('COMPLETED!', False, 'White')
completed_rect = completed_surf.get_rect(center = (CENTER[0], SCREEN_HEIGHT//10))
instructions_2_rect_completed = instructions_surf.get_rect(center = (CENTER[0], SCREEN_HEIGHT//10 * 5))

#fuctions
def level_changes(LEVEL_CHANGES):
    level_surf = font.render(f'Level {LEVEL}', False, 'White')
    screen.blit(level_surf, level_rect)
    LEVEL_CHANGES -= 1
    return LEVEL_CHANGES

def get_time(START_TIME_GAME):
    current_time= pygame.time.get_ticks() - START_TIME_GAME
    current_time = current_time//1000
    return  current_time

def screen_backgrounds(Cont):
    i = 0
    for rect in rects_backgrounds:
        if Cont == 3:
            rect.y += 1
        if rect.y >= SCREEN_HEIGHT:
            rect.y = -1150
            index_backgrounds[i] = random.choice(range(0,3))
        screen.blit(backgrounds[index_backgrounds[i]], rect)
        i += 1

player = Player(SCREEN_WIDTH,SCREEN_HEIGHT)

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
                        START_TIME_GAME = pygame.time.get_ticks()
                        LEVEL = 1
                        LEVEL_CHANGES = 100
                        Score = 0
                        player.starting()
                    else:
                        LEVEL = 0
                #teclas especiales
                if event.key == pygame.K_4:
                    LEVEL = -2
                    LEVEL_CHANGES = 100
                if event.key == pygame.K_0:
                    LEVEL = -1
        else:
            player.chek_inputs(event)
            if event.type == pygame.KEYUP:
                # teclas especiales
                if event.key == pygame.K_1:
                    LEVEL = 1
                    LEVEL_CHANGES = 100
                if event.key == pygame.K_2:
                    LEVEL = 2
                    LEVEL_CHANGES = 100
                if event.key == pygame.K_3:
                    LEVEL = 3
                    LEVEL_CHANGES = 100
                if event.key == pygame.K_9:
                    Game_active = False

    # Scenes
    if Game_active == False:
        #start
        if LEVEL == 0:
            screen.fill('black')
            screen.blit(name_game_surf,name_game_rect)
            screen.blit(instructions_surf, instructions_rect)
            screen.blit(player_stand_surf, player_stand_rect)
            screen.blit(enemy_A_stand_surf, enemy_A_stand_rect)
            screen.blit(enemy_B_stand_surf, enemy_B_stand_rect)
            screen.blit(enemy_C_stand_surf, enemy_C_stand_rect)
        #game over
        elif LEVEL == -1:
            screen.fill('black')
            screen.blit(game_over_surf, game_over_rect)
            screen.blit(score_surf,  score_rect_final)
            screen.blit(instructions_2_surf,instructions_2_rect_game_over)
            screen.blit(player_game_over_surf, player_game_over_rect)
            screen.blit(level_surf,level_rect_game_over)
        #completed
        elif LEVEL == -2:
            screen.fill('black')
            screen.blit(score_surf,score_rect_final)
            screen.blit(completed_surf,completed_rect)
            screen.blit(instructions_2_surf, instructions_2_rect_completed)
            screen.blit(player_stand_surf, player_stand_rect)
            current_time = 0
        elif Score > 0:
            LEVEL = -1

    if Game_active == True:
        # events & changes
        if Cont == 3:
            Cont = 0
        else:
            Cont += 1
        screen_backgrounds(Cont)
        screen.blit(score_surf, score_rect)
        #level defined
        current_time = get_time(START_TIME_GAME)
        if current_time == 300:
            LEVEL = 2
            LEVEL_CHANGES = 100
        elif current_time == 600:
            LEVEL = 3
            LEVEL_CHANGES = 100
        elif current_time == 900:
            Game_active = False
            LEVEL = -2

        player.update(screen, bullet_enemie_rect)
        Game_active = player.colisions(bullet_enemie_rect, Game_active)

        #level 1
        if LEVEL == 1:
            if LEVEL_CHANGES > 0:
                LEVEL_CHANGES = level_changes(LEVEL_CHANGES)
            # Spawning
            pygame.draw.rect(screen, 'Red', (EJE_X_ALIEN1, EJE_Y_ALIEN1, ALIEN_RECT_WIDTH, ALIEN_RECT_HEIGHT), 25)
            pygame.draw.rect(screen, 'Purple', (EJE_X_ALIEN2, EJE_Y_ALIEN2, ALIEN_RECT_WIDTH, ALIEN_RECT_HEIGHT),25)
            pygame.draw.rect(screen, 'Blue', (EJE_X_ALIEN3, EJE_Y_ALIEN3, ALIEN_RECT_WIDTH, ALIEN_RECT_HEIGHT), 25)

            # Alien Movement
            EJE_X_ALIEN1 -= ALIEN_SPEED_MOVEMENT1
            EJE_X_ALIEN2 -= ALIEN_SPEED_MOVEMENT2
            EJE_X_ALIEN3 -= ALIEN_SPEED_MOVEMENT3
            if EJE_X_ALIEN1 <= SCREEN_WIDTH - 450 or EJE_X_ALIEN1 >= SCREEN_WIDTH - 50:
                ALIEN_SPEED_MOVEMENT1 *= -1
            if EJE_X_ALIEN2 <= SCREEN_WIDTH - 450 or EJE_X_ALIEN2 >= SCREEN_WIDTH - 50:
                ALIEN_SPEED_MOVEMENT2 *= -1
            if EJE_X_ALIEN3 <= SCREEN_WIDTH - 450 or EJE_X_ALIEN3 >= SCREEN_WIDTH - 50:
                ALIEN_SPEED_MOVEMENT3 *= -1

        #level 2
        elif LEVEL == 2:
            if LEVEL_CHANGES > 0:
                LEVEL_CHANGES = level_changes(LEVEL_CHANGES)

        #level 3
        elif LEVEL == 3:
            if LEVEL_CHANGES > 0:
                LEVEL_CHANGES = level_changes(LEVEL_CHANGES)

    pygame.display.update()
    clock.tick(60)
