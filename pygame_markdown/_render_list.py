

def render_list(self, block: str, block_type: str, y: int, ordered) -> int:
    """ Renders the items of a list (ordered and unordered). Replaces the supplied numbers / hyphen with the correctly
    ordered numbers / unicode character for display.

    :param self: MarkdownRenderer
    :param block: string of text
    :param block_type: type of the text (e.g. headers, ordered/unordered lists, blockquotes, code etc)
    :param y:  y-coordinate to start rendering on
    :param ordered: boolean to signal whether we have an ordered or unordered list at hand
    :return: y-coordinate after rendering is finished
    """

    start_of_line_x = self.x
    x = start_of_line_x

    # Cleanup
    block = block \
        .strip('\n') \
        .replace('<li>', '') \
        .replace('</li>', '') \

    code_flag = False
    bold_flag = False
    italic_flag = False
    position = None
    for i, item in enumerate(block.split('\n')):
        if ordered:
            item = u'    ' + str(i + 1) + '. ' + item
        else:
            item = u'    \u2022 ' + item

        for word in item.split(" "):

            # _________ PREPARATION _________ #
            # inline code, bold and italic formatting
            word, position, code_flag, bold_flag, italic_flag = self.inline_formatting_preparation(word, position, code_flag, bold_flag, italic_flag)

            # _________ TEXT BLITTING _________ #
            # create surface to get width of the word to identify necessary linebreaks
            word = word + " "
            word = word.replace("&gt;", ">").replace("&lt;", "<")
            if code_flag:
                if position == 'first' or position == 'single':
                    x += self.code_padding
                surface = self.get_surface(word, 'code', bold_flag, italic_flag)
            else:
                surface = self.get_surface(word, block_type, bold_flag, italic_flag)

            if not(x + surface.get_width() < self.x + self.w):  # new line necessary
                y = y + prev_text_height + self.gap_line
                if ordered:
                    extra_width = self.get_surface(u'    ' + str(i + 1) + '. ', 'p').get_width()
                else:
                    extra_width = self.get_surface(u'    \u2022 ', 'p').get_width()

                x = start_of_line_x + extra_width

            if self.is_visible(y) and self.is_visible(y + surface.get_height()):
                self.draw_code_background(code_flag, word, x, y, position)
                self.screen.blit(surface, (x, y))

            prev_text_height = surface.get_height()  # update for next line

            # Update x for the next word
            x = x + surface.get_width()
            if code_flag and position in ('single', 'last'):
                x -= self.code_padding  # reduce empty space by padding.

            # _________ FORMATTING RESET FOR NEXT WORD _________ #
            bold_flag = False if bold_flag and position == 'last' else bold_flag
            code_flag = False if code_flag and (position == 'last' or position == 'single') else code_flag
            italic_flag = False if italic_flag and position == 'last' else italic_flag

        if i == len(block.split('\n')) - 1:
            return y  # return without adding to the last line

        y = y + prev_text_height + self.gap_line
        x = start_of_line_x

    return y
