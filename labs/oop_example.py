import platform
import sys


class Circle:
    def __init__(self, radius):
        self._radius = radius

    # Getter
    @property
    def radius(self):
        return self._radius

    # Setter
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    # Deleter
    @radius.deleter
    def radius(self):
        print("Deleting radius...")
        del self._radius


my_circle = Circle(3)
print("Initial radius:", my_circle.radius)  # Initial radius: 3

my_circle.radius = 8
print("After modifying the radius:", my_circle.radius)  # After modifying the radius: 8


def main():
    print(sys.executable, platform.python_version(), sep="\n")


if __name__ == "main":
    main()
