import markdown
import pygame
import re


class MarkdownRenderer:

    # MISCELLANEOUS
    from ._visibility import is_visible, is_above_area, is_below_area
    from ._get_surface import get_surface
    from ._mouse import handle_mouse_input, mouse_within_md_area

    # RENDERING
    from ._inline_preparations import inline_formatting_preparation
    from ._render import render_block
    from ._render_text import render_text
    from ._render_code import render_codeblock
    from ._render_list import render_list

    # DRAWING
    from ._draw_code_background import draw_code_background, draw_codeblock_background
    from ._draw_quote import draw_quote_rect
    from ._draw_horizontal_line import draw_horizontal_line

    # CUSTOMIZATION
    from ._customization import set_font_sizes, set_font, reload_fonts, set_line_gaps, set_hline_color, \
        set_code_bg_color, set_font_color, set_quote_color, set_background_color, set_scroll_step

    def __init__(self, mdfile_path):
        self.x = None
        self.y = None
        self.w = None
        self.h = None
        self.screen = None

        # Colors
        self.md_area_bg_color = (60, 63, 65)
        self.font_color = (204, 204, 204)
        self.coding_bg_color = (44, 44, 44)
        self.quote_color = (98, 102, 103)
        self.hline_color = (44, 44, 44)

        # Fonts
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

        # Text-rendering variables
        self.gap_line = 5
        self.gap_paragraph = 30
        self.indentation_quote = 25
        self.indentation_code = 25

        # Scrollbar
        self.pixel_scroll_step = 25
        self.pixel_first_showable = 0
        self.pixels_showable_at_once = 0
        self.pixels_entire_length = 0

        # load md file and parse to HTML
        with open(mdfile_path, "r") as f:
            l = ''.join(list(f))
        self.html = markdown.markdown(l)
        self.blocks = []
        self.parse_markdown_file()

    def parse_markdown_file(self):
        while True:
            if self.html[:7] == '\n<hr />':  # horizonal line -> special case.
                self.blocks.append(('placeholder', 'horizontal_line'))

            # find the start of the next block:
            pattern_start = r'<\w+>'
            start = re.search(pattern_start, self.html)
            if start is None:
                break  # no new block -> stop working.

            # find the matching end:
            block_type = start.group()[1:-1]
            pattern_end = r'<\/' + block_type + '>'
            end = re.search(pattern_end, self.html)

            if start is not None and end is not None:
                block = self.html[start.span()[1]:  end.span()[0]]

                if block_type == 'p':  # test whether the paragraph is actually a nested code block
                    rex = re.search(r'^<code>[\s\S]+<\/code>$', block)
                    if rex is not None:
                        block_type = 'codeblock'
                        block = block[6:-7]

                self.html = self.html[end.span()[1]:]
                self.blocks.append((block, block_type))

    def set_area(self, surface, offset_x, offset_y, width=-1, height=-1) -> None:
        self.x = offset_x
        self.y = offset_y
        # if no values are given, we take the end of the screen as limit.
        self.w = width if width > 0 else surface.get_width() - self.x
        self.h = height if height > 0 else surface.get_height() - self.y
        self.pixels_showable_at_once = self.h
        self.screen = surface

    def display(self, pygame_events, mouse_x, mouse_y):
        # Background
        pygame.draw.rect(self.screen, self.md_area_bg_color, (self.x, self.y, self.w, self.h))

        line_position_y = self.y - self.pixel_first_showable  # set start position with scroll taken into account

        for block, block_type in self.blocks:

            line_position_y = self.render_block(block, block_type, line_position_y)
            line_position_y = line_position_y + self.gap_paragraph

        if self.pixel_first_showable == 0:
            # top-most setting, we set the entire length of the text
            # subtract offset (=y) and last gap (=gap_paragraph)
            self.pixels_entire_length = line_position_y - self.y

        # handle scrolling-action
        self.handle_mouse_input(pygame_events, mouse_x, mouse_y)
