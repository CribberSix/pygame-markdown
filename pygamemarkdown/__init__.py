import pygame


class MarkdownBlitter():

    from ._customization import set_font_sizes, set_font, reload_fonts, set_line_gaps
    from ._parse_text import parse_into_text_blocks, interpret_text_blocks
    from ._render import display, render_block, get_surface, prep_code_and_draw_rect, draw_quote_rect, prep_quote, \
        check_for_inline_code_and_draw, draw_inline_code_rect, draw_horizontal_rule


    def __init__(self, screen, text, x, y, width=-1, height=-1):

        # dimensions of the area in which the text is being blitted
        self.x = x
        self.y = y
        # if no values are given, we take the end of the screen as limit.
        self.w = width if width > 0 else screen.get_width() - x
        self.h = height if height > 0 else screen.get_height() - y
        self.screen = screen
        self.text = text

        # FONT
        pygame.font.init()
        self.font = 'Arial'
        self.font_header_size = 20
        self.font_header = pygame.font.SysFont(self.font, self.font_header_size, bold=True)
        self.font_header2_size = 18
        self.font_header2 = pygame.font.SysFont(self.font, self.font_header2_size, bold=True)
        self.font_header3_size = 15
        self.font_header3 = pygame.font.SysFont(self.font, self.font_header3_size, bold=True)
        self.font_text_size = 15
        self.font_text = pygame.font.SysFont(self.font, self.font_text_size, bold=False)
        self.font_code_size = 15
        self.font_code = pygame.font.SysFont('CourierNew', self.font_text_size, bold=False)
        self.font_quote_size = 15
        self.font_quote = pygame.font.SysFont(self.font, self.font_quote_size, bold=False)
        self.gap_line = 5
        self.gap_paragraph = 30

        self.font_color = (0, 0, 0)
        self.coding_bg_color = (145, 163, 176)
        self.quote_color = (114, 160, 193)

        lines = [i.replace('\n', '') for i in text]  # replace newline characters (for now)
        lines = [i.lstrip() for i in lines]  # remove leading whitespaces
        text_blocks_logical = self.parse_into_text_blocks(lines)  # parse physical lines into logical lines
        self.text_blocks_dicts = self.interpret_text_blocks(text_blocks_logical)
