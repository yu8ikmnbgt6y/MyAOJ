import sys
import io
import time
import pprint

input_txt = """
5 3
"""

sys.stdin = io.StringIO(input_txt);input()
#sys.stdin = open('in.test')
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
from itertools import combinations


def calc_int(arr):
    ret = 0
    for i in arr:
        ret += 1 << i
    return ret


n, k = map(int, input().split())
subsets = []
for sub in combinations(range(n), k):
    subsets.append((calc_int(sub), sub))
subsets.sort()

for sub in subsets:
    print('{}: {}'.format(sub[0], ' '.join(map(str, sub[1])))) if len(sub[1]) != 0 else print(f'{sub[0]}:')

# -----------------------------
print("elapsed:", time.time() - start)
sys.stdin = sys.__stdin__