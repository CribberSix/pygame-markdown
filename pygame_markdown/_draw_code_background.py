import pygame
import pygame.gfxdraw


def draw_code_background(self, code_flag, word, x, y, position):
    """ Draws a background rectangle behind inline-code.

    :param self: MarkdownRenderer
    :param code_flag: inline-code flag
    :param word: the word for which the background will be rendered.
    :param x: x-coordinate
    :param y: y-coordinate
    :param position: position of the word in the context of a multi-word inline-code subtext.
    :return: None
    """
    if code_flag:
        if position == 'last':  # remove last char (whitespace) from background-surface
            word = word[:-1]

        # blit colored background rectangle
        if code_flag:
            word_surface = self.get_surface(word, 'code')
        else:
            word_surface = self.get_surface(word, 'text')
        width = word_surface.get_width() + (self.code_padding * 2)
        height = word_surface.get_height()
        draw_rounded_rect(self.screen, pygame.Rect(x - self.code_padding, y, width, height),
                          self.color_code_background, 3)


def draw_codeblock_background(self, y):
    """ Draws the background for an entire line of a codeblock

    :param self: MarkdownRenderer
    :param y: y-coordinate
    :return: None
    """

    height_of_line = self.get_surface('placeholder', 'code').get_height()

    x_coordinate = self.x + (0.5 * self.indentation_code)
    width = self.w - self.indentation_code

    y_coordinate = y - self.gap_line
    height = height_of_line + (2 * self.gap_line)
    draw_rounded_rect(self.screen, pygame.Rect(x_coordinate, y_coordinate, width, height),
                      self.color_code_background, 5)


def draw_rounded_rect(surface, rect, color, corner_radius):
    """ Draw a rectangle with rounded corners.
    We use anti-aliased circles to make the corners smoother
    """
    if rect.width < 2 * corner_radius or rect.height < 2 * corner_radius:
        raise ValueError(f"Both height (rect.height) and width (rect.width) must be > 2 * corner radius ({corner_radius})")

    # need to use anti aliasing circle drawing routines to smooth the corners
    pygame.gfxdraw.aacircle(surface, rect.left+corner_radius, rect.top+corner_radius, corner_radius, color)
    pygame.gfxdraw.aacircle(surface, rect.right-corner_radius-1, rect.top+corner_radius, corner_radius, color)
    pygame.gfxdraw.aacircle(surface, rect.left+corner_radius, rect.bottom-corner_radius-1, corner_radius, color)
    pygame.gfxdraw.aacircle(surface, rect.right-corner_radius-1, rect.bottom-corner_radius-1, corner_radius, color)

    pygame.gfxdraw.filled_circle(surface, rect.left+corner_radius, rect.top+corner_radius, corner_radius, color)
    pygame.gfxdraw.filled_circle(surface, rect.right-corner_radius-1, rect.top+corner_radius, corner_radius, color)
    pygame.gfxdraw.filled_circle(surface, rect.left+corner_radius, rect.bottom-corner_radius-1, corner_radius, color)
    pygame.gfxdraw.filled_circle(surface, rect.right-corner_radius-1, rect.bottom-corner_radius-1, corner_radius, color)

    rect_tmp = pygame.Rect(rect)

    rect_tmp.width -= 2 * corner_radius
    rect_tmp.center = rect.center
    pygame.draw.rect(surface, color, rect_tmp)

    rect_tmp.width = rect.width
    rect_tmp.height -= 2 * corner_radius
    rect_tmp.center = rect.center
    pygame.draw.rect(surface, color, rect_tmp)
