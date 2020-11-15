import pygame


def get_surface(self, word: str, t_type: str, strong=False, italic=False) -> pygame.Surface:
    """ Returns rendered surface of a string (word) based on Markdown text types.

    :param self: MarkdownRenderer
    :param word: word to get a surface from
    :param t_type: the type of the text
    :param strong: boolean to signal strong/bold text
    :param italic: boolean to signal italicized text
    :return:  pygame.Surface
    """

    if strong:
        # headers are already bold and code cannot be bold -> only applicable to text or quotes.
        self.font_text.set_bold(True)
        self.font_quote.set_bold(True)
    if italic:
        self.font_text.set_italic(True)
        self.font_quote.set_italic(True)

    if t_type == 'h1':
        surface = self.font_header.render(word, True, self.color_font)
    elif t_type == 'h2':
        surface = self.font_header2.render(word, True, self.color_font)
    elif t_type == 'h3':
        surface = self.font_header3.render(word, True, self.color_font)

    elif t_type == 'code':
        surface = self.font_code.render(word, True, self.color_font)
    elif t_type == 'codeblock':
        surface = self.font_code.render(word, True, self.color_font)

    elif t_type == 'blockquote':
        surface = self.font_quote.render(word, True, self.color_quote)

    elif t_type in ('ol', 'ul'):  # un-/ordered lists
        surface = self.font_text.render(word, True, self.color_font)

    elif t_type == 'p':  # normal text paragraph
        surface = self.font_text.render(word, True, self.color_font)

    else:
        surface = self.font_text.render(word, True, self.color_font)

    if strong:
        self.font_text.set_bold(False)
        self.font_quote.set_bold(False)
    if italic:
        self.font_text.set_italic(False)
        self.font_quote.set_italic(False)

    return surface