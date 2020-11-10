import pygame


def mouse_within_md_area(self, mouse_x, mouse_y) -> bool:
    """ Returns True if the given coordinates are within the console area of the pygame window, otherwise False.

    :param self: MarkdownRenderer
    :param mouse_x: x-coordinate of mouse position
    :param mouse_y: y-coordinate of mouse position
    :return: boolean
    """

    return self.x < mouse_x < (self.x + self.w) and self.y < mouse_y < (self.h + self.y)


def handle_mouse_input(self, pygame_events, mouse_x, mouse_y):
    """

    :param self: MarkdownRenderer
    :param pygame_events: return value of 'pygame.event.get()'
    :param mouse_x: x-coordinate of mouse position
    :param mouse_y: y-coordinate of mouse position
    :return: None
    """
    for event in pygame_events:
        # Mouse scrolling wheel should only work if it is within the coding area.
        if event.type == pygame.MOUSEBUTTONDOWN and self.mouse_within_md_area(mouse_x, mouse_y):
            if event.button == 4 and self.pixel_first_showable > 0:
                # scrolling up
                self.pixel_first_showable -= self.pixel_scroll_step
                if self.pixel_first_showable < 0:  # reset to min
                    self.pixel_first_showable = 0
            elif event.button == 5 and self.pixel_first_showable + self.pixels_showable_at_once < self.pixels_entire_length:
                # scrolling down
                self.pixel_first_showable += self.pixel_scroll_step
                if self.pixel_first_showable > self.pixels_entire_length - self.pixels_showable_at_once:
                    self.pixel_first_showable = self.pixels_entire_length - self.pixels_showable_at_once  # reset to max
