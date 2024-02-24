import PingPongGame_AI
import pygame


def Play_again(winner):
    PingPongGame_AI.pygame.mixer.Channel(0).stop()
    pygame.init()

    # Printing the name of the winner
    print(f"{winner} won the match, yoohoo")

    display = pygame.display.set_mode((1200, 650))
    Again_BUT = pygame.transform.scale(pygame.image.load("Ping_Pong files/PlayAgain.jpg"), (1200, 650))

    Play = True
    while Play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        display.blit(Again_BUT, (0, 0))
        Again_BUT_RECT = pygame.Rect(355, 473, 500, 45)
        Exit_RECT = pygame.Rect(494, 527, 224, 45)
        if pygame.Rect.collidepoint(Again_BUT_RECT, pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == 1:
                Play = False
                PingPongGame_AI.main()
        if pygame.Rect.collidepoint(Exit_RECT, pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == 1:
                quit()
        pygame.display.update()

    pygame.quit()
