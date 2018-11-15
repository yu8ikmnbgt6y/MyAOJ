import sys
import io
import time
import pprint

input_txt = """
3
0 0 3 0 0 2 3 2
0 0 3 0 1 1 1 4
0 0 3 0 1 1 2 2
"""

sys.stdin = io.StringIO(input_txt); tmp = input()
#sys.stdout = open("out.dat","w")
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
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

    def dot(self, other):
        return self.vector.x * other.vector.x + self.vector.y * other.vector.y

    def cross(self, other):
        return self.vector.x * other.vector.y - self.vector.y * other.vector.x

    def projection(self, pt: Point)-> Point:


        return Point(1,1)

    def __repr__(self):
        return f"{self.pt1},{self.pt2},{self.vector}"


def main():
        n = int(input())
        for i in range(n):
            p0_x, p0_y, p1_x, p1_y, p2_x, p2_y, p3_x, p3_y = map(int, input().split())
            seg_1 = Segment(Point(p0_x, p0_y), Point(p1_x, p1_y))
            seg_2 = Segment(Point(p2_x, p2_y), Point(p3_x, p3_y))

            if seg_1.dot(seg_2) == 0:
                print('1')
            elif seg_1.cross(seg_2) == 0:
                print('2')
            else:
                print('0')
        return

main()
# -----------------------------
print("elapsed:", time.time()-start)
sys.stdin = sys.__stdin__