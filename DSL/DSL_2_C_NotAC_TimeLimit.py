import sys
import io
import time
import pprint

input_txt = """
6
2 1
2 2
4 2
6 2
3 3
5 4
2
2 4 0 4
4 10 2 5
"""

#sys.stdin = io.StringIO(input_txt); tmp = input()
sys.stdin = open("DSL_1_A_in14.txt")
#sys.stdout = open("out.dat","w")
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
import sys
from typing import List, Tuple

class Point:
    def __init__(self, point_id: int, point_x: int, point_y: int):
        self.point_id = point_id
        self.point_x = point_x
        self.point_y = point_y
        self.left_tree = None
        self.right_tree = None

    def __repr__(self):
        return f"{self.point_id},({self.point_x},{self.point_y}),l:{self.left_tree},r:{self.right_tree}"


class Two_Dimention_Tree:
    def __init__(self, points: List[Point]):
        self.points = points
        self.root = self.make_2d_tree(self.points, self.points[:], depth=0)

    def __repr__(self):
        return f"root:{self.root},\tpoints:{self.points}"

    def make_2d_tree(self, points: List[Point], nested_points: List[Point], depth=0):
        if len(nested_points) == 0:
            return None
        elif len(nested_points) == 1:
            return nested_points[0].point_id

        if depth & 0x0011 == 0x0000:
        #if depth % 2 == 0:
            #sort points for x
            nested_points.sort(key=lambda x: x.point_x)
        elif depth & 0x0011 == 0x0010:
        #else:
            #sort points for y
            nested_points.sort(key=lambda x: x.point_y)

        mid = len(nested_points) // 2
        mid_id = nested_points[mid].point_id

        points[mid_id].left_tree  = self.make_2d_tree(points, nested_points[:mid]  , depth+1)
        points[mid_id].right_tree = self.make_2d_tree(points, nested_points[mid+1:], depth+1)

        return mid_id


    num_points = 0
    points_in_roi = [0]

    def find_tree_in_roi(self, lb_x, rt_x, lb_y, rt_y, depth: int, parent: int):
        parent_point = self.points[parent]
        p_x, p_y = parent_point.point_x, parent_point.point_y
        if lb_x <= p_x <= rt_x and lb_y <= p_y <= rt_y:
            self.points_in_roi[self.num_points] = parent
            self.num_points += 1

        if depth & 0x0010 == 0x0000:
        #if depth % 2 == 0:
            # x-axis
            #if lb_x <= p_x and parent_point.left_tree != None:
            if parent_point.left_tree != None and lb_x <= p_x:
                self.find_tree_in_roi(lb_x, rt_x, lb_y, rt_y, depth+1, parent_point.left_tree)
            if parent_point.right_tree != None and p_x <= rt_x:
                self.find_tree_in_roi(lb_x, rt_x, lb_y, rt_y, depth+1, parent_point.right_tree)
        else:
            # y-axis
            if parent_point.left_tree != None and lb_y <= p_y:
                self.find_tree_in_roi(lb_x, rt_x, lb_y, rt_y, depth+1, parent_point.left_tree)
            if parent_point.right_tree != None and p_y <= rt_y:
                self.find_tree_in_roi(lb_x, rt_x, lb_y, rt_y, depth+1, parent_point.right_tree)
        return

    def find_points_in_roi(self, lb_x, rt_x, lb_y, rt_y)  -> Tuple[int, List[int]]:
        self.num_points = 0
        self.points_in_roi = [None] * 100

        self.find_tree_in_roi(lb_x, rt_x, lb_y, rt_y, depth=0, parent=self.root)
        return self.num_points, self.points_in_roi


def main():
    lines = sys.stdin.readlines()
    num_points = int(lines[0])
    lines = lines[1:]

    points = [None] * num_points
    for i in range(num_points):
        x, y = map(int, lines[i].split())
        points[i] = Point(i, x, y)
    lines = lines[num_points:]

    two_d_tree = Two_Dimention_Tree(points)

    num_query = int(lines[0])
    lines = lines[1:]
    answers = [""] * 2020000
    num_answers = 0
    for i in range(num_query):
        lb_x, rt_x, lb_y, rt_y = map(int, lines[i].split())
        n, point_ids_roi = two_d_tree.find_points_in_roi(lb_x, rt_x, lb_y, rt_y)
        if n != 0:
            point_ids_roi = point_ids_roi[:n]
            point_ids_roi.sort()
            for i in range(n):
                answers[num_answers] = point_ids_roi[i]
                num_answers += 1
        num_answers += 1

    #[print(answers[i]) for i in range(num_answers)]
    return


main()
# -----------------------------
print("elapsed:", time.time()-start)
sys.stdin = sys.__stdin__