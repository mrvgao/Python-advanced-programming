from dataclasses import dataclass

@dataclass
class Point:
    __match_args__ = ('x', 'y')
    x : int = 0
    y : int = 0

class Line:
    def __init__(self, *p):
        match p:
            case (Point(a, b), Point(c, d)):
                pass
            case (float, int):
                pass
            case (tuple, Point):
                pass
            case Point:
                pass