import pygame


def check_for_inline_code_and_draw(self, inline_code_tuples, char_counter, word, x, y, code_flag) -> bool:
    """
    Identifies the words highlighted by the inline-code signifiers and draws rectangles as a background
    for the words encased by the sginifiers. Returns the rest of the inline_code_tuples, signifying further
    inline-code statements.
    """

    for t in inline_code_tuples:
        if char_counter == t[0]:  # code begins
            if char_counter + len(word) - 2 == t[1]:  # one-word code -> check minus whitespace
                self.draw_inline_code_rect(x, y, word, 'oneword')
                return False, inline_code_tuples[1:]
            else:  # multiple words
                self.draw_inline_code_rect(x, y, word, 'start')
                return True, inline_code_tuples

        elif char_counter - 2 + len(word) == t[1] and code_flag:  # code ends  -> check minus whitespace
            self.draw_inline_code_rect(x, y, word, 'end')
            return False, inline_code_tuples[1:]

        elif code_flag:
            self.draw_inline_code_rect(x, y, word, 'middle')

    return code_flag, inline_code_tuples


def draw_inline_code_rect(self, x, y, word, position) -> None:
    """
    Renders a background rect for the words encased with coding signifiers in the plain text.
    """
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


