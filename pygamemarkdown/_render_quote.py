import pygame


def prep_quote(self) -> int:
    indentation_code = 30  # quote is shown indented
    start_of_line = self.x + indentation_code
    return start_of_line


def draw_quote_rect(self, y_start, y_end) -> None:
    # Only possible to draw after the fact, as we do not know how many lines the quote will have.
    indentation_code = 30  # quote is shown indented

    line_height = self.get_surface('tmp', 'quote').get_height() + self.gap_line
    x_coordinate = self.x + (0.5 * indentation_code)
    y_coordinate = y_start
    width = 5
    height = (y_end - y_start) + line_height - self.gap_line

    pygame.draw.rect(self.screen, self.quote_color, pygame.Rect(x_coordinate, y_coordinate, width, height))
