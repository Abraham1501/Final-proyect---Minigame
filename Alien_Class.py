import pygame
import random

class alien(pygame.sprite.Sprite):
    def __init__(self, alien, EJE_X_1, EJE_X_2, EJE_Y_ALIEN1, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()

        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.EJE_1_X_ALIEN1= EJE_X_1
        self.EJE_2_X_ALIEN1 = EJE_X_2
        self.EJE_Y_ALIEN1 = EJE_Y_ALIEN1
        file_path = 'Game_project\Graphics\Enemies\Enemies '+alien+'\enemies_'+alien+'_ 1.png'
        self.alien_surf1 = pygame.image.load(file_path).convert_alpha()
        self.alien_rect_left = self.alien_surf1.get_rect(center=(self.EJE_1_X_ALIEN1,self.EJE_Y_ALIEN1))
        self.alien_rect_right = self.alien_surf1.get_rect(center=(self.EJE_2_X_ALIEN1,self.EJE_Y_ALIEN1))
        
        self.ALIEN_SPEED_MOVEMENT1 = 3
        self.ALIEN_ALIVE = True
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
        self.ALIEN_SHOOT_TIME = 50
        self.alien_shoot_time = self.ALIEN_SHOOT_TIME
        self.ALIEN_SPEED_SHOT = 5

    def choose_spawn(self,screen):
        if self.random_spawn1_side == self.ALIEN_SPAWN_LEFT:
            self.alien_rect_left.x -= self.ALIEN_SPEED_MOVEMENT1
            screen.blit(self.alien_surf1,self.alien_rect_left)
            if self.alien_rect_left.left <= self.SCREEN_WIDTH - 560 or self.alien_rect_left.right >= self.SCREEN_WIDTH + 60:
                self.ALIEN_SPEED_MOVEMENT1 *= -1
                return self.ALIEN_SPEED_MOVEMENT1
            self.__alien_shooting()
            self.__draw_alien_bullets(screen)
            self.__move_alien_bullets(self.alien_rect_left)

        if self.random_spawn1_side == self.ALIEN_SPAWN_RIGHT:
            self.alien_rect_right.x -= self.ALIEN_SPEED_MOVEMENT1
            screen.blit(self.alien_surf1,self.alien_rect_right)
            if self.alien_rect_right.left <= self.SCREEN_WIDTH - 560 or self.alien_rect_right.right >= self.SCREEN_WIDTH + 60:
                self.ALIEN_SPEED_MOVEMENT1 *= -1
                return self.ALIEN_SPEED_MOVEMENT1
            self.__alien_shooting()
            self.__draw_alien_bullets(screen)
            self.__move_alien_bullets(self.alien_rect_right)

        return self.alien_rect_left, self.alien_rect_right

    def __alien_shooting(self):
        for alien_bullets in self.bullet1:
            alien_bullets.y += self.ALIEN_SPEED_SHOT

    def __draw_alien_bullets(self,screen):
        for alien_bullets in self.bullet1:
            screen.blit(self.bullet_enemie_surf,alien_bullets)
            if alien_bullets.y > self.SCREEN_HEIGHT:
                self.bullet1.remove(alien_bullets)

    def __move_alien_bullets(self,alien_rect):
        if self.alien_shoot_time > 0:
            self.alien_shoot_time -= 1
        if self.alien_shoot_time == 0:
            alien_bullets = pygame.Rect(alien_rect.centerx, alien_rect.centery, 10,10)
            self.bullet1.append(alien_bullets)
            self.alien_shoot_time = self.ALIEN_SHOOT_TIME
        return self.alien_shoot_time

    def alien_update(self,screen):
        self.choose_spawn(screen)