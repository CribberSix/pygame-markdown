import pygame
from pygamemarkdown.PygameMarkdown import MarkdownRenderer


# minimal pygame setup
pygame.init()
screenHeight = 900
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


md_blitter = MarkdownRenderer(mdfile_path)
md_blitter.set_area(surface, offset_X, offset_Y, textAreaWidth, textAreaHeight)

while True:
    # INPUT - Mouse + Keyboard
    pygame.draw.rect(screen, (255,255,255), (0, 0, screenWidth, screenHeight))

    pygame_events = pygame.event.get()
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame_events:  # handle QUIT operation
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    md_blitter.display(pygame_events, mouse_x, mouse_y)  # renders the markdown text onto the surface.


    pygame.display.flip()  # updates pygame window


