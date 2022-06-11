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

        # player shoot
        self.Shoot = False
        self.EJE_X_SHOOT = self.EJE_X_PLAYER
        self.EJE_Y_SHOOT = self.EJE_Y_PLAYER
        self.SHOOT_TIME = 20
        self.Shoot_time = self.SHOOT_TIME
        self.SPEED_SHOOT = 15

        # player move
        self.Move_left = False
        self.Move_right = False
        self.SPEED_MOVEMENT = 5

        # player
        player_surf = pygame.image.load('Game_project/Graphics/Player/player_1.png').convert_alpha()
        self.player_surf = player_surf
        self.player_rect = player_surf.get_rect(center=(self.EJE_X_PLAYER, self.EJE_Y_PLAYER))

        bullet_player_surf = pygame.image.load('Game_project/Graphics/Player/bullet_player_1.png').convert_alpha()
        self.bullet_player_surf = bullet_player_surf
        self.bullet_player_rect = self.bullet_player_surf.get_rect(center=(self.EJE_X_SHOOT, self.EJE_Y_SHOOT))
        self.bullets = []

        #sounds player
        sound_player = pygame.mixer.Sound('Game_project/Sounds/shoot_player_sound.mp3')
        self.sound_player = sound_player
        self.sound_player.set_volume(0.1)
        sound_died_player = pygame.mixer.Sound('Game_project/Sounds/died_player.mp3')
        self.sound_died_player = sound_died_player
        self.sound_died_player.set_volume(0.1)

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

    def __player_screen(self, screen):
        self.player_rect = self.player_surf.get_rect(center=(self.EJE_X_PLAYER, self.EJE_Y_PLAYER))
        screen.blit(self.player_surf, self.player_rect)

    def __shoot_player(self, screen):
        def screen_bullets():
            for rect in self.bullets:
                screen.blit(self.bullet_player_surf, rect)
        def move_bullets():
            for rect in self.bullets:
                rect.y -= self.SPEED_SHOOT
            rects = []
            for rect in self.bullets:
                if rect.y > 0:
                    rects.append(rect)
            return rects

        self.EJE_X_SHOOT = self.EJE_X_PLAYER
        if self.Shoot_time > 0:
            self.Shoot_time -= 1
        if self.Shoot and self.Shoot_time == 0:
            self.Shoot_time = self.SHOOT_TIME
            self.sound_player.play()
            self.bullets.append(self.bullet_player_surf.get_rect(center=(self.EJE_X_SHOOT, self.EJE_Y_SHOOT)))
        self.bullets = move_bullets()
        screen_bullets()
        return self.ALIEN_ALIVE

    def starting(self):
        self.EJE_X_PLAYER = self.EJE_X_PLAYER_STARTING
        for rect in self.bullets:
            self.bullets.remove(rect)
        self.Move_left = False
        self.Move_right = False

    def update(self, screen, bullet_enemie_rect):
        self.__move()
        self.__player_screen(screen)
        self.__shoot_player(screen)


class alien(pygame.sprite.Sprite):
    def __init__(self, alien, EJE_X_1, EJE_X_2, EJE_Y_ALIEN1, SCREEN_WIDTH, SCREEN_HEIGHT, ALIEN_SPEED, ALIEN_ALIVE):
        super().__init__()

        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.EJE_1_X_ALIEN1 = EJE_X_1
        self.EJE_2_X_ALIEN1 = EJE_X_2
        self.Ejes_X_aliens = [self.EJE_1_X_ALIEN1, self.EJE_2_X_ALIEN1]
        self.EJE_Y_ALIEN1 = EJE_Y_ALIEN1
        file_path = 'Game_project/Graphics/Enemies/Enemies ' + alien + '/enemie_' + alien + '_1.png'
        alien_surf = pygame.image.load(file_path).convert_alpha()
        self.alien_surf1 = alien_surf

        self.ALIEN_SPEED_MOVEMENT1 = ALIEN_SPEED
        self.ALIEN_ALIVE = ALIEN_ALIVE
        self.ALIEN_RESPAWN_COOLDOWN = 30

        # Alien Spawn
        self.random_spawn1_side = random.choice(self.Ejes_X_aliens)
        self.alien_rect = alien_surf.get_rect(center=(self.random_spawn1_side, self.EJE_Y_ALIEN1))
        sound_shoot_alien = pygame.mixer.Sound('Game_project/Sounds/shoott_alien.mp3')
        self.sound_shoot_alien = sound_shoot_alien
        self.sound_shoot_alien.set_volume(0.1)
        sound_died_alien = pygame.mixer.Sound('Game_project/Sounds/died_alien.mp3')
        self.sound_died_alien = sound_died_alien
        self.sound_died_alien.set_volume(0.1)

        # Alien Shooting
        self.shooting_positions = [50, 125, 200, 250, 300, 375, 450]
        self.bullet_enemie_surf = pygame.image.load('Game_project/Graphics/Enemies/bullet_enemies.png').convert_alpha()
        self.bullet1 = []
        self.ALIEN_SHOOT_TIME = 100
        self.alien_shoot_time = self.ALIEN_SHOOT_TIME
        self.ALIEN_SPEED_SHOT = 4

    def choose_spawn(self, screen):
        self.alien_rect.x += self.ALIEN_SPEED_MOVEMENT1
        screen.blit(self.alien_surf1, self.alien_rect)
        self.__alien_movement(self.alien_rect)

    def __alien_shooting(self):
        for alien_bullets in self.bullet1:
            alien_bullets.y += self.ALIEN_SPEED_SHOT

    def __draw_alien_bullets(self, screen):
        for alien_bullets in self.bullet1:
            screen.blit(self.bullet_enemie_surf, alien_bullets)
            if alien_bullets.y > self.SCREEN_HEIGHT:
                self.bullet1.remove(alien_bullets)

    def __move_alien_bullets(self, alien_rect):
        if self.alien_shoot_time > 0:
            self.alien_shoot_time -= 1
        if self.alien_shoot_time == 0:
            alien_bullets = pygame.Rect(alien_rect.centerx, alien_rect.centery, 10, 10)
            self.bullet1.append(alien_bullets)
            self.sound_shoot_alien.play()
            self.alien_shoot_time = self.ALIEN_SHOOT_TIME

    def __alien_movement(self, alien_rect):
        if alien_rect.left <= self.SCREEN_WIDTH - 560 or alien_rect.right >= self.SCREEN_WIDTH + 60:
            self.ALIEN_SPEED_MOVEMENT1 *= -1

    def collisions_aliens_bullets(self, player_rect, Game_active):
        for alien_bullets in self.bullet1:
            if alien_bullets.colliderect(player_rect):
                self.bullet1.remove(alien_bullets)
                Game_active = False
                self.ALIEN_ALIVE = False
                break
            else:
                if not Game_active == False:
                    Game_active = True
        return Game_active

    def collisions_alien(self, bullets, Score):
        for rect in bullets:
            if self.alien_rect.colliderect(rect):
                self.ALIEN_ALIVE = False
                self.spawing()
                self.sound_died_alien.play()
                bullets.remove(rect)
                Score += 100
        return Score

    def spawing(self,):
        ALIEN_SPEED1 = 3
        ALIEN_SPEED2 = 2
        ALIEN_SPEED3 = 1
        Aliens_speeds = [ALIEN_SPEED1, ALIEN_SPEED2, ALIEN_SPEED3]
        self.ALIEN_SPEED_MOVEMENT1 = random.choice(Aliens_speeds)
        Aliens_letters = ['A', 'B', 'C']
        alien = random.choice(Aliens_letters)
        file_path = 'Game_project/Graphics/Enemies/Enemies ' + alien + '/enemie_' + alien + '_1.png'
        alien_surf = pygame.image.load(file_path).convert_alpha()
        self.alien_surf1 = alien_surf
        self.alien_rect = alien_surf.get_rect(center=(self.random_spawn1_side, self.EJE_Y_ALIEN1))

    def reset(self):
        for rect in self.bullet1:
            self.bullet1.remove(rect)


    def alien_update(self, screen):
        self.__alien_shooting()
        self.__draw_alien_bullets(screen)
        self.__move_alien_bullets(self.alien_rect)
        if self.ALIEN_ALIVE == True:
            self.choose_spawn(screen)
        elif self.ALIEN_ALIVE == False:
            if self.ALIEN_RESPAWN_COOLDOWN > 0:
                self.ALIEN_RESPAWN_COOLDOWN -= 1
            if self.ALIEN_RESPAWN_COOLDOWN == 0:
                self.ALIEN_ALIVE = True
                for rect in self.bullet1:
                    self.bullet1.remove(rect)
                self.ALIEN_RESPAWN_COOLDOWN = 200