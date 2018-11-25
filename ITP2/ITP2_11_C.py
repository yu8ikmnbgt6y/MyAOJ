import sys
import io
import time
import pprint

input_txt = """
4
2 0 2 3
"""

sys.stdin = io.StringIO(input_txt);input()
#sys.stdin = open('in.test')
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
from itertools import combinations
n = int(input())
k, *b_arr = map(int, input().split())


def calc_int(arr):
    ret = 0
    for i in arr:
        ret += 1 << i
    return ret


subsets = []
for i in range(len(b_arr)+1):
    i_subsets = []
    for sub in combinations(b_arr, i):
        i_subsets.append((calc_int(sub), sub))
    subsets.extend(i_subsets)

subsets.sort()
for sub in subsets:
    print('{}: {}'.format(sub[0], ' '.join(map(str, sub[1])))) if len(sub[1]) != 0 else print(f'{sub[0]}:')

# -----------------------------
print("elapsed:", time.time() - start)
sys.stdin = sys.__stdin__