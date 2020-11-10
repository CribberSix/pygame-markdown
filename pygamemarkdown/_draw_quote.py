import pygame


def draw_quote_rect(self, y_start, y_end) -> None:
    """
    Draws the vertical thin rect in front of the quoted text.
    Starts/ends half of a gap_line above/below the first line.
    """

    x_coordinate = self.x + (0.5 * self.indentation_quote)
    y_coordinate = y_start - (self.gap_line * 0.5)
    width = 5
    height = (y_end - y_start) + self.gap_line
    pygame.draw.rect(self.screen, self.quote_color, pygame.Rect(x_coordinate, y_coordinate, width, height))
