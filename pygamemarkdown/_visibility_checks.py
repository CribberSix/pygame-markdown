
def is_visible(self, y):
    return not self.is_above_area(y) and not self.is_below_area(y)


def is_above_area(self, y):
    return y < self.y


def is_below_area(self, y):
    return y > self.y + self.h

