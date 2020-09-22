import pygame
from typing import List, Tuple


def display(self) -> None:
    y = self.y
    for block in self.text_blocks_dicts:
        y = self.render_block(block['chars'], block['type'], y)
        y = y + self.gap_paragraph


def prep_code_and_draw_rect(self, test_list: List[str], y: int) -> Tuple[List[str], int]:
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


def prep_quote(self):
    indentation_code = 30  # quote is shown indented
    start_of_line = self.x + indentation_code
    return start_of_line



def render_block(self, text: str, t_type: str, y: int) -> int:
    """
    Renders a "block" (a string) based on the number of lines. Coding lines have necessary newline characters
    as well as bullet-point paragraphs.

    For overflowing text the method determines automatically at which point a new line is needed.
    The text is left leaning on the border of the area and never extends over the width of the text area.

    Returns
    """
    start_of_line_x = self.x
    text_split = text.split('\n')

    print("________")
    print(t_type)
    print(text_split)
    print("start_of_line_y: " + str(y))

    # ___ CODE BLOCK PREPARATION AND BACKGROUND RECT ___
    if t_type == 'code':
        text_split, start_of_line_x = self.prep_code_and_draw_rect(text_split, y)

    # ___ QUOTE BLOCK PREPARATION ___
    if t_type == 'quote':
        start_of_line_x = self.prep_quote()
        start_of_line_y = y

    # ___ LINE BLITTING ___
    for i, line in enumerate(text_split):
        # Split on whitespaces and add whitespaces back to the individual words (all but the last)
        word_split = line.split()
        if len(word_split) == 0:
            wordblock = [""]
        else:
            wordblock = [substr + " " for substr in word_split[:-1]] + [word_split[-1]]

        # iterate over the words to determine when a new line is needed.
        x = start_of_line_x
        for word in wordblock:
            surface = self.get_surface(word, t_type)

            if x + surface.get_width() < self.x + self.w:
                # Continue in current line
                self.screen.blit(surface, (x, y))
                x = x + surface.get_width()
                prev_text_height = surface.get_height()

            else:  # new line
                y += prev_text_height + self.gap_line
                x = start_of_line_x
                self.screen.blit(surface, (x, y))
                x = x + surface.get_width()
                prev_text_height = surface.get_height()

        if i < len(text_split) - 1:  # between the lines of one block, we add a gap
            y += prev_text_height + self.gap_line

    # ___ QUOTE BLOCK RECT ___
    if t_type == 'quote':
        self.draw_quote_rect(start_of_line_y, y)
    print("end_of_line_y: " + str(y))

    return y


def draw_quote_rect(self, y_start, y_end):
    # Only possible to draw after the fact, as we do not know how many lines the quote will have.
    indentation_code = 30  # quote is shown indented

    line_height = self.get_surface('tmp', 'quote').get_height() + self.gap_line
    x_coordinate = self.x + (0.5 * indentation_code)
    y_coordinate = y_start
    width = 5
    height = (y_end - y_start) + line_height - 5

    pygame.draw.rect(self.screen, self.quote_color, pygame.Rect(x_coordinate, y_coordinate, width, height))


def get_surface(self, word: str, t_type: str) -> pygame.Surface:
    """
    Returns rendered surface of a string (word) based on Markdown text types.
    """
    if t_type == 'h1':  #
        return self.font_header.render(word, False, self.font_color)
    elif t_type == 'h2':
        return self.font_header2.render(word, False, self.font_color)
    elif t_type == 'h3':
        return self.font_header3.render(word, False, self.font_color)
    elif t_type == 'code':
        return self.font_code.render(word, True, self.font_color)
    elif t_type == 'quote':
        return self.font_quote.render(word, True, self.quote_color)
    else:
        return self.font_text.render(word, False, self.font_color)
