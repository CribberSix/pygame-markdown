import pygame
from typing import Tuple


def set_font_sizes(self, h1=20, h2=18, h3=15, normal=15, code=15) -> None:
    self.font_header_size = h1
    self.font_header2_size = h2
    self.font_header3_size = h3
    self.font_normal_size = normal
    self.font_code_size = code
    self.reload_fonts()


def set_font(self, font='Arial', font_code='CourierNew') -> None:
    self.font = font
    self.font_code = font_code
    self.reload_fonts()


def reload_fonts(self) -> None:
    self.font_header = pygame.font.SysFont(self.font, self.font_header_size, bold=True)
    self.font_header2 = pygame.font.SysFont(self.font, self.font_header2_size, bold=True)
    self.font_header3 = pygame.font.SysFont(self.font, self.font_header3_size, bold=True)
    self.font_text = pygame.font.SysFont(self.font, self.font_normal_size, bold=False)
    self.font_code = pygame.font.SysFont(self.font_code, self.font_code_size, bold=False)


def set_line_gaps(self, gap_line=5, gap_paragraph=30) -> None:
    self.gap_line = gap_line
    self.gap_paragraph = gap_paragraph


def set_code_bg_color(self, a: int, b: int, c: int) -> None:
    """
    Setting the coding color with three separate integers,
    """
    self.coding_bg_color = (a, b, c)


def set_code_bg_color(self, a: Tuple) -> None:
    """
    Setting the coding color directly with an rgb tuple (0,0,0)
    """
    self.coding_bg_color = a
