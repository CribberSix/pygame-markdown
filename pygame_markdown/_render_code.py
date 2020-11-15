

def render_codeblock(self, block: str, block_type: str, y: int) -> int:
    """Renders a block of code.

    Warning: Each code line is represented in one physical line, there are no line-breaks inserted!
             If the code-line is too long, it might be blitted to the right of the area.

    :param self:  MarkdownRenderer
    :param block: string of text
    :param block_type: type of the text (e.g. headers, ordered/unordered lists, blockquotes, code etc)
    :param y: y-coordinate to start rendering on
    :return: y-coordinate after rendering is finished
    """


    start_of_line_x = self.x + self.indentation_code
    x = start_of_line_x  # for the start with the first line of block

    for i, line in enumerate(block.split('\n')):   # user-set lines in codeblocks
        # render background of line if visible before rendering the line
        if self.is_visible(y) and self.is_visible(y + self.get_surface('placeholder', 'code').get_height()):
            self.draw_codeblock_background(y)

        # render actual line
        for word in line.split(" "):
            word = word + " "
            # create surface to get width of the word to identify necessary linebreaks
            surface = self.get_surface(word, block_type)

            if self.is_visible(y) and self.is_visible(y + surface.get_height()):
                self.screen.blit(surface, (x, y))

            x = x + surface.get_width()  # update for next word
            prev_text_height = surface.get_height()  # update for next line

        if i == len(block.split('\n')) - 1:
            return y  # return without adding to the last line

        y = y + prev_text_height + self.gap_line
        x = start_of_line_x
    return y