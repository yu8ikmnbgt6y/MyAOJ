import sys
import io
import time
import pprint

input_txt = """
50 20 21
41 11 29
"""

sys.stdin = io.StringIO(input_txt); tmp = input()
#sys.stdin = open("CGL_2_B_in17.test")
#sys.stdout = open("out.dat","w")
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
import math
from typing import Union, Tuple


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

    def norm(self):
        return pow(self.x, 2) + pow(self.y, 2)

    def abs(self):
        return math.sqrt(self.norm())

    def __repr__(self):
        return f"({self.x},{self.y})"


class Vector(Point):
    __slots__ = ['x', 'y', 'pt1', 'pt2']

    def __init__(self, pt1: Point, pt2: Point):
        super().__init__(pt2.x - pt1.x, pt2.y - pt1.y)
        self.pt1 = pt1
        self.pt2 = pt2

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def arg(self) -> float:
        return math.atan2(self.y, self.x)

    @staticmethod
    def polar(r, theta) -> Point:
        return Point(r * math.cos(theta), r * math.sin(theta))

    def __repr__(self):
        return f"{self.pt1},{self.pt2}"


class Segment(Vector):
    __slots__ = ['x', 'y', 'pt1', 'pt2']

    def __init__(self, pt1: Point, pt2: Point):
        super().__init__(pt1, pt2)

    def projection(self, pt: Point)-> Point:
        t = self.dot(Vector(self.pt1, pt)) / self.norm()
        return self.pt1 + self * t

    def reflection(self, pt: Point) -> Point:
        return self.projection(pt) * 2 - pt

    def is_intersected_with(self, other) -> bool:
        if (self.point_geometry(other.pt1) * self.point_geometry(other.pt2)) <= 0\
                and other.point_geometry(self.pt1) * other.point_geometry(self.pt2) <= 0:
            return True
        else:
            return False

    def point_geometry(self, pt: Point) -> int:
        """
        [-2:"Online Back", -1:"Counter Clockwise", 0:"On Segment", 1:"Clockwise",  2:"Online Front"]
        """
        vec_pt1_to_pt = Vector(self.pt1, pt)
        cross = self.cross(vec_pt1_to_pt)
        if cross > 0:
            return -1   # counter clockwise
        elif cross < 0:
            return 1    # clockwise
        else:           # cross == 0
            dot = self.dot(vec_pt1_to_pt)
            if dot < 0:
                return -2    # online back
            else:       # dot > 0
                if self.abs() < vec_pt1_to_pt.abs():
                    return 2    # online front
                else:
                    return 0    # on segment

    def cross_point(self, other) -> Point:
        d1 = abs(self.cross(Vector(self.pt1, other.pt1)))       # / self.abs()
        d2 = abs(self.cross(Vector(self.pt1, other.pt2)))       # / self.abs()
        t = d1 / (d1 + d2)
        return other.pt1 + other * t

    def distance_to_point(self, pt: Point) -> Union[int, float]:
        vec_pt1_to_pt = Vector(self.pt1, pt)
        if self.dot(vec_pt1_to_pt) <= 0:
            return vec_pt1_to_pt.abs()
        vec_pt2_to_pt = Vector(self.pt2, pt)
        if Vector.dot(self * -1, vec_pt2_to_pt) <= 0:
            return vec_pt2_to_pt.abs()
        return (self.projection(pt) - pt).abs()

    def distance_to_segment(self, other) -> Union[int, float]:
        if self.is_intersected_with(other):
            return 0.0
        else:
            return min(
                self.distance_to_point(other.pt1),
                self.distance_to_point(other.pt2),
                other.distance_to_point(self.pt1),
                other.distance_to_point(self.pt2)
            )

    def __repr__(self):
        return f"{self.pt1},{self.pt2}"


class Circle(Point):
    __slots__ = ['x', 'y', 'r']
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def cross_point_with_circle(self, other) -> Tuple[Point, Point]:
        vec_self_to_other = Vector(self, other)
        vec_abs = vec_self_to_other.abs()
        # if vec_abs > (self.r + other.r):
        #     raise AssertionError
        t = ((pow(self.r, 2) - pow(other.r, 2)) / pow(vec_abs, 2) + 1) / 2
        pt = (other - self) * t
        abs_from_pt = math.sqrt(pow(self.r, 2) - pt.norm())
        inv = Point(vec_self_to_other.y / vec_abs,  - vec_self_to_other.x / vec_abs) * abs_from_pt
        pt_ = self + pt
        return (pt_ + inv), (pt_ - inv)

    def cross_point_with_circle2(self, other) -> Tuple[Point, Point]:
        vec_self_to_other = Vector(self, other)
        vec_abs = vec_self_to_other.abs()
        # if vec_abs > (self.r + other.r):
        #     raise AssertionError

        theta_base_to_other = vec_self_to_other.arg()
        theta_other_to_pt = math.acos((pow(self.r, 2) + pow(vec_abs, 2) - pow(other.r, 2)) / (2 * self.r * vec_abs))

        return self + Vector.polar(self.r, theta_base_to_other + theta_other_to_pt),\
               self + Vector.polar(self.r, theta_base_to_other - theta_other_to_pt)

    def __repr__(self):
        return f"({self.x},{self.y}), {self.r}"


def main():
    c1x, c1y, c1r = map(int, input().split())
    c2x, c2y, c2r = map(int, input().split())

    pt1, pt2 = Circle(c1x, c1y, c1r).cross_point_with_circle2(Circle(c2x, c2y, c2r))

    if pt1.x > pt2.x or (pt1.x == pt2.x and pt1.y > pt2.y):
        tmp = pt1
        pt1 = pt2
        pt2 = tmp

    print(" ".join(map('{:.10f}'.format, [pt1.x, pt1.y, pt2.x, pt2.y])))

    return


main()
# -----------------------------
print("elapsed:", time.time()-start)
sys.stdin = sys.__stdin__