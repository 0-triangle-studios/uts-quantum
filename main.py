import pygame
import time
running = True

def INC(x, max, mult):
    return x + mult if x < max else 1

ball_gravity = 0.0
IDLE_index = 1
IDLE_max = 5

BALL_frame = 0

#game logic
def int_main():
    #do game stuff
    global IDLE_index
    global BALL_frame
    tpmg = pygame.image.load("IDLE_" + str(IDLE_index) + ".jpg").convert_alpha()
    IDLE_index = INC(IDLE_index, IDLE_max, 1)

    #draw commands
    screen.blit(tpmg, (0, 0))
    pygame.draw.circle(screen, (0, 255, 255), (400, 300), BALL_frame)

    BALL_frame = INC(BALL_frame, 30, 3)
    

    #xinput
    for ev in pygame.event.get():

        # Keyboard
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_SPACE:
                print("Space pressed!")
            if ev.key == pygame.K_TAB:
                running = False
        # Mouse
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if ev.button == 1:   # 1 = left click
                print(f"Clicked at {ev.pos}")
#########

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My Window")

while running:
    # boilerplate code
    time.sleep(0.125)
    print(running)
    screen.fill((30,30,30)) 
    int_main()
    #end boilerplate code
    pygame.display.flip()
pygame.quit()