import pygame


def draw_code_background(self, code_flag, word, x, y, position):
    """ Draws a background rectangle behind inline-code.

    :param self: MarkdownRenderer
    :param code_flag: inline-code flag
    :param word: the word for which the background will be rendered.
    :param x: x-coordinate
    :param y: y-coordinate
    :param position: position of the word in the context of a multi-word inline-code subtext.
    :return: None
    """
    if code_flag:
        if position == 'last':  # remove last char (whitespace) from background-surface
            word = word[:-1]

        # blit colored background rectangle
        word_surface = self.get_surface(word, 'text')
        width = word_surface.get_width()
        height = word_surface.get_height()
        pygame.draw.rect(self.screen, self.color_code_background, pygame.Rect(x, y, width, height))


def draw_codeblock_background(self, y):
    """ Draws the background for an entire line of a codeblock

    :param self: MarkdownRenderer
    :param y: y-coordinate
    :return: None
    """

    height_of_line = self.get_surface('placeholder', 'code').get_height()

    x_coordinate = self.x + (0.5 * self.indentation_code)
    width = self.w - self.indentation_code

    y_coordinate = y - self.gap_line
    height = height_of_line + (2 * self.gap_line)
    pygame.draw.rect(self.screen, self.color_code_background, pygame.Rect(x_coordinate, y_coordinate, width, height))



