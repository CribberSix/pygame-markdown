import pygame
from pygame_markdown.PygameMarkdown import MarkdownRenderer


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
textAreaHeight = 800
textAreaWidth = 500
mdfile_path = "README_test.md"


md = MarkdownRenderer()
md.set_markdown(mdfile_path)
md.set_area(surface, offset_X, offset_Y, textAreaWidth, textAreaHeight)

# OPTIONAL
#md.set_scroll_step(25)
#md.set_line_gaps(8, 35)
#md.set_font_sizes(28, 24, 20, 16, 16, 16)


md.set_font('Arial', 'CourierNew')
md.set_color_background(204, 204, 204)
md.set_color_code_background(42, 157, 143)
md.set_color_font(41, 50, 65)
md.set_color_hline(41, 50, 65)
#md.set_color_quote(41, 50, 65)

while True:
    pygame.draw.rect(screen, (255,255, 255), (0, 0, screenWidth, screenHeight))

    # get various input from pygame
    pygame_events = pygame.event.get()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    for event in pygame_events:  # handle QUIT operation
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    md.color_font = (41, 50, 65)
    md.display(pygame_events, mouse_x, mouse_y, mouse_pressed)  # renders the markdown text onto the surface.

    pygame.display.flip()  # updates pygame window

