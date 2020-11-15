import markdown
import pygame
import re


class MarkdownRenderer:

    # MISCELLANEOUS
    from ._visibility import is_visible, is_above_area, is_below_area
    from ._get_surface import get_surface
    from ._mouse import handle_mouse_input, mouse_within_md_area
    from ._scrollbar import draw_scrollbar, scroll_down, scroll_up

    # RENDERING
    from ._inline_preparations import inline_formatting_preparation
    from ._render import render_block
    from ._render_text import render_text
    from ._render_code import render_codeblock
    from ._render_list import render_list

    # DRAWING
    from ._draw_code_background import draw_code_background, draw_codeblock_background
    from ._draw_quote import draw_quote_rect
    from ._draw_lines import draw_horizontal_line, draw_subheader_line

    # CUSTOMIZATION
    from ._customization import set_font_sizes, set_font, reload_fonts, set_line_gaps, set_color_hline, \
        set_color_code_background, set_color_font, set_color_quote, set_color_background, set_scroll_step

    def __init__(self):
        self.x: int = None
        self.y: int = None
        self.w: int = None
        self.h: int = None
        self.margin: int = None
        self.screen: pygame.Surface = None

        # Scrollbar
        self.scrollbar: pygame.Rect = None
        self.scroll_start_y: int = None
        self.scroll_dragging: bool = False

        # Colors
        self.color_area_background = (60, 63, 65)
        self.color_font = (204, 204, 204)
        self.color_code_background = (44, 44, 44)
        self.color_quote = (98, 102, 103)
        self.color_hline = (44, 44, 44)
        self.color_scrollbar = (44, 44, 44)

        # Fonts
        pygame.font.init()
        self.font_normal_str = 'Arial'
        self.font_code_str = 'Courier'
        self.font_header_size = 28
        self.font_header = pygame.font.SysFont(self.font_normal_str, self.font_header_size, bold=True)
        self.font_header2_size = 24
        self.font_header2 = pygame.font.SysFont(self.font_normal_str, self.font_header2_size, bold=True)
        self.font_header3_size = 20
        self.font_header3 = pygame.font.SysFont(self.font_normal_str, self.font_header3_size, bold=True)
        self.font_text_size = 16
        self.font_text = pygame.font.SysFont(self.font_normal_str, self.font_text_size, bold=False)
        self.font_code_size = 16
        self.font_code = pygame.font.SysFont(self.font_code_str, self.font_text_size, bold=False)
        self.font_quote_size = 16
        self.font_quote = pygame.font.SysFont(self.font_normal_str, self.font_quote_size, bold=False)

        # Text-rendering variables
        self.gap_line = 8
        self.gap_paragraph = 35
        self.indentation_quote = 25
        self.indentation_code = 25
        self.code_padding = 2

        # Scrollbar
        self.pixel_scroll_step = 25
        self.pixel_first_showable = 0
        self.pixels_showable_at_once = 0
        self.pixels_entire_length = 0

        self.html = ""
        self.blocks = []

    def set_markdown(self, mdfile_path):
        # load md file and parse to HTML
        with open(mdfile_path, "r") as f:
            l = ''.join(list(f))
        self.html = markdown.markdown(l)
        self.html = self.html.replace('&amp;', '&')  # '&' symbol is parsed by HTML to '&amp;', has to be reversed.
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
                    rex = re.search(r'^<code>[\s\S]+<\/code>$', block.strip(' '))
                    if rex is not None:
                        block_type = 'codeblock'
                        block = block.strip(' ')[6:-7]

                self.html = self.html[end.span()[1]:]
                self.blocks.append((block, block_type))

    def set_area(self, surface, offset_x, offset_y, width=-1, height=-1, margin=10) -> None:
        """
        TODO: missing docstring
        :param surface:
        :param offset_x:
        :param offset_y:
        :param width:
        :param height:
        :param margin:
        :return:
        """
        self.margin = margin
        # for simplicity, margin is subtracted from the initial x, y, w and h.
        # When rendering the background rect, we add the margin.
        # This way, margin does not have any effect on other calculations.

        self.x = offset_x + margin
        self.y = offset_y + margin
        # if no values are given, we take the end of the screen as limit.
        self.w = width - (2 * self.margin) if width > 0 else surface.get_width() - offset_x - (2 * self.margin)
        self.h = height - (2 * self.margin) if height > 0 else surface.get_height() - offset_y - (2 * self.margin)
        self.pixels_showable_at_once = self.h
        self.screen = surface

    def display(self, pygame_events, mouse_x, mouse_y, mouse_pressed):
        """
        TODO: missing docstring
        :param pygame_events:
        :param mouse_x:
        :param mouse_y:
        :param mouse_pressed:
        :return:
        """
        # Background -> reverse the margins
        pygame.draw.rect(self.screen, self.color_area_background, (self.x - self.margin, self.y - self.margin,
                                                                   self.w + (2 * self.margin), self.h + (2 * self.margin)))

        # Set start position with scroll taken into account
        line_position_y = self.y - self.pixel_first_showable

        # Render the markdown blocks
        for block, block_type in self.blocks:
            line_position_y = self.render_block(block, block_type, line_position_y)
            line_position_y = line_position_y + self.gap_paragraph

        if self.pixel_first_showable == 0:
            # top-most setting, we set the entire length of the text
            # subtract offset (=y) and last gap (=gap_paragraph)
            self.pixels_entire_length = line_position_y - self.y

        # scrollbar
        self.draw_scrollbar()

        # handle scrolling-action
        self.handle_mouse_input(pygame_events, mouse_x, mouse_y, mouse_pressed)

