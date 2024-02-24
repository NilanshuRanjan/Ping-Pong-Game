import PingPongGame_AI
import pygame

pygame.init()

display = pygame.display.set_mode((1200, 650))
START_BUT = pygame.transform.scale(pygame.image.load("Ping_Pong files/start_button.jpg"), (1200, 650))

Play = True
while Play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Play = False
    display.blit(START_BUT, (0, 0))
    START_BUT_RECT = pygame.Rect(280, 265, 659, 103)
    if pygame.Rect.collidepoint(START_BUT_RECT, pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0] == 1:
            RUN = False
            PingPongGame_AI.main()
    pygame.display.update()

pygame.quit()
