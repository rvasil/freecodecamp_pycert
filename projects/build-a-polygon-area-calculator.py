from math import sqrt


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def __str__(self):
        return f"{type(self).__name__}(width={self._width}, height={self._height})"

    def set_width(self, width):
        self._width = width

    def set_height(self, height):
        self._height = height

    def get_area(self):
        return self._width * self._height

    def get_perimeter(self):
        return 2 * (self._width + self._height)

    def get_diagonal(self):
        return sqrt(self._width**2 + self._height**2)

    def get_picture(self):
        if self._width > 50 or self._height > 50:
            return "Too big for picture."
        return self._height * ("*" * self._width + "\n")

    def get_amount_inside(self, shape):
        return self._width // shape._width * self._height // shape._height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f"{type(self).__name__}(side={self._width})"

    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)


# rect = Rectangle(10, 5)
# print(rect.get_area())
# rect.set_height(3)
# print(rect.get_perimeter())
# print(rect)
# print(rect.get_picture())

# sq = Square(9)
# print(sq.get_area())
# sq.set_side(4)
# print(sq.get_diagonal())
# print(sq)
# print(sq.get_picture())

# rect.set_height(8)
# rect.set_width(16)
# print(rect.get_amount_inside(sq))


sq = Square(4)
print(sq)
print(sq.get_picture())
sq.set_width(5)
print(sq)
print(sq.get_picture())
sq.set_height(1)
print(sq)
print(sq.get_picture())
