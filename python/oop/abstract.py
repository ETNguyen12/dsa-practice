from abc import ABC, abstractmethod

class Shape(ABC):
    sides = 4
    length = 4

    @abstractmethod
    def perimeter(self) -> int:
        ...


class Triangle(Shape):

    def __init__(self, length):
        self.sides = 3
        self.length = length

    def perimeter(self):
        return self.sides * self.length 


class Pentagon(Shape):

    def __init__(self, length):
            self.sides = 5
            self.length = length

    def perimeter(self) -> int:
        return self.sides * self.length

if __name__ == '__main__':
    triangle = Triangle(5)
    pentagon = Pentagon(6)

    print(triangle.perimeter())
    print(pentagon.perimeter())