import pygame
from warnings import warn

class MarkdownRenderer:

    from ._parse_text import parse_into_text_blocks
    from ._interpret_text import interpret_text_blocks
    from ._render import render_block
    from ._render_get_surface import get_surface
    from ._render_code_block import prep_code_block_and_draw_rect
    from ._render_quote import get_quote_identation, draw_quote_rect
    from ._render_code_inline import check_for_inline_code_and_draw, draw_inline_code_rect
    from ._render_horizontal_rule import draw_horizontal_rule
    from ._render_text import prep_text
    from ._render_list_unordered import prep_unordered_list
    from ._render_list_ordered import prep_ordered_list

    from ._customization import set_font_sizes, set_font, reload_fonts, set_line_gaps, set_quote_color, set_font_color,\
            set_code_bg_color


    def __init__(self):
        # attributes for the rendering process
        self.text = []
        self.text_blocks_dicts = []
        self.x = None
        self.y = None
        self.w = None
        self.h = None
        self.screen = None

        # FONT
        pygame.font.init()
        self.font_normal_str = 'Arial'
        self.font_code_str = 'CourierNew'
        self.font_header_size = 20
        self.font_header = pygame.font.SysFont(self.font_normal_str, self.font_header_size, bold=True)
        self.font_header2_size = 18
        self.font_header2 = pygame.font.SysFont(self.font_normal_str, self.font_header2_size, bold=True)
        self.font_header3_size = 15
        self.font_header3 = pygame.font.SysFont(self.font_normal_str, self.font_header3_size, bold=True)
        self.font_text_size = 15
        self.font_text = pygame.font.SysFont(self.font_normal_str, self.font_text_size, bold=False)
        self.font_code_size = 15
        self.font_code = pygame.font.SysFont(self.font_code_str, self.font_text_size, bold=False)
        self.font_quote_size = 15
        self.font_quote = pygame.font.SysFont(self.font_normal_str, self.font_quote_size, bold=False)
        self.gap_line = 5
        self.gap_paragraph = 30

        self.font_color = (0, 0, 0)
        self.coding_bg_color = (145, 163, 176)
        self.quote_color = (114, 160, 193)

        self.pattern_header = r'^#.+$'
        self.pattern_h1 = r'^#{1}\s?.+$'
        self.pattern_h2 = r'^#{2}\s?.+$'
        self.pattern_h3 = r'^#{3}\s?.+$'
        self.pattern_unorderedList = r'^\s*-\s.+$'
        self.pattern_uList_first_indent = r'^\s{0,3}-\s.+$'
        self.pattern_uList_second_indent = r'^\s{4}-\s.+$'
        self.pattern_orderedList = r'^\s*\d{1,2}\.\s.*$'

        self.pattern_hrule = r'^\s*-{3,}\s*$'
        self.pattern_quote = r'^\s*>.*$'
        self.pattern_code = r'^\s*`{3}.*$'

    def set_markdown(self, mdfile_path):
        """
        :param mdfile_path: path to a local markdown file
        :return: None
        """
        if mdfile_path.endswith('.md'):
            with open(mdfile_path, "r") as f:
                self.text = list(f)
            lines = [i.replace('\n', '') for i in self.text]  # replace newline characters (for now)
        else:
            warn(mdfile_path + " is not a markdown file. Continuing with substituted empty file.")
            lines = []

        text_blocks_logical = self.parse_into_text_blocks(lines)  # parse physical lines into logical lines
        self.text_blocks_dicts = self.interpret_text_blocks(text_blocks_logical)

    def display(self, surface, offset_x, offset_y, width=-1, height=-1) -> None:
        self.x = offset_x
        self.y = offset_y
        # if no values are given, we take the end of the screen as limit.
        self.w = width if width > 0 else surface.get_width() - self.x
        self.h = height if height > 0 else surface.get_height() - self.y
        self.screen = surface

        line_position_y = self.y
        for block in self.text_blocks_dicts:
            line_position_y = self.render_block(block['chars'], block['type'], line_position_y)
            line_position_y = line_position_y + self.gap_paragraph
