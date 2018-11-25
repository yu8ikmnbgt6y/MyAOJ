import sys
import io
import time
import pprint

input_txt = """
10
0 blue 6
0 red 1
0 blue 4
0 white 5
1 red
1 blue
2 red
1 black
1 red
3 w z
"""

sys.stdin = io.StringIO(input_txt);input()
#sys.stdin = open('in.test')
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
import sys
import bisect
from collections import defaultdict

n = int(input())
arr = []
d = defaultdict(list)
lines = sys.stdin.readlines()
ans = [None] * n

for i in range(n):
    q, *arg = lines[i].split()
    key = arg[0]
    l_idx = bisect.bisect_left(arr, arg[0])
    r_idx = bisect.bisect_right(arr, arg[0])
    if q == '0':    # insert
        if l_idx == len(arr) or arr[l_idx] != key:
            arr.insert(l_idx, key)
        d[key].append(arg[1])
    elif q == '1':  # get
        if l_idx != r_idx:
            ans[i] = '\n'.join(d[key])
    elif q == '2':  # delete
        arr[l_idx:r_idx] = []
        if l_idx != r_idx:
            del d[key]
    elif q == '3':  # dump L R
        r_idx = bisect.bisect_right(arr, arg[1])
        if l_idx != r_idx:
            keys = arr[l_idx:r_idx]
            ans[i] = '\n'.join(['\n'.join([f'{k} {x}' for x in d[k]]) for k in keys])

[print(x) for x in ans if x is not None]


# -----------------------------
print("elapsed:", time.time() - start)
sys.stdin = sys.__stdin__