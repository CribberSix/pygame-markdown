import pygame


def draw_code_background(self, code_flag, word, x, y, position):
    if code_flag:
        if position == 'last':  # remove last char (whitespace) from background-surface
            word = word[:-1]

        # blit colored background rectangle
        word_surface = self.get_surface(word, 'text')
        width = word_surface.get_width()
        height = word_surface.get_height()
        pygame.draw.rect(self.screen, self.coding_bg_color, pygame.Rect(x, y, width, height))


def draw_codeblock_background(self, y):

    height_of_line = self.get_surface('placeholder', 'code').get_height()

    x_coordinate = self.x + (0.5 * self.indentation_code)
    width = self.w - self.indentation_code

    y_coordinate = y - self.gap_line
    height = height_of_line + (2 * self.gap_line)
    pygame.draw.rect(self.screen, self.coding_bg_color, pygame.Rect(x_coordinate, y_coordinate, width, height))



