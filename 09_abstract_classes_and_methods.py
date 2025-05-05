from abc import ABC, abstractmethod

class Shape(ABC):
    
    """Abstract base class for geometric shapes."""

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the shape.
        Must be implemented by subclasses.
        """
        pass

class Rectangle(Shape):
    """
    Rectangle class that inherits from Shape and implements the area method.
    """

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


if __name__ == '__main__':
    react = Rectangle(5, 3)
    print(f'Area of Rectangle is: {react.area}')