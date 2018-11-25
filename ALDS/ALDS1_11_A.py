import sys
import io
import time
import pprint

input_txt = """
6
1 2 2 4
2 1 5
3 2 5 6
4 0
5 1 4
6 1 6
"""

sys.stdin = io.StringIO(input_txt)
tmp = input()
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
import sys
def main():
    n = int(input())
    lines = sys.stdin.readlines()
    outputs = [None] * n
    str_range = [str(i) for i in range(1, n+1)]
    for i in range(n):
        idx, idx_n, *idx_vertices = lines[i].rstrip().split()
        outputs[i] = ['1' if str_i in idx_vertices else '0' for str_i in str_range]

    [print(" ".join(outputs[i])) for i in range(n)]


main()
# -----------------------------
print("elapsed:", time.time()-start)
sys.stdin = sys.__stdin__