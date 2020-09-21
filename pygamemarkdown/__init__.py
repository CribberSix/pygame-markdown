import pygame


class MarkdownBlitter():

    def __init__(self, screen, text, x, y, width=-1, height=-1):
        # dimensions of the area in which the text is being blitted
        self.x = x
        self.y = y
        # if no values are given, we take the end of the screen as limit.
        self.w = width if width > 0 else screen.get_width() - x
        self.h = height if height > 0 else screen.get_height() - y
        self.screen = screen
        self.text = text

        # FONT
        pygame.font.init()
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)  # TEMP
        self.line_gap = 20

        # split in whitespaces, add whitespaces back to every element
        # except the last one
        split = text.split()
        self.text_cut = [substr + " " for substr in split[:-1]] + [split[-1]]
        self.text_surfaces = [self.myfont.render(t, False, (0, 0, 0)) for t in self.text_cut]

        print(self.text_cut)

    def display(self):
        x = self.x
        y = self.y
        prev_text_height = 0

        for text_surface in self.text_surfaces:
            if x + text_surface.get_width() < self.x + self.w:
                self.screen.blit(text_surface, (x, y))
                x = x + text_surface.get_width()

                prev_text_height = text_surface.get_height()

            else:  # new line
                y += prev_text_height + self.line_gap
                x = self.x
                self.screen.blit(text_surface, (x, y))
                x = x + text_surface.get_width()
                prev_text_height = text_surface.get_height()
