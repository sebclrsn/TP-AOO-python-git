"""Manipulation of 2D-vectors.

Note :
``from __future__ import annotations`` est nécessaire si l'on veut pouvoir utiliser une classe
en tant qu'annotation de type dans cette même classe ! Comme dans l'exemple suivant :
class Point:
    @classmethod
    def origin(cls) -> Point:  # "Error: Point not defined" serait levé sans l'utilisation de ``from __future__ import annotations``

"""

from __future__ import annotations

import math


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    @classmethod
    def origin(cls) -> Point:
        return Point(0, 0)

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    @classmethod
    def from_points(cls, tail: Point, head: Point) -> Vector:
        return Vector(head.x - tail.x, head.y - head.y)

    @property
    def magnitude(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def dot_prod(self, other: Vector) -> float:
        return self.x * other.x + self.y * other.y

    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)


def main():
    origin = Point.origin()
    point_A = Point(-2, -1)
    point_B = Point(3, 7)

    print(f"Point O: x={origin.x} y={origin.y}")
    print(f"Point A: x={point_A.x} y={point_A.y}")
    print(f"Point B: x={point_B.x} y={point_B.y}")


def main_2():
    v = Vector(1, 1)
    v2 = Vector(3, -2)

    print(f"{v.magnitude = }")
    print(f"{v.dot_prod(v2) = }")
    print(f"{v2.dot_prod(v) = }")


def main_3():
    v = Vector(1, 1)
    v2 = Vector(3, -2)

    print(f"{v + v2 =}")
    print(f"{-v =}")
    print(f"{- (-v) =}")
    print(f"{v - v2 =}")
    print(f"{v * 2 =}")
    print(f"{v2 * (-10) =}")


def main_4():
    origin = Point.origin()
    point_A = Point(-2, -1)
    point_B = Point(3, 7)

    vector_AB = Vector.from_points(point_A, point_B)
    vector_OA = Vector.from_points(origin, point_A)
    vector_AB = Vector.from_points(point_A, point_B)

    print(f"Vector OA: dx={vector_OA.x} dy={vector_OA.y}")
    print(f"Vector AB: dx={vector_AB.x} dy={vector_AB.y}")


if __name__ == "__main__":
    main()
    # main_2()
    # main_3()
    # main_4()
