import pygame


def draw_horizontal_rule(self, y) -> int:
    """
    Draws a horizontal rectangle along the entire width of the designated text area.
    """
    line_height = self.get_surface("line_tmp", 'text').get_height()
    pygame.draw.rect(self.screen, self.coding_bg_color, pygame.Rect(self.x, y + (0.4 * line_height), self.w, 5))
    y += line_height + self.gap_line
    return y