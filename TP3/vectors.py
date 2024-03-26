"""Manipulation of 2D-vectors."""

from __future__ import annotations


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

    print(f"{v.magnitude() = }")  # or v.magnitude if using the @property decorator
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
