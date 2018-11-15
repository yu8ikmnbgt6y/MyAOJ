import sys
import io
import time
import pprint

input_txt = """
0 0 2 0
3
-1 1
0 1
1 1
"""

sys.stdin = io.StringIO(input_txt); tmp = input()
#sys.stdout = open("out.dat","w")
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"({self.x},{self.y})"


class Segment:
    def __init__(self, x: Point, y: Point):
        self.pt1 = x
        self.pt2 = y
        self.vector = self.pt2 - self.pt1
        self.norm = pow(self.vector.x, 2) + pow(self.vector.y, 2)
        self.abs = math.sqrt(self.norm)

    def dot(self, other):
        return self.vector.x * other.vector.x + self.vector.y * other.vector.y

    def cross(self, other):
        return self.vector.x * other.vector.y - self.vector.y * other.vector.x

    def projection(self, pt: Point)-> Point:
        vec_p1_to_pt = Segment(self.pt1, pt)
        t = self.dot(vec_p1_to_pt) / self.abs
        x = self.pt1.x + t / self.abs * self.vector.x
        y = self.pt1.y + t / self.abs * self.vector.y
        return Point(x, y)

    def __repr__(self):
        return f"{self.pt1},{self.pt2},{self.vector}"


def main():
    p0_x, p0_y, p1_x, p1_y = map(int, input().split())
    seg_1 = Segment(Point(p0_x, p0_y), Point(p1_x, p1_y))
    num_query = int(input())
    for i in range(num_query):
        pt_x , pt_y = map(int, input().split())
        proj = seg_1.projection(Point(pt_x, pt_y))

        print("{:.10f} {:.10f}".format(proj.x, proj.y))
    return

main()
# -----------------------------
print("elapsed:", time.time()-start)
sys.stdin = sys.__stdin__