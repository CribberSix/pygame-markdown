import pygame


def set_font_sizes(self, h1: int = 20, h2: int = 18, h3: int = 15, text: int = 15, code: int = 15, quote: int = 15) -> None:
    """
    Customizes the font size for all three headers, the text, quoteblocks (quote) and codeblocks (code)
    All font sizes can be individually customized.
    """
    self.font_header_size = h1
    self.font_header2_size = h2
    self.font_header3_size = h3
    self.font_text_size = text
    self.font_code_size = code
    self.font_quote_size = quote
    self.reload_fonts()


def set_font(self, font_text='Arial', font_code='CourierNew') -> None:
    """
    Customizes the font by using Strings for pygame.font.Sysfont.
    Normal font for text and the font for code can be individually customized.
    """
    self.font_normal_str = font_text
    self.font_code_str = font_code
    self.reload_fonts()


def reload_fonts(self) -> None:
    """
    Reloads the fonts after some change happenned (e.g. font or font-size was changed with the other customizing functions).
    """
    self.font_header = pygame.font.SysFont(self.font_normal_str, self.font_header_size, bold=True)
    self.font_header2 = pygame.font.SysFont(self.font_normal_str, self.font_header2_size, bold=True)
    self.font_header3 = pygame.font.SysFont(self.font_normal_str, self.font_header3_size, bold=True)
    self.font_text = pygame.font.SysFont(self.font_normal_str, self.font_text_size, bold=False)
    self.font_code = pygame.font.SysFont(self.font_code_str, self.font_code_size, bold=False)
    self.font_quote = pygame.font.SysFont(self.font_normal_str, self.font_quote_size, bold=False)


def set_line_gaps(self, gap_line: int = 5, gap_paragraph: int = 30) -> None:
    """
    Customizes the gaps between lines and paragraphs individually.
    """
    self.gap_line = gap_line
    self.gap_paragraph = gap_paragraph


def set_color_code_background(self, r: int = 44, g: int = 44, b: int = 44) -> None:
    """
    Setting the coding color with three separate integers (rgb).
    """
    self.coding_bg_color = (r, g, b)


def set_color_font(self, r: int = 204, g: int = 204, b: int = 204) -> None:
    """
    Setting the general font color with three separate integers (rgb).
    """
    self.font_color = (r, g, b)


def set_color_quote(self, r: int = 98, g: int = 102, b: int = 103) -> None:
    """
    Setting the general font color with three separate integers (rgb).
    """
    self.quote_color = (r, g, b)


def set_color_hline(self, r: int = 44, g: int = 44, b: int = 44) -> None:
    """
    Setting the general font color with three separate integers (rgb).
    """
    self.hline_color = (r, g, b)


def set_color_background(self, r: int = 60, g: int = 63, b: int = 65) -> None:
    """
    Setting the background color of the markdown area with three separate integers (rgb).
    """
    self.md_area_bg_color = (r, g, b)


def set_scroll_step(self, i: int = 25) -> None:
    """
    Setting the amount of pixels which get scrolled upon one mousewheel 'click'.
    """
    self.pixel_scroll_step = i
