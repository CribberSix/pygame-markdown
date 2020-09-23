import pygame


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
