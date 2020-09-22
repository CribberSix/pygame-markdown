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

    # ___ CODE BLOCK PREPARATION AND BACKGROUND RECT ___
    if t_type == 'code':
        text_split, start_of_line_x = self.prep_code_and_draw_rect(text_split, y)

    # ___ QUOTE BLOCK PREPARATION ___
    if t_type == 'quote':
        start_of_line_x = self.prep_quote()
        start_of_line_y = y

    if t_type == 'text':
        # identify inline-code (start + end)
        print("______________")
        print("text")
        print(text_split)
        inline_code_tuples = []
        start = -1
        c = 0
        result = ""
        for char in text_split[0]:
            if char == '`':
                if start == -1:
                    start = c
                else:
                    inline_code_tuples.append((start, c - 1))
                    start = -1
            else:
                result = result + char
                c = c + 1

        # __ DEVELOPMENT ____
        print(result)
        print("inline_code_tuples: " + str(inline_code_tuples))
        for t in inline_code_tuples:
            print("CUT: " + result[t[0]:t[1] + 1])

        text_split[0] = result

    code_flag = False
    # ___ LINE BLITTING ___

    char_counter = 0
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

                if t_type == 'text':
                    code_flag, inline_code_tuples = self.check_for_inline_code_and_draw(inline_code_tuples,
                                                                                        char_counter, word, x, y,
                                                                                        code_flag)

                self.screen.blit(surface, (x, y))
                x = x + surface.get_width()
                prev_text_height = surface.get_height()

            else:  # new line
                y += prev_text_height + self.gap_line
                x = start_of_line_x

                if t_type == 'text':
                    code_flag, inline_code_tuples = self.check_for_inline_code_and_draw(inline_code_tuples,
                                                                                        char_counter, word, x, y,
                                                                                        code_flag)

                self.screen.blit(surface, (x, y))
                x = x + surface.get_width()
                prev_text_height = surface.get_height()

            char_counter += len(word)
        if i < len(text_split) - 1:  # between the lines of one block, we add a gap
            y += prev_text_height + self.gap_line

    # ___ QUOTE BLOCK RECT ___
    if t_type == 'quote':
        self.draw_quote_rect(start_of_line_y, y)

    return y


def check_for_inline_code_and_draw(self, inline_code_tuples, char_counter, word, x, y, code_flag) -> bool:

    if len(inline_code_tuples) > 0:
        print("_______________________________________________________________")
        print(inline_code_tuples)
        print("word: " + word + "|")
        #print("char_counter: " + str(char_counter))
        #print("char_counter - 2 + len(word): " + str(char_counter - 2 + len(word)))
        print("Flag: " + str(code_flag))

    for t in inline_code_tuples:
        print(t[1])
        if char_counter - 2 + len(word) == t[1]:
            print("WORD END IS CORRECT")

        if char_counter == t[0]:  # code begins
            if char_counter + len(word) - 2 == t[1]:  # one-word code -> check minus whitespace
                self.draw_inline_code_rect(x, y, word, 'oneword')
                print("ONE-WORD-CODE")
                return False, inline_code_tuples[1:]
            else:  # multiple words
                print("CODE MULTIPLE BEGINS: " + word)
                self.draw_inline_code_rect(x, y, word, 'start')
                return True, inline_code_tuples

        elif char_counter - 2 + len(word) == t[1] and code_flag:  # code ends  -> check minus whitespace
            print("CODE MULTIPLE ENDS")
            self.draw_inline_code_rect(x, y, word, 'end')
            return False, inline_code_tuples[1:]

        elif code_flag:
            self.draw_inline_code_rect(x, y, word, 'middle')

    return code_flag, inline_code_tuples

def draw_inline_code_rect(self, x, y, word, position):
    print("DRAW: " + str(x) + ", " + str(y) + ", " + word)
    height_of_line = self.get_surface(word, 'text').get_height()  # + self.gap_line
    xcoord = x

    # Adaption depending where we are in the inline code
    if position == 'start':  # start in the middle of the leading whitespace.
        xcoord = x - (0.5 * self.get_surface(' ', 'text').get_width())
        width = self.get_surface(word, 'text').get_width() + (0.5 * self.get_surface(' ', 'text').get_width())
    elif position == 'middle':
        width = self.get_surface(word, 'text').get_width()
    elif position == 'end':  # ends in the middle of the trailing whitespace
        width = self.get_surface(word, 'text').get_width() - (0.5 * self.get_surface(' ', 'text').get_width())
    elif position == 'oneword':  # starts in the middle of leading, ends in the middle of trailing whitespace
        xcoord = x - (0.5 * self.get_surface(' ', 'text').get_width())
        width = self.get_surface(word, 'text').get_width()

    pygame.draw.rect(self.screen, self.coding_bg_color, pygame.Rect(xcoord, y, width, height_of_line))


def draw_quote_rect(self, y_start, y_end):
    # Only possible to draw after the fact, as we do not know how many lines the quote will have.
    indentation_code = 30  # quote is shown indented

    line_height = self.get_surface('tmp', 'quote').get_height() + self.gap_line
    x_coordinate = self.x + (0.5 * indentation_code)
    y_coordinate = y_start
    width = 5
    height = (y_end - y_start) + line_height - self.gap_line

    pygame.draw.rect(self.screen, self.quote_color, pygame.Rect(x_coordinate, y_coordinate, width, height))


def get_surface(self, word: str, t_type: str) -> pygame.Surface:
    """
    Returns rendered surface of a string (word) based on Markdown text types.
    """
    if t_type == 'h1':
        return self.font_header.render(word, False, self.font_color)
    elif t_type == 'h2':
        return self.font_header2.render(word, False, self.font_color)
    elif t_type == 'h3':
        return self.font_header3.render(word, False, self.font_color)

    elif t_type == 'code':
        return self.font_code.render(word, True, self.font_color)

    elif t_type == 'quote':
        return self.font_quote.render(word, True, self.quote_color)

    elif t_type == 'unorderdList':
        return self.font_text.render(word, False, self.font_color)
    elif t_type == 'text':
        return self.font_text.render(word, False, self.font_color)
    else:
        return self.font_text.render(word, False, self.font_color)
