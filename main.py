import sys, pygame
from body import Body

pygame.init()

size = width, height = 920, 680
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
balls = []

print ("Hi")

last_ball_done = True

while 1:
    pygame.time.delay(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    if(pygame.mouse.get_pressed()[0] and last_ball_done): 
        ball = Body( pygame.mouse.get_pos(),5,screen )
        balls.append(ball)
        last_ball_done = False
    
    if(pygame.mouse.get_pressed()[0]):
        ball.enlarge()

    if(not (pygame.mouse.get_pressed()[0] or last_ball_done)): 
        ball.finish()
        last_ball_done = True


    screen.fill(black)
    
    for ball in balls:
        ball.draw()

    pygame.display.flip()