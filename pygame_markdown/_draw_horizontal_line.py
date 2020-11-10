import pygame


def draw_horizontal_line(self, y):
    """ Draws a horizontal line if visible.

    :param self: MarkdownRenderer
    :param y: y-coordinate
    :return:  y-coordinate
    """
    y_offset = 3
    x_offset = 5
    height = 6
    width = self.w - (2 * x_offset)

    if self.is_visible(y + y_offset) and self.is_visible(y + y_offset + height):
        pygame.draw.rect(self.screen, self.hline_color, pygame.Rect(self.x, y + y_offset, width, height))

    return y
