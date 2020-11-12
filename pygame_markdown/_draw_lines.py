import pygame


def draw_horizontal_line(self, y):
    """ Draws a horizontal line if visible.

    :param self: MarkdownRenderer
    :param y: y-coordinate
    :return:  y-coordinate
    """
    y_offset = 3
    x_offset = 10
    height = 6
    width = self.w - (2 * x_offset)

    if self.is_visible(y + y_offset) and self.is_visible(y + y_offset + height):
        pygame.draw.rect(self.screen, self.color_hline, pygame.Rect(self.x +  x_offset, y + y_offset, width, height))

    return y


def draw_subheader_line(self, y):
    """ Draws a horizontal thin line (below headers) if visible.

    :param self: MarkdownRenderer
    :param y: y-coordinate
    :return:  y-coordinate
    """
    y_offset = 3
    x_offset = 4
    height = 2
    width = self.w - (2 * x_offset)

    if self.is_visible(y + y_offset) and self.is_visible(y + y_offset + height):
        pygame.draw.rect(self.screen, self.color_hline, pygame.Rect(self.x + x_offset, y + y_offset, width, height))

    return y

