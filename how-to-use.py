import pygame
from src.pygamemarkdown import MarkdownRenderer

# minimal pygame setup
pygame.init()
screenHeight = 600
screenWidth = 900
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Pygame")
pygame.display.get_surface().fill((200, 200, 200))  # background coloring

# parameters
surface = pygame.display.get_surface()  # get existing pygame window/screen
offset_X = 50  # offset from the left border of the pygame window
offset_Y = 20  # offset from the top border of the pygame window
textAreaHeight = 500
textAreaWidth = 800
mdfile_path = "README_test.mdwe"

# Setup MD-Renderer
md_blitter = MarkdownRenderer()
md_blitter.set_markdown(mdfile_path)

# pygame-loop
f = True
while True:
    # INPUT - Mouse + Keyboard
    for event in pygame.event.get():  # handle QUIT operation
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if f:
        md_blitter.display(surface, offset_X, offset_Y, textAreaWidth, textAreaHeight)  # renders the markdown text onto the surface.
        f = False
    pygame.display.flip()  # updates pygame window
