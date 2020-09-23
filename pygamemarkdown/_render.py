import pygame


def display(self) -> None:
    line_position_y = self.y
    for block in self.text_blocks_dicts:
        line_position_y = self.render_block(block['chars'], block['type'], line_position_y)
        line_position_y = line_position_y + self.gap_paragraph


def render_block(self, text: str, t_type: str, y: int) -> int:
    """
    Renders a "block" (a string) based on the number of lines. Coding paragraphs have necessary newline characters
    as well as bullet-point paragraphs.

    For overflowing text the method determines automatically at which point a new line is needed.
    The text is left leaning on the border of the area and never extends over the width of the text area.

    Returns
    """

    start_of_line_x = self.x
    text_split = text.split('\n')

    # ___ HORIZONTAL RULE IMPLEMENTATION ___
    if t_type == 'horizontalRule':
        self.draw_horizontal_rule(y)
        return

    # ___ CODE BLOCK PREPARATION AND BACKGROUND RECT ___
    if t_type == 'code':
        text_split, start_of_line_x = self.prep_code_block_and_draw_rect(text_split, y)

    # ___ QUOTE BLOCK PREPARATION ___
    if t_type == 'quote':
        start_of_line_x = self.prep_quote()
        start_of_line_y = y

    # ___ TEXT (with possible inline-code) PREPARATION __
    if t_type == 'text':
        text_split[0], inline_code_tuples = self.prep_text(text_split[0])

    # ___ LINE BLITTING ___
    code_flag = False
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
        if i < len(text_split) - 1:  # between the lines of a block, we add a gap
            y += prev_text_height + self.gap_line

    # ___ QUOTE BLOCK RECT ___
    if t_type == 'quote':
        self.draw_quote_rect(start_of_line_y, y)

    return y


