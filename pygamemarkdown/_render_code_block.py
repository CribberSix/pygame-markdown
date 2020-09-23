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
    height_of_line = self.get_surface('tmp', 'code').get_height() + self.gap_line
    extension = 3
    x_coordinate = self.x + (0.5 * indentation)
    y_coordinate = y - extension
    width = self.w - (1 * indentation)
    height = (number_of_lines * height_of_line) + extension
    pygame.draw.rect(self.screen, self.coding_bg_color, pygame.Rect(x_coordinate, y_coordinate, width, height))
    return test_list, start_of_line
