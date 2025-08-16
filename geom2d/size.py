from geom2d.nums import are_close_enough

class Size:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, Size):
            return False

        return are_close_enough(self.width, other.width) \
            and are_close_enough(self.height, other.height)