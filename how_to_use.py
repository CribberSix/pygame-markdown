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
textAreaHeight = 500
textAreaWidth = 500
mdfile_path = "README_test.md"


md = MarkdownRenderer(mdfile_path)
md.set_area(surface, offset_X, offset_Y, textAreaWidth, textAreaHeight)
# OPTIONAL
#md.set_line_gaps(5, 30)
#md.set_scroll_step(25)
#md.set_font_sizes(20, 18, 15, 15, 15, 15)
#md.set_font('Arial', 'CourierNew')
#md.set_background_color(60, 63, 65)
#md.set_code_bg_color(44, 44, 44)
#md.set_quote_color(98, 102, 103)
#md.set_hline_color(44, 44, 44)
#md.set_font_color(204, 204, 204)


while True:
    # INPUT - Mouse + Keyboard
    pygame.draw.rect(screen, (255,255,255), (0, 0, screenWidth, screenHeight))

    pygame_events = pygame.event.get()
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame_events:  # handle QUIT operation
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    md.display(pygame_events, mouse_x, mouse_y)  # renders the markdown text onto the surface.


    pygame.display.flip()  # updates pygame window


