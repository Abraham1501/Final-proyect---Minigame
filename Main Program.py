import pygame
from sys import exit
import random
from Object_classes import Player, alien
#from Alien_Class import alien

pygame.init()

# Variables
# Levels & game
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 650
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

#Alien
EJE_1_X_ALIEN1 = -15
EJE_2_X_ALIEN1 = 515
EJE_Y_ALIEN1 = SCREEN_HEIGHT - 375
EJE_Y_ALIEN2 = SCREEN_HEIGHT - 465
EJE_Y_ALIEN3 = SCREEN_HEIGHT - 555

ALIEN_SPEED1 = 2.5
ALIEN_SPEED2 = 1.5
ALIEN_SPEED3 = 0.5

ALIEN_ALIVE = True

score_surf = font.render(f'Score: {Score}', False, 'White')
score_rect = score_surf.get_rect(midtop = (85, 25))

alien_shoot_x = EJE_1_X_ALIEN1
alien_shoot_y = EJE_Y_ALIEN1

bullet_enemie_rect = pygame.Rect(alien_shoot_x, alien_shoot_y, 10,10)

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
enemy_A_stand_surf = pygame.image.load('Game_project/Graphics/Enemies/Enemies A/enemie_A_1.png').convert_alpha()
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

def player_bullet_hit(bullet_player,alien_rect):
    if bullet_player.colliderect(alien_rect):
        print("hit")

player = Player(SCREEN_WIDTH,SCREEN_HEIGHT,ALIEN_ALIVE)
Alien1 = alien('A', EJE_1_X_ALIEN1, EJE_2_X_ALIEN1, EJE_Y_ALIEN1, SCREEN_WIDTH, SCREEN_HEIGHT,3,ALIEN_ALIVE)
Alien2 = alien('B', EJE_1_X_ALIEN1, EJE_2_X_ALIEN1, EJE_Y_ALIEN2, SCREEN_WIDTH, SCREEN_HEIGHT,2,ALIEN_ALIVE)
Alien3 = alien('C', EJE_1_X_ALIEN1, EJE_2_X_ALIEN1, EJE_Y_ALIEN3, SCREEN_WIDTH, SCREEN_HEIGHT,1,ALIEN_ALIVE)

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

        player.update(screen, bullet_enemie_rect, Alien1.alien_rect_left, Alien1.alien_rect_right, Alien2.alien_rect_left, Alien2.alien_rect_right, Alien3.alien_rect_left, Alien3.alien_rect_right)
        Alien1.alien_update(screen,player.player_rect)
        Alien2.alien_update(screen,player.player_rect)
        Alien3.alien_update(screen,player.player_rect)
        #player_bullet_hit(player.bullet_player_rect,player.player_rect)

        #level 1
        if LEVEL == 1:
            if LEVEL_CHANGES > 0:
                LEVEL_CHANGES = level_changes(LEVEL_CHANGES)
            
            #player.colisions()
            if ALIEN_ALIVE == True:
                Alien1.choose_spawn(screen,player.player_rect)
                Alien2.choose_spawn(screen,player.player_rect)
                Alien3.choose_spawn(screen,player.player_rect)

            #if abs(player.bullet_player_rect.bottom - Alien1.alien_rect_left.top) <= 10:
            #    print("hit")
            #    Alien1.kill()
            #if abs(player.bullet_player_rect.bottom - Alien1.alien_rect_right.top) <= 10:
            #    print("hit")
            #    Alien1.kill()
            #if player.bullet_player_rect.x == Alien1.alien_rect_left.x:
            #    print("hit")
            #    Alien1.kill()
            #if player.bullet_player_rect.x == Alien1.alien_rect_right.x:
            #    print("hit")
            #    Alien1.kill()
                
                #    player_shot_hit(ALIEN1_RECT_Left)
                #    ALIEN_ALIVE = False
                #    if ALIEN_RESPAWN_COOLDOWN > 0:
                #        ALIEN_RESPAWN_COOLDOWN -= 1
                #    if ALIEN_RESPAWN_COOLDOWN == 0:
                #        ALIEN_ALIVE = True 
                #        ALIEN_RESPAWN_COOLDOWN = 30

                #    player_shot_hit(ALIEN1_RECT_Right)
                #    ALIEN_ALIVE = False
                #    if ALIEN_RESPAWN_COOLDOWN > 0:
                #        ALIEN_RESPAWN_COOLDOWN -= 1
                #    if ALIEN_RESPAWN_COOLDOWN == 0:
                #        ALIEN_ALIVE = True 
                #        ALIEN_RESPAWN_COOLDOWN = 30

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