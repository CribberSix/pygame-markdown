import pygame


def mouse_within_md_area(self, mouse_x, mouse_y) -> bool:
    """ Returns True if the given coordinates are within the console area of the pygame window, otherwise False.

    :param self: MarkdownRenderer
    :param mouse_x: x-coordinate of mouse position
    :param mouse_y: y-coordinate of mouse position
    :return: boolean
    """

    return self.x - self.margin < mouse_x < (self.x + self.w + (2* self.margin)) and self.y - self.margin < mouse_y < (self.h + self.y + 2 * self.margin)


def handle_mouse_input(self, pygame_events, mouse_x, mouse_y, mouse_pressed):
    """

    :param self: MarkdownRenderer
    :param pygame_events: return value of 'pygame.event.get()'
    :param mouse_x: x-coordinate of mouse position
    :param mouse_y: y-coordinate of mouse position
    :param mouse_pressed: return value of 'pygame.mouse.get_pressed()'
    :return: None
    """
    for event in pygame_events:
        # Mouse scrolling wheel should only work if it is within the coding area.
        if event.type == pygame.MOUSEBUTTONDOWN and self.mouse_within_md_area(mouse_x, mouse_y):
            if event.button == 4 and self.pixel_first_showable > 0:
                self.scroll_up()
            elif event.button == 5 and self.pixel_first_showable + self.pixels_showable_at_once < self.pixels_entire_length:
                self.scroll_down()

            if event.button == 1:
                if self.scrollbar.collidepoint(mouse_x, mouse_y):
                    self.scroll_start_y = mouse_y
                    self.scroll_dragging = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.scroll_dragging = False

    if mouse_pressed[0] == 1 and self.scroll_dragging:
        # left mouse is being pressed after click on scrollbar
        if mouse_y > self.scroll_start_y:  # dragged lower
            self.scroll_down()
        elif mouse_y < self.scroll_start_y:  # dragged higher
            self.scroll_up()

