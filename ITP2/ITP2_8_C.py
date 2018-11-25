import sys
import io
import time
import pprint

input_txt = """
9
0 blue 4
0 red 1
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

n = int(input())
arr = []
lines = sys.stdin.readlines()
ans = [None] * n
d = {}
for i in range(n):
    q, *arg = lines[i].split()
    key = arg[0]
    idx = bisect.bisect_left(arr, arg[0])
    if q == '0':    # insert
        if idx == len(arr) or arr[idx] != key:
            arr.insert(idx, key)
        d[key] = arg[1]
    elif q == '1':  # get
        ans[i] = d[key] if idx != len(arr) and arr[idx] == key else '0'
    elif q == '2':  # delete
        if idx < len(arr) and arr[idx] == key:
            del arr[idx]
            del d[key]
    elif q == '3':  # dump L R
        r_idx = bisect.bisect_right(arr, arg[1])
        ans[i] = '\n'.join([f'{key_} {d[key_]}' for key_ in arr[idx:r_idx]]) if (r_idx - idx) != 0 else None

[print(x) for x in ans if x is not None]


# -----------------------------
print("elapsed:", time.time() - start)
sys.stdin = sys.__stdin__