import pygame
import random

class Player(pygame.sprite.Sprite):

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, ALIEN_ALIVE):
        super().__init__()
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.EJE_X_PLAYER = SCREEN_WIDTH // 2
        self.EJE_Y_PLAYER = SCREEN_HEIGHT - 110
        self.EJE_X_PLAYER_STARTING = SCREEN_WIDTH // 2

        self.ALIEN_ALIVE = ALIEN_ALIVE

        #player shoot
        self.Shoot = False
        self.EJE_X_SHOOT = self.EJE_X_PLAYER
        self.EJE_Y_SHOOT = self.EJE_Y_PLAYER
        self.SHOOT_TIME = 20
        self.Shoot_time = self.SHOOT_TIME
        self.SPEED_SHOOT = 15

        #player move
        self.Move_left = False
        self.Move_right = False
        self.SPEED_MOVEMENT = 5

        #player
        player_surf = pygame.image.load('Game_project/Graphics/Player/player_1.png').convert_alpha()
        self.player_surf = player_surf
        self.player_rect = player_surf.get_rect(center=(self.EJE_X_PLAYER, self.EJE_Y_PLAYER))

        bullet_player_surf = pygame.image.load('Game_project/Graphics/Player/bullet_player_1.png').convert_alpha()
        self.bullet_player_surf = bullet_player_surf
        self.bullet_player_rect = self.bullet_player_surf.get_rect(center=(self.EJE_X_SHOOT, self.EJE_Y_SHOOT))
        self.bullets = []

        # sounds player
        #sound_player = pygame.mixer.Sound('Game_project/Sounds/shoot_player_sound.mp3')
        #self.sound_player = sound_player
        #self.sound_player.set_volume(0.1)
        #sound_died_player = pygame.mixer.Sound('Game_project/Sounds/died_player.mp3')
        #self.sound_died_player = sound_died_player

    def chek_inputs(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and self.Shoot == False:
                self.Shoot = True
            if event.key == pygame.K_a:
                self.Move_left = True
            if event.key == pygame.K_d:
                self.Move_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.Move_left = False
            if event.key == pygame.K_d:
                self.Move_right = False
            if event.key == pygame.K_SPACE and self.Shoot == True:
                self.Shoot = False

    def __move(self):
        if self.EJE_X_PLAYER > 0 and self.EJE_X_PLAYER < self.SCREEN_WIDTH:
            if self.Move_right == True:
                self.EJE_X_PLAYER += self.SPEED_MOVEMENT
            elif self.Move_left == True:
                self.EJE_X_PLAYER -= self.SPEED_MOVEMENT
        else:
            if self.EJE_X_PLAYER <= 0:
                self.EJE_X_PLAYER += self.SPEED_MOVEMENT
            else:
                self.EJE_X_PLAYER -= self.SPEED_MOVEMENT

    def __player_screen(self,screen):
        self.player_rect = self.player_surf.get_rect(center=(self.EJE_X_PLAYER, self.EJE_Y_PLAYER))
        screen.blit(self.player_surf, self.player_rect)

    def __shoot_player(self, screen, bullet_enemie_rect,alien1_rect_left,alien1_rect_right,alien2_rect_left,alien2_rect_right,alien3_rect_left,alien3_rect_right):
        def move_bullets():
            for rect in self.bullets:
                rect.y -= self.SPEED_SHOOT
            rects = []
            for rect in self.bullets:
                if rect.y > 0:
                    if not rect.colliderect(bullet_enemie_rect):
                        rects.append(rect)
            return rects
        def screen_bullets(alien1_rect_left,alien1_rect_right,alien2_rect_left,alien2_rect_right,alien3_rect_left,alien3_rect_right):
            for rect in self.bullets:
                screen.blit(self.bullet_player_surf, rect)
                if rect.colliderect(alien1_rect_left):
                    self.ALIEN_ALIVE = False
                    print("hit")
                    self.bullets.remove(rect)
                if rect.colliderect(alien1_rect_right):
                    self.ALIEN_ALIVE = False
                    print("hit")
                    self.bullets.remove(rect)
                if rect.colliderect(alien2_rect_left):
                    self.ALIEN_ALIVE = False
                    print("hit")
                    self.bullets.remove(rect)
                if rect.colliderect(alien2_rect_right):
                    self.ALIEN_ALIVE = False
                    print("hit")
                    self.bullets.remove(rect)
                if rect.colliderect(alien3_rect_left):
                    self.ALIEN_ALIVE = False
                    print("hit")
                    self.bullets.remove(rect)
                if rect.colliderect(alien3_rect_right):
                    self.ALIEN_ALIVE = False
                    print("hit")
                    self.bullets.remove(rect)
        self.EJE_X_SHOOT = self.EJE_X_PLAYER
        if self.Shoot_time > 0:
            self.Shoot_time -= 1
        if self.Shoot and self.Shoot_time == 0:
            self.Shoot_time = self.SHOOT_TIME
            #self.sound_player.play()
            self.bullets.append(self.bullet_player_surf.get_rect(center=(self.EJE_X_SHOOT, self.EJE_Y_SHOOT)))
        self.bullets = move_bullets()
        screen_bullets(alien1_rect_left,alien1_rect_right,alien2_rect_left,alien2_rect_right,alien3_rect_left,alien3_rect_right)
        return self.ALIEN_ALIVE

    def starting(self):
        self.EJE_X_PLAYER = self.EJE_X_PLAYER_STARTING

    def update(self, screen, bullet_enemie_rect,alien1_rect_left,alien1_rect_right,alien2_rect_left,alien2_rect_right,alien3_rect_left,alien3_rect_right):
        self.__move()
        self.__player_screen(screen)
        self.__shoot_player(screen, bullet_enemie_rect,alien1_rect_left,alien1_rect_right,alien2_rect_left,alien2_rect_right,alien3_rect_left,alien3_rect_right)

class alien(pygame.sprite.Sprite):
    def __init__(self, alien, EJE_X_1, EJE_X_2, EJE_Y_ALIEN1, SCREEN_WIDTH, SCREEN_HEIGHT, ALIEN_SPEED, ALIEN_ALIVE):
        super().__init__()

        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.EJE_1_X_ALIEN1 = EJE_X_1
        self.EJE_2_X_ALIEN1 = EJE_X_2
        self.EJE_Y_ALIEN1 = EJE_Y_ALIEN1
        file_path = 'Game_project/Graphics/Enemies/Enemies '+alien+'/enemie_'+alien+'_1.png'
        self.alien_surf1 = pygame.image.load(file_path).convert_alpha()
        self.alien_rect_left = self.alien_surf1.get_rect(center=(self.EJE_1_X_ALIEN1,self.EJE_Y_ALIEN1))
        self.alien_rect_right = self.alien_surf1.get_rect(center=(self.EJE_2_X_ALIEN1,self.EJE_Y_ALIEN1))
        
        self.ALIEN_SPEED_MOVEMENT1 = ALIEN_SPEED
        self.ALIEN_ALIVE = ALIEN_ALIVE
        self.ALIEN_RESPAWN_COOLDOWN = 30

        #Alien Spawn
        self.ALIEN_SPAWN_RIGHT = 1
        self.ALIEN_SPAWN_LEFT = 2
        self.SPAWN_SIDE = [self.ALIEN_SPAWN_LEFT,self.ALIEN_SPAWN_RIGHT]
        self.random_spawn1_side = random.choice(self.SPAWN_SIDE)

        #Alien Shooting
        self.shooting_positions = [50,125,200,250,300,375,450]
        self.bullet_enemie_surf = pygame.image.load('Game_project/Graphics/Enemies/bullet_enemies.png').convert_alpha()
        self.bullet1 = []
        self.ALIEN_SHOOT_TIME = 100
        self.alien_shoot_time = self.ALIEN_SHOOT_TIME
        self.ALIEN_SPEED_SHOT = 4

    def choose_spawn(self,screen,player_rect):
        if self.ALIEN_ALIVE == True:
            if self.random_spawn1_side == self.ALIEN_SPAWN_LEFT:
                self.alien_rect_left.x += self.ALIEN_SPEED_MOVEMENT1
                screen.blit(self.alien_surf1,self.alien_rect_left)
                self.__alien_movement(self.alien_rect_left)
                self.__alien_shooting()
                self.__draw_alien_bullets(screen,player_rect)
                self.__move_alien_bullets(self.alien_rect_left)
            if self.random_spawn1_side == self.ALIEN_SPAWN_RIGHT:
                self.alien_rect_right.x -= self.ALIEN_SPEED_MOVEMENT1
                screen.blit(self.alien_surf1,self.alien_rect_right)
                self.__alien_movement(self.alien_rect_right)
                self.__alien_shooting()
                self.__draw_alien_bullets(screen,player_rect)
                self.__move_alien_bullets(self.alien_rect_right)
            return self.alien_rect_left, self.alien_rect_right, self.ALIEN_SPEED_MOVEMENT1
        elif self.ALIEN_ALIVE == False:
            if self.ALIEN_RESPAWN_COOLDOWN > 0:
                self.ALIEN_RESPAWN_COOLDOWN -= 1
            if self.ALIEN_RESPAWN_COOLDOWN == 0:
                self.ALIEN_ALIVE = True 
                self.ALIEN_RESPAWN_COOLDOWN = 30
        return self.ALIEN_ALIVE

    def __alien_shooting(self):
        for alien_bullets in self.bullet1:
            alien_bullets.y += self.ALIEN_SPEED_SHOT

    def __draw_alien_bullets(self,screen,player_rect):
        for alien_bullets in self.bullet1:
            screen.blit(self.bullet_enemie_surf,alien_bullets)
            if alien_bullets.y > self.SCREEN_HEIGHT:
                self.bullet1.remove(alien_bullets)
            if alien_bullets.colliderect(player_rect):
                print("hit")
                self.bullet1.remove(alien_bullets)

    def __move_alien_bullets(self, alien_rect):
        if self.alien_shoot_time > 0:
            self.alien_shoot_time -= 1
        if self.alien_shoot_time == 0:
            alien_bullets = pygame.Rect(alien_rect.centerx, alien_rect.centery, 10,10)
            self.bullet1.append(alien_bullets)
            self.alien_shoot_time = self.ALIEN_SHOOT_TIME
        return self.alien_shoot_time

    def __alien_movement(self,alien_rect):
        if alien_rect.left <= self.SCREEN_WIDTH - 560 or alien_rect.right >= self.SCREEN_WIDTH + 60:
            self.ALIEN_SPEED_MOVEMENT1 *= -1

    def alien_update(self,screen,player_rect):
        self.choose_spawn(screen,player_rect)