import pygame

pygame.init()

#Created the screen/canvas to diplasy the things. 
screen = pygame.display.set_mode((500, 500)) #Height and the Width of the window
screen.fill("white")

#The caption for the window
pygame.display.set_caption("Drawing Shapes on the Surface")

# Creating the shapes using pygame library
pygame.draw.line(screen, "black", (0, 0), (300, 300), 5)
pygame.draw.lines(screen, "red", True, [(100, 100), (200, 100), (100, 200)], 4)
pygame.draw.rect(screen, "blue", (50, 50, 100, 100), 7)

#Loop for the closing of the window
done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #it run when the user click the X btn on top
            done == False

    pygame.display.flip()