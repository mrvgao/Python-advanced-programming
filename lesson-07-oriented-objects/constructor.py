from dataclasses import dataclass
from heapq import nlargest


@dataclass
class Point:
    __match_args__ = ('x', 'y')
    x: int = 0
    y: int = 0


def some_func(points):
    patterns = [
        [Point, Point],
        [Point]
    ]

    for pat in patterns:
        pat = points


def match_func(*points):
    match points:
        case [Point(x=0, y=0), Point(x=0, y=0)]:
            print('haha')
        case [Point(x, y) as a, Point(c, d) as z]:
            print(a, z)
        case [float(), int()]:
            print('float and int')
        case [tuple(), Point(x, y)]:
            print('tuple and Point')
        case _:
            print('none of this')


if __name__ == '__main__':
    match_func(Point(0, 0))
    match_func(Point(0, 0), Point(-1, -1))
    match_func(0.1, 1)
    match_func(1, 2, 3)

