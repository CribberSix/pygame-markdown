import pygame
from typing import List

class MarkdownBlitter():

    def __init__(self, screen, text, x, y, width=-1, height=-1):

        from ._customization import set_font_sizes, set_font, reload_fonts, set_line_gaps

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
        self.font_text = pygame.font.SysFont(self.font, self.font_text_size)

        self.gap_line = 5
        self.gap_paragraph = 20

        # TODO: Sort text into functional blocks based on (?), independent of lines.
        # A new block is symbolized by an empty line in between
        # A new block is symbolized by header-characters at the beginning
        # A new block starts in the next line after a header-line
        # ...

        lines = [i.replace('\n', '') for i in text]  # replace newline characters (for now)
        lines = [i.lstrip() for i in text]  # remove leading whitespaces
        text_cut = list(filter(lambda a: a != '', lines))  # filter out empty lines
        self.text_blocks = self.interpret_text_blocks(text_cut)

    def interpret_text_blocks(self, text_cut) -> List:
        text_blocks = []
        for line in text_cut:
            if line[:2] == '# ':  # h1
                text_blocks.append({'chars': line[2:].lstrip(), 'type': 'h1'})
            elif line[:3] == '## ':
                text_blocks.append({'chars': line[3:].lstrip(), 'type': 'h2'})
            elif line[:4] == '### ':
                text_blocks.append({'chars': line[4:].lstrip(), 'type': 'h3'})
            else:
                text_blocks.append({'chars': line, 'type': 'text'})
        return text_blocks

    def display(self) -> None:
        y = self.y
        for block in self.text_blocks:
            y = self.render_block(block['chars'], block['type'], y)

    def render_block(self, text, type, y) -> int:
        """
        Renders a "block" (a string) and determines automatically at which point a new line is needed.
        The text is left leaning on the border of the area and never extends over the width of the text area.
        """
        # Split on whitespaces and add whitespaces back to the individual words.
        text_sp = text.split()
        if len(text_sp) == 0:
            textblock = [""]
        else:
            textblock = [substr + " " for substr in text_sp[:-1]] + [text_sp[-1]]

        # iterate over the words to determine when a new line is needed.
        x = self.x
        for word in textblock:
            surface = self.get_surface(word, type)

            if x + surface.get_width() < self.x + self.w:
                self.screen.blit(surface, (x, y))
                x = x + surface.get_width()
                prev_text_height = surface.get_height()

            else:  # new line
                y += prev_text_height + self.gap_line
                x = self.x
                self.screen.blit(surface, (x, y))
                x = x + surface.get_width()
                prev_text_height = surface.get_height()

        return y + prev_text_height + self.gap_paragraph

    def get_surface(self, word, type) -> pygame.Surface:
        """
        Returns rendered surface of a string (word) based on Markdown text types.
        """
        if type == 'h1':  #
            return self.font_header.render(word, False, (0, 0, 0))
        elif type == 'h2':
            return self.font_header2.render(word, False, (0, 0, 0))
        elif type == 'h3':
            return self.font_header3.render(word, False, (0, 0, 0))
        else:
            return self.font_text.render(word, False, (0, 0, 0))
