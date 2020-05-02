import sys, pygame
import itertools
from body import Body

pygame.init()

base_ball_size = 1
size = width, height = 1220, 880
speed = [2, 2]
black = 0, 0, 0
G = 5 * (10**(-3))

screen = pygame.display.set_mode(size)
balls = []

print ("Hi")

last_ball_done = True

def add_forces(body1,body2):
        dx = body2.position[0] - body1.position[0]
        dy = body2.position[1] - body1.position[1]
        r_squared = dx*dx + dy*dy
        r = r_squared**0.5
        force_magnitude = (G * body1.mass * body2.mass) / r_squared #F=G*M1*M2/(r^2)
        dx_normalized_scaled = (dx / r) * force_magnitude
        dy_normalized_scaled = (dy / r) * force_magnitude
        body1.forces = (body1.forces[0] + dx_normalized_scaled, body1.forces[1] + dy_normalized_scaled)
        body2.forces = (body2.forces[0] - dx_normalized_scaled, body2.forces[1] - dy_normalized_scaled)

def collisions(bodies):
    list_to_check = list(itertools.combinations(bodies, 2))
    for pair in list_to_check:

        add_forces(pair[0],pair[1])

        if (pair[0].collision(pair[1])):
            ball = Body( pygame.mouse.get_pos(),base_ball_size,screen )
            ball.collided_body(pair[0],pair[1])
            bodies.append(ball)
            bodies.remove(pair[0])
            bodies.remove(pair[1])
            

while 1:
    pygame.time.delay(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    if(pygame.mouse.get_pressed()[0] and last_ball_done): 
        ball = Body( pygame.mouse.get_pos(),base_ball_size,screen )
        balls.append(ball)
        last_ball_done = False
    
    if(pygame.mouse.get_pressed()[0]):
        ball.enlarge()

    if(not (pygame.mouse.get_pressed()[0] or last_ball_done)): 
        ball.finish(pygame.mouse.get_pos())
        last_ball_done = True


    screen.fill(black)
    collisions(balls)
    for ball in balls:
        print(ball.forces)
        if (ball.done):
            ball.move()
        ball.draw()

    pygame.display.flip()