import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500)) #Height and the Width of the window
screen.fill("white")

pygame.display.set_caption("Drawing Shapes on the Surface")

pygame.draw.line(screen, "black", (0, 0), (300, 300), 5)

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #it run when the user click the X btn on top
            done == False

    pygame.display.flip()