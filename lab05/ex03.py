import random

class Point:
    def __init__(self, *coords):
        self._coords = []
        for coord in coords:
            if isinstance(coord, (int, float)):
                self._coords.append(coord)
            else:
                raise TypeError("Coordinates must be int or float type")

    def getRandomNumbers(self):
        return [random.randint(-100, 100) for x in self._coords]

    def __repr__(self) -> str:
        result = ""
        for coord in self._coords:
            result += str(coord) + " "
        return result

    def __len__(self):
        return len(self._coords)


point1 = Point(1,2)
print(point1)
point2 = Point(1,2,3)
print(point2)
point3 = Point(1,2,3,4)
print(point3)
point4 = Point(1,2,3,4,5)
print(point4)

print(point4.getRandomNumbers())
print(len(point4))
