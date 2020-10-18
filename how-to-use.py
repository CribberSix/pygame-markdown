import pygame
from pygamemarkdown import MarkdownRenderer

# minimal pygame setup
pygame.init()
screenHeight = 1800
screenWidth = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Pygame")
pygame.display.get_surface().fill((200, 200, 200))  # background coloring

# parameters
surface = pygame.display.get_surface()  # get existing pygame window/screen
offset_X = 50  # offset from the left border of the pygame window
offset_Y = 20  # offset from the top border of the pygame window
textAreaHeight = 500
textAreaWidth = 500
mdfile_path = "README_test.md"

# mark

# Setup MD-Renderer
md_blitter = MarkdownRenderer()
md_blitter.set_markdown(mdfile_path)
md_blitter.set_line_gaps(10, 40)
md_blitter.set_area(surface, offset_X, offset_Y, textAreaWidth, textAreaHeight)

# pygame-loop
f = True
blitonce = False
while True:
    # INPUT - Mouse + Keyboard
    pygame.draw.rect(screen, (255,255,255), (0, 0, screenWidth, screenHeight))

    pygame_events = pygame.event.get()
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame_events:  # handle QUIT operation
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if f:
        md_blitter.display(pygame_events, mouse_x, mouse_y) # renders the markdown text onto the surface.
        if blitonce:
            f = False

    pygame.display.flip()  # updates pygame window
