import sys
import io

input_txt="""
2
"""


sys.stdin = io.StringIO(input_txt)
tmp = input()


# copy the below part and paste to the submission form.
# ---------function------------
import math
sqrt3 = math.sqrt(3.0)

def koch_curve(n, i, pt1, pt2, pt_array):
    if i > n:
        return
    pt1x, pt1y = pt1
    pt2x, pt2y = pt2
    pts = (2/3 * pt1x + 1/3 * pt2x, 2/3 * pt1y + 1/3 * pt2y)
    ptt = (1/3 * pt1x + 2/3 * pt2x, 1/3 * pt1y + 2/3 * pt2y)
    ptx = ptt[0] - pts[0]
    pty = ptt[1] - pts[1]
    ptu = (1/2 * (ptx - sqrt3 * pty) + pts[0], 1/2 * (sqrt3 * ptx + pty) + pts[1])

    koch_curve(n, i+1, pt1, pts, pt_array)
    pt_array.append(pts)
    koch_curve(n, i+1, pts, ptu, pt_array)
    pt_array.append(ptu)
    koch_curve(n, i+1, ptu, ptt, pt_array)
    pt_array.append(ptt)
    koch_curve(n, i+1, ptt, pt2, pt_array)
    return

def main():
    n = int(input())
    pt_array = []
    begin = (0.0, 0.0)
    end = (100.0, 0.0)
    pt_array.append(begin)
    koch_curve(n, 1, begin, end, pt_array)
    pt_array.append(end)
    for pt in pt_array:
        print("{:.6f} {:.6f}".format(pt[0], pt[1]))

main()
# -----------------------------
sys.stdin = sys.__stdin__
