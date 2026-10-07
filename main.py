import pygame

ball_gravity = 0.0

#game logic
def int_main():
    #do game stuff

    #draw commands
    pygame.draw.rect(screen, (255, 0, 0), (100, 100, 150, 80))       # filled rect
    pygame.draw.rect(screen, (0, 200, 0), (300, 100, 150, 80), 3)   # outlined rect
    pygame.draw.circle(screen, (0, 0, 255), (500, 150), 60)         # filled circle
    pygame.draw.line(screen, (255, 255, 0), (100, 300), (400, 400), 5)
    pygame.draw.polygon(screen, (255, 100, 0), [(400, 300), (500, 450), (300, 450)])  # triangle

    screen.blit(tpmg, (0, 0))
    #xinput
    for ev in pygame.event.get():

        # Keyboard
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_SPACE:
                print("Space pressed!")

        # Mouse
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if ev.button == 1:   # 1 = left click
                print(f"Clicked at {ev.pos}")
#########

pygame.init()
screen = pygame.display.set_mode((640, 480))
tpmg = pygame.image.load("logo.png").convert_alpha()
pygame.display.set_caption("My Window")

running = True
while running:
    # boilerplate code
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
    screen.fill((30,30,30)) 
    int_main()
    #end boilerplate code
    pygame.display.flip()
pygame.quit()