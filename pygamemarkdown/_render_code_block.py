import pygame
from typing import List, Tuple


def prep_code_block_and_draw_rect(self, test_list: List[str], y: int) -> Tuple[List[str], int]:
    """
    Renders a background rect of the coding area and returns the lines containing code.
    Cuts leading and trailing line which contains the coding block signifiers.
    """
    # Render background of coding block and perform special preparations
    test_list = test_list[1:-1]  # remove codeblock apostrophe lines
    indentation = 20  # code is shown indented
    start_of_line = self.x + indentation

    # Calculating the background area and drawing the rect
    number_of_lines = len(test_list)
    height_of_line = self.get_surface('tmp', 'code').get_height()
    extension = 3
    x_coordinate = self.x + (0.5 * indentation)
    y_coordinate = y - extension  # first line
    width = self.w - (1 * indentation)
    height = height_of_line + extension

    prev_line_visible = False
    for i in range(number_of_lines):
        # Rendering the background for every line individually to be able to draw the background when scrolling halfway.
        if self.is_visible(y_coordinate) and self.is_visible(y_coordinate + height):
            if prev_line_visible:  # render filler background between lines
                pygame.draw.rect(self.screen, self.coding_bg_color,
                                 pygame.Rect(x_coordinate, y_coordinate - self.gap_line, width, self.gap_line))

            # Render line background
            pygame.draw.rect(self.screen, self.coding_bg_color, pygame.Rect(x_coordinate, y_coordinate, width, height))
            prev_line_visible = True

        y_coordinate += height_of_line + self.gap_line

    return test_list, start_of_line
