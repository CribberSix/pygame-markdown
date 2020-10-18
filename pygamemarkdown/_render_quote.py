import pygame


def get_quote_identation(self) -> int:
    """
    Returns the indentation of the code
    by pixels as concrete coordinates based
    on the x-coordinate of the textarea.
    """
    start_of_line = self.x + self.indentation_code
    return start_of_line


def draw_quote_rect(self, y_start, y_end) -> None:
    """
    Draws the vertical thin rect in front of the quoted text.
    """
    # Only possible to draw after the fact, as we do not know how many lines the quote will have.

    line_height = self.get_surface('tmp', 'quote').get_height() + self.gap_line
    x_coordinate = self.x + (0.5 * self.indentation_code)
    y_coordinate = y_start
    width = 5
    height = (y_end - y_start) + line_height - self.gap_line
    if self.is_visible(y_coordinate):
        pygame.draw.rect(self.screen, self.quote_color, pygame.Rect(x_coordinate, y_coordinate, width, height))
