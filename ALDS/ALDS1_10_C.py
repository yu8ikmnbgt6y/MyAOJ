import sys
import io

input_txt = """
1
ABCDE
ACEABC
"""


import pprint
sys.stdin = io.StringIO(input_txt)
tmp = input()

# copy the below part and paste to the submission form.
# ---------function------------
import sys
def longest_common_subsequence(line1, line2):
    n_rows = len(line2) + 1
    array = [0] * n_rows

    ix_ = [x for x in range(n_rows)]
    ix = [x+1 for x in range(n_rows)]

    for l1_letter in line1:
        prev_array = array[:]
        for i_row_, i_row, l2_letter in zip(ix_, ix, line2):
            if l1_letter == l2_letter:
                array[i_row] = prev_array[i_row_] + 1
            else:
                up = prev_array[i_row]
                left = array[i_row_]
                array[i_row] = up if up > left else left
    return array[-1]

calc_time = False
if calc_time: import time; start = time.time()
def main():
    n = int(input())
    lines = sys.stdin.readlines()
    for i in range(0, 2*n, 2):
        ans = longest_common_subsequence(lines[i].rstrip(), lines[i+1].rstrip())
        print(ans)
    return

main()
if calc_time:print("elapsed:",time.time()-start)
# -----------------------------
sys.stdin = sys.__stdin__
