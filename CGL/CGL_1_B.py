import sys
import io
import time
import pprint

input_txt = """
0 0 3 4
3
2 5
1 4
0 3
"""

sys.stdin = io.StringIO(input_txt); tmp = input()
#sys.stdout = open("out.dat","w")
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
import math
from typing import Union


class Point(object):
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[int, float]):
        return Point(self.x * other, self.y * other)

    def __repr__(self):
        return f"({self.x},{self.y})"


class Vector(Point):
    __slots__ = ['x', 'y', 'pt1', 'pt2']

    def __init__(self, pt1: Point, pt2: Point):
        from_pt1_to_pt2 = pt2 - pt1
        super().__init__(from_pt1_to_pt2.x, from_pt1_to_pt2.y)
        self.pt1 = pt1
        self.pt2 = pt2

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def norm(self):
        return pow(self.x, 2) + pow(self.y, 2)

    def abs(self):
        return math.sqrt(self.norm())

    def __repr__(self):
        return f"{self.pt1},{self.pt2}"


class Segment(Vector):
    __slots__ = ['x', 'y', 'pt1', 'pt2']

    def __init__(self, pt1: Point, pt2: Point):
        super().__init__(pt1, pt2)

    def projection(self, pt: Point)-> Point:
        t = self.dot(Vector(self.pt1, pt)) / pow(self.abs(), 2)
        return Point(self.pt1.x + t * self.x, self.pt1.y + t * self.y)

    def reflection(self, pt: Point) -> Point:
        return self.projection(pt) * 2 - pt

    def __repr__(self):
        return f"{self.pt1},{self.pt2}"


def main():
    p0_x, p0_y, p1_x, p1_y = map(int, input().split())
    seg = Segment(Point(p0_x, p0_y), Point(p1_x, p1_y))
    num_query = int(input())
    for i in range(num_query):
        pt_x, pt_y = map(int, input().split())
        reflection = seg.reflection(Point(pt_x, pt_y))
        print("{:.10f} {:.10f}".format(reflection.x, reflection.y))
    return


main()
# -----------------------------
print("elapsed:", time.time()-start)
sys.stdin = sys.__stdin__