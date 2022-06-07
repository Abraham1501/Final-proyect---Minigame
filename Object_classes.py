import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.EJE_X_PLAYER = SCREEN_WIDTH // 2
        self.EJE_Y_PLAYER = SCREEN_HEIGHT - 110
        self.EJE_X_PLAYER_STARTING = SCREEN_WIDTH // 2
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
        self.SPEED_MOVEMENT = 6
        #player
        player_surf = pygame.image.load('Game_project/Graphics/Player/player_1.png').convert_alpha()
        self.player_surf = player_surf
        self.player_rect = player_surf.get_rect(center=(self.EJE_X_PLAYER, self.EJE_Y_PLAYER))
        bullet_player_surf = pygame.image.load('Game_project/Graphics/Player/bullet_player_1.png').convert_alpha()
        self.bullet_player_surf = bullet_player_surf
        self.bullet_player_rect = self.bullet_player_surf.get_rect(center=(self.EJE_X_SHOOT, self.EJE_Y_SHOOT))

        self.bullets = []

        # sounds player
        sound_player = pygame.mixer.Sound('Game_project/Sounds/shoot_player_sound.mp3')
        self.sound_player = sound_player
        self.sound_player.set_volume(0.1)
        sound_died_player = pygame.mixer.Sound('Game_project/Sounds/died_player.mp3')
        self.sound_died_player = sound_died_player

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

    def __shoot_player(self, screen, bullet_enemie_rect):
        def move_bullets():
            for rect in self.bullets:
                rect.y -= self.SPEED_SHOOT
            rects = []
            for rect in self.bullets:
                if rect.y > 0:
                    if not rect.colliderect(bullet_enemie_rect):
                        rects.append(rect)
            return rects
        def screen_bullets():
            for rect in self.bullets:
                screen.blit(self.bullet_player_surf, rect)

        self.EJE_X_SHOOT = self.EJE_X_PLAYER
        if self.Shoot_time > 0:
            self.Shoot_time -= 1
        if self.Shoot and self.Shoot_time == 0:
            self.Shoot_time = self.SHOOT_TIME
            self.sound_player.play()
            self.bullets.append(self.bullet_player_surf.get_rect(center=(self.EJE_X_SHOOT, self.EJE_Y_SHOOT)))
        self.bullets = move_bullets()
        screen_bullets()

    def colisions(self, bullet_enemie_rect, Game_active):
        if self.player_rect.colliderect(bullet_enemie_rect):
            Game_active = False
            self.sound_died_player.play()
        return Game_active

    def starting(self):
        self.EJE_X_PLAYER = self.EJE_X_PLAYER_STARTING

    def update(self, screen, bullet_enemie_rect):
        self.__move()
        self.__player_screen(screen)
        self.__shoot_player(screen, bullet_enemie_rect)