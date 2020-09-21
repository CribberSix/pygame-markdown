import pygame


def display(self) -> None:
    y = self.y
    for block in self.text_blocks_dicts:
        y = self.render_block(block['chars'], block['type'], y)
        y = y + self.gap_paragraph


def render_block(self, text: str, t_type: str, y: int) -> int:
    """
    Renders a "block" (a string) based on the number of lines. Coding lines have necessary newline characters
    as well as bullet-point paragraphs.

    For overflowing text the method determines automatically at which point a new line is needed.
    The text is left leaning on the border of the area and never extends over the width of the text area.

    Returns
    """
    text_split = text.split('\n')
    for i, line in enumerate(text_split):
        # Split on whitespaces and add whitespaces back to the individual words (all but the last)
        word_split = line.split()
        if len(word_split) == 0:
            wordblock = [""]
        else:
            wordblock = [substr + " " for substr in word_split[:-1]] + [word_split[-1]]

        # iterate over the words to determine when a new line is needed.
        x = self.x
        for word in wordblock:
            surface = self.get_surface(word, t_type)

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

        if i < len(text_split) - 1:  # between the lines of one block, we add a gap
            y += prev_text_height + self.gap_line
    return y


def get_surface(self, word: str, t_type:str) -> pygame.Surface:
    """
    Returns rendered surface of a string (word) based on Markdown text types.
    """
    if t_type == 'h1':  #
        return self.font_header.render(word, False, (0, 0, 0))
    elif t_type == 'h2':
        return self.font_header2.render(word, False, (0, 0, 0))
    elif t_type == 'h3':
        return self.font_header3.render(word, False, (0, 0, 0))
    else:
        return self.font_text.render(word, False, (0, 0, 0))
