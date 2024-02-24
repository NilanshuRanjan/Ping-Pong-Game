import pygame
import GameOver
from pygame import mixer
mixer.init()

# loading images
PLAYER1_img = pygame.image.load("Ping_Pong files/Player1_img.png")
PLAYER2_img = pygame.image.load("Ping_Pong files/Player2_img.png")
BALL_img = pygame.image.load("Ping_Pong files/Ball_img.png")
BG = pygame.image.load("Ping_Pong files/Background_1.png")

# defining all the variables
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 650
COLOUR = "#0FB60D"
FPS = 90
PLAYER1_x = 50
PLAYER1_y = 250
PLAYER2_x = 1130
PLAYER2_y = 250
PLAYER_VELOCITY = 6

BALL_x_VELOCITY = 9
BALL_y_VELOCITY = 3.3
BALL_x = 575
BALL_y = 275
start = False


def main():
    global SCREEN, start
    pygame.mixer.Channel(0).play(pygame.mixer.Sound("Ping_Pong files/BGMusic_2.mp3"))
    mixer.Channel(0).set_volume(0.3)
    # defining the screen
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Ping-Pong Game")
    clock = pygame.time.Clock()

    run = True
    while run:

        clock.tick(FPS)

        SCREEN.fill(COLOUR)
        SCREEN.blit(pygame.transform.scale(BG, (1200, 650)), (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # drawing objects on screen
        PLAYER1.drawing_player()
        PLAYER2.drawing_player()
        BALL.drawing()

        # Movement of the player
        PLAYER1.movement(PLAYER_VELOCITY)
        PLAYER2.AI()

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            start = True
        if start:
            BALL.movement()

        # Check everytime for winner
        BALL.check_win()

        pygame.display.update()

    pygame.quit()


class Players:

    def __init__(self, img, x_cords, y_cords):
        self.X = x_cords
        self.Y = y_cords
        self.img = pygame.transform.scale(img, (20, 100))

    def drawing_player(self):
        SCREEN.blit(self.img, (self.X, self.Y))

    def movement(self, velocity):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_w]:
            if self == PLAYER1:
                if self.Y > 0:
                    self.Y -= velocity
        if key_pressed[pygame.K_s]:
            if self == PLAYER1:
                if self.Y < SCREEN_HEIGHT - 100:
                    self.Y += velocity
        # if key_pressed[pygame.K_UP]:
        #     if self == PLAYER2:
        #         if self.Y > 0:
        #             self.Y -= velocity
        # if key_pressed[pygame.K_DOWN]:
        #     if self == PLAYER2:
        #         if self.Y < SCREEN_HEIGHT - 100:
        #             self.Y += velocity

    def AI(self):

        TIME_CAL = (1200 - (BALL.X + 70))/(BALL.x_vel)
        DES_YCORD = BALL.Y + (BALL_y_VELOCITY * TIME_CAL)
        # print(self.Y, TIME_CAL, DES_YCORD, BALL.Y)

        if DES_YCORD - 25 < self.Y:
            if self.Y > 0:
                self.Y -= PLAYER_VELOCITY
        elif DES_YCORD - 25 > self.Y:
            if self.Y < SCREEN_HEIGHT - 100:
                self.Y += PLAYER_VELOCITY


# Defining the instances of class players
PLAYER1 = Players(PLAYER1_img, PLAYER1_x, PLAYER1_y)
PLAYER2 = Players(PLAYER2_img, PLAYER2_x, PLAYER2_y)


class Ball:

    def __init__(self, img, x_cord, y_cord, x_vel, y_vel):
        self.X = x_cord
        self.Y = y_cord
        self.img = pygame.transform.scale(img, (20, 20))
        self.x_vel = x_vel
        self.y_vel = y_vel

    def drawing(self):
        SCREEN.blit(self.img, (self.X, self.Y))

    def collision(self):
        # Creating rectangles around the images
        PLAYER1_rect = pygame.Rect(PLAYER1.X, PLAYER1.Y, PLAYER1.img.get_width(), PLAYER1.img.get_height())
        PLAYER2_rect = pygame.Rect(PLAYER2.X, PLAYER2.Y, PLAYER2.img.get_width(), PLAYER2.img.get_height())
        BALL_rect = pygame.Rect(BALL.X, BALL.Y, BALL.img.get_width(), BALL.img.get_height())

        # collision to upper boundary and lower boundary
        if self.Y <= 0:
            pygame.mixer.Channel(1).play(pygame.mixer.Sound("Ping_Pong files/Ball_soundeffect_1.mp3"))
            self.y_vel = -self.y_vel
        if self.Y >= 625:
            pygame.mixer.Channel(1).play(pygame.mixer.Sound("Ping_Pong files/Ball_soundeffect_1.mp3"))
            self.y_vel = -self.y_vel

        # collision between player and ball
        if pygame.Rect.colliderect(BALL_rect, PLAYER1_rect) or pygame.Rect.colliderect(BALL_rect, PLAYER2_rect):
            pygame.mixer.Channel(1).play(pygame.mixer.Sound("Ping_Pong files/Ball_soundeffect_1.mp3"))
            self.x_vel = -self.x_vel

    def movement(self):
        self.collision()
        self.X += self.x_vel
        self.Y += self.y_vel

    def check_win(self):
        global PLAYER1_y, PLAYER2_y, BALL_x, BALL_y, start, run, PLAYER1, PLAYER2, BALL
        # checking for winner
        if self.X > 1175:
            PLAYER1_y = 250
            PLAYER2_y = 250
            BALL_x = 575
            BALL_y = 275
            PLAYER1 = Players(PLAYER1_img, PLAYER1_x, PLAYER1_y)
            PLAYER2 = Players(PLAYER2_img, PLAYER2_x, PLAYER2_y)
            BALL = Ball(BALL_img, BALL_x, BALL_y, BALL_x_VELOCITY, BALL_y_VELOCITY)
            start = False
            run = False
            GameOver.Play_again("Player1")
        elif self.X < 0:
            PLAYER1_y = 250
            PLAYER2_y = 250
            BALL_x = 575
            BALL_y = 275
            PLAYER1 = Players(PLAYER1_img, PLAYER1_x, PLAYER1_y)
            PLAYER2 = Players(PLAYER2_img, PLAYER2_x, PLAYER2_y)
            BALL = Ball(BALL_img, BALL_x, BALL_y, BALL_x_VELOCITY, BALL_y_VELOCITY)
            start = False
            run = False
            GameOver.Play_again("Player2")


# defining instances for ball class
BALL = Ball(BALL_img, BALL_x, BALL_y, BALL_x_VELOCITY, BALL_y_VELOCITY)

if __name__ == '__main__':
    main()
