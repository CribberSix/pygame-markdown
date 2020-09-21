import pygame
from pygamemarkdown import *

# minimal pygame setup
pygame.init()
screenHeight = 600
screenWidth = 900
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Pygame")
pygame.display.get_surface().fill((200, 200, 200))  # background coloring

# parameters
screen = pygame.display.get_surface()  # get existing pygame window/screen
offset_X = 50  # offset from the left border of the pygame window
offset_Y = 100  # offset from the top border of the pygame window
textAreaHeight = 500
textAreaWidth = 800

with open("README.md", "r") as f:
    text_list = list(f)

# instantiation
md_blitter = MarkdownBlitter(screen, text_list, offset_X, offset_Y,
                             textAreaWidth, textAreaHeight)

f = True
# TextEditor in the pygame-loop
while True:
    # INPUT - Mouse + Keyboard
    for event in pygame.event.get():  # handle QUIT operation
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if f:
        md_blitter.display()  # Logic
        f = False

    pygame.display.flip()  # updates pygame window
