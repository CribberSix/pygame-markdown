import pygame


def draw_scrollbar(self):

    if self.pixels_showable_at_once >= self.pixels_entire_length:
        self.scrollbar = None
        return  # scrollbar hidden when there is nothing to scroll

    # Calculate position and dimensions of the scrollbar
    x = self.x + self.w
    w = 6  # must be an even number!
    y = int(self.y - (w/2) + (self.h * (self.pixel_first_showable / self.pixels_entire_length)))
    h = int((self.h - w) * (self.pixels_showable_at_once / self.pixels_entire_length))
    self.scrollbar = pygame.Rect(x, y, w, h)

    # top corner -> round
    pygame.draw.circle(self.screen, self.color_scrollbar, (int(x + (w/2)), y), int(w/2))
    # actual scrollbar
    pygame.draw.rect(self.screen, self.color_scrollbar, self.scrollbar)
    # bottom corner -> round
    pygame.draw.circle(self.screen, self.color_scrollbar, (int(x + (w/2)), y + h), int(w/2))


def scroll_up(self):
    # scrolling up
    self.pixel_first_showable -= self.pixel_scroll_step
    if self.pixel_first_showable < 0:  # reset to min
        self.pixel_first_showable = 0


def scroll_down(self):
    self.pixel_first_showable += self.pixel_scroll_step
    if self.pixel_first_showable > self.pixels_entire_length - self.pixels_showable_at_once: # reset to max
        self.pixel_first_showable = self.pixels_entire_length - self.pixels_showable_at_once
