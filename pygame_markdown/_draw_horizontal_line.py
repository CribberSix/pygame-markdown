import pygame


def draw_horizontal_line(self, y):
    """
    Draws a horizontal line if visible.
    """
    y_offset = 3
    height = 6
    if self.is_visible(y + y_offset) and self.is_visible(y + y_offset + height):
        pygame.draw.rect(self.screen, self.quote_color, pygame.Rect(self.x, y + y_offset, self.w, height))

    return y
