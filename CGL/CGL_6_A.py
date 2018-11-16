import sys
import io
import time
import pprint

input_txt = """
9
2 1 2 8
1 3 11 3
4 2 4 4
3 4 9 4
5 2 5 5
7 2 7 7
9 4 9 5
10 0 10 6
4 7 7 7
"""

#sys.stdin = io.StringIO(input_txt); tmp = input()
sys.stdin = open("CGL_6_A_in40.test")
#sys.stdout = open("out.dat","w")
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
import sys
import bisect

def main():
    num_segments = int(input())
    events = [None] * num_segments * 2
    num_events = 0

    lines = sys.stdin.readlines()
    for line in lines:
        pt1_x, pt1_y, pt2_x, pt2_y = map(int, line.split())
        if pt1_x == pt2_x:
            if pt1_y > pt2_y:
                pt1_y, pt2_y = pt2_y, pt1_y
            events[num_events] = (pt1_y, pt1_x, 0)
            num_events += 1
            events[num_events] = (pt2_y, pt2_x, 2)
            num_events += 1
        elif pt1_y == pt2_y:
            if pt1_x > pt2_x:
                pt1_x, pt2_x = pt2_x, pt1_x
            events[num_events] = (pt1_y, (pt1_x, pt2_x), 1)
            num_events += 1
        else:
            raise AssertionError

    events = events[:num_events]
    events.sort(key=lambda x: (x[0], x[2]))

    cross_count = 0
    vertical = []
    for event in events:
        if event[2] == 0:
            bisect.insort_left(vertical, event[1])
        elif event[2] == 2:
            i = bisect.bisect_left(vertical, event[1])
            del vertical[i]
        else:   # horizontal
            left_x, right_x = event[1][0], event[1][1]
            for v_x in vertical:
                if left_x <= v_x <= right_x:
                    cross_count += 1
    print(cross_count)


main()
# -----------------------------
print("elapsed:", time.time()-start)
sys.stdin = sys.__stdin__