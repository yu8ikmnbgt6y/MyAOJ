import sys
import io
import time
import pprint

input_txt = """
0 0 2 0
10
-1 1
0 1
1 1
2 1
3 1
-1 -1
0 -1
1 -1
2 -1
3 -1
"""

sys.stdin = io.StringIO(input_txt); tmp = input()
#sys.stdin = open("CGL_1_C_in27.txt")
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

    def point_geometry(self, pt: Point) -> int:
        """
        [0:"Counter Clockwise", 1:"Clockwise", 2:"Online Back", 3:"Online Front", 4:"On Segment"]
        """
        vec_pt1_to_pt = Vector(self.pt1, pt)
        cross = self.cross(vec_pt1_to_pt)
        if cross > 0:
            return 0
        elif cross < 0:
            return 1
        else:           # cross == 0
            dot = self.dot(vec_pt1_to_pt)
            if dot < 0:
                return 2
            else:       # dot > 0
                if self.abs() < vec_pt1_to_pt.abs():
                    return 3
                else:
                    return 4

    def __repr__(self):
        return f"{self.pt1},{self.pt2}"


def main():
    p0_x, p0_y, p1_x, p1_y = map(int, input().split())
    p0 = Point(p0_x, p0_y)
    seg = Segment(p0, Point(p1_x, p1_y))
    num_query = int(input())

    ccw = {0: 'COUNTER_CLOCKWISE', 1: 'CLOCKWISE', 2: 'ONLINE_BACK', 3: 'ONLINE_FRONT', 4: 'ON_SEGMENT'}
    for i in range(num_query):
        p2_x, p2_y = map(int, input().split())
        ans = seg.point_geometry(Point(p2_x, p2_y))
        print(ccw[ans])
    return


main()
# -----------------------------
print("elapsed:", time.time()-start)
sys.stdin = sys.__stdin__