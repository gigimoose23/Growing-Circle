import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((500,500))



pygame.display.update()
class Circle():
    def __init__(self, pos, radius, color, width):
        self.pos = pos
        self.radius = radius
        self.color = color
        self.surface = screen
        self.width = width
    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.pos, self.radius, self.width)

    def grow(self, interval):
        self.radius += interval
        self.draw()
screen.fill("skyblue")
growthCircle = Circle((250,250), 5, "darkred", 0)
growthCircle.draw()
growthCircle.grow(2)

while True:
    pygame.display.update()
    for i in pygame.event.get():
        if i.type == pygame.MOUSEBUTTONDOWN:
            screen.fill("skyblue")
            growthCircle.draw()
            growthCircle.grow(2)

        if i.type == pygame.QUIT: 
            sys.exit(0)










