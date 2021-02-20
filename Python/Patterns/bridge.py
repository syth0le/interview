from abc import ABCMeta, abstractmethod


# Implementor
class IDrawingAPI(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def drawCircle(self, x, y, radius):
        pass


# ConcreteImplementor 1/3
class DrawingAPI1(IDrawingAPI):

    def drawCircle(self, x, y, radius):
        print(f"API1.circle at {x}:{y} radius {radius}")


# ConcreteImplementor 2/3
class DrawingAPI2(IDrawingAPI):

    def drawCircle(self, x, y, radius):
        print(f"API2.circle at {x}:{y} radius {radius}")


# ConcreteImplementor 3/3
class DrawingAPI3(IDrawingAPI):

    def drawCircle(self, x, y, radius):
        print(f"API3.circle at {x}:{y} radius {radius}")


# Abstraction
class Shape:
    # Low-level
    def draw(self):
        pass

    # High-level
    def resizeByPercentage(self, pct):
        pass


# Refined Abstraction
class CircleShape(Shape):
    def __init__(self, x, y, radius, drawingAPI):
        self.__x = x
        self.__y = y
        self.__radius = radius
        self.__drawingAPI = drawingAPI

    # low-level i.e. Implementation specific
    def draw(self):
        self.__drawingAPI.drawCircle(self.__x, self.__y, self.__radius)

    # high-level i.e. Abstraction specific
    def resizeByPercentage(self, pct):
        self.__radius *= pct


def main():
    shapes = [
        CircleShape(1, 2, 3, DrawingAPI1()),
        CircleShape(5, 7, 11, DrawingAPI2()),
        CircleShape(4, 13, 17, DrawingAPI3())
    ]

    for shape in shapes:
        shape.resizeByPercentage(2.5)
        shape.draw()


if __name__ == "__main__":
    main()
