def is_visible(self, y: int):
    """Checks whether a given point is within the currently visible area of the markdown area.
    The function is used to handle text which is longer than the specified height of the markdown area and
    during scrolling.

    :param self: MarkdownRenderer
    :param int y: y-coordinate
    :return: boolean
    """
    return not self.is_above_area(y) and not self.is_below_area(y)


def is_above_area(self, y: int):
    """Checks whether a given point is above the markdown area.

    :param self: MarkdownRenderer
    :param int y: y-coordinate
    :return: boolean
    """
    return y < self.y


def is_below_area(self, y: int):
    """Checks whether a given point is below the markdown area.

    :param self: MarkdownRenderer
    :param int y: y-coordinate
    :return: boolean
    """
    return y > self.y + self.h
