"""Manipulation of 2D-vectors."""

from __future__ import annotations

class Point:
    def __init__(self, x:float, y:float):
        self.x=x
        self.y=y
class Vector:
    def __init__(self, end:Point, start:Point):
        self.end=end
        self.start=start
        self.x = end.x - start.x
        self.y = end.y - start.y

def main():
    origin = Point(0, 0)
    point_A = Point(-2, -1)
    point_B = Point(3, 7)

    print(f"Point O: x={origin.x} y={origin.y}")
    print(f"Point A: x={point_A.x} y={point_A.y}")

    vector_OA = Vector(origin, point_A)
    vector_AB = Vector(point_A, point_B)

    print(f"Vector OA: dx={vector_OA.x} dy={vector_OA.y}")
    print(f"Vector AB: dx={vector_AB.x} dy={vector_AB.y}")


def main_2():
    v = Vector(1, 2)
    v2 = Vector(1, 0)
    print(v.dot_prod(v2))
    print(v2.dot_prod(v))


def main_3():
    v = Vector(1, 2)
    v2 = Vector(1, 0)
    print(-v)
    print(-(-v))
    print(v + v2)
    print(v - v2)
    print(v * 3)
    print(v2 * -10)


def main_4():
    point_B = Point(3, 7)
    vector_OB = Vector.from_origin(point_B)
    print(vector_OB)


if __name__ == "__main__":
    main()
    # main_2()
    # main_3()
    # main_4()




