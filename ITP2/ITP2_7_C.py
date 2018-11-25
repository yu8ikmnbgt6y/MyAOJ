import sys
import io
import time
import pprint

input_txt = """
9
0 1
0 2
0 3
2 2
1 1
1 2
1 3
0 4
3 2 4
"""

sys.stdin = io.StringIO(input_txt);input()
#sys.stdin = open('ITP2_7_B_in10.test')
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
import sys
import bisect
nq = int(input())
lines = sys.stdin.readlines()
ans = [None] * nq
arr = []
for i in range(nq):
    q, *arg = lines[i].split()
    x = int(arg[0])
    idx = bisect.bisect_left(arr,x)
    if q == '0':    # insert x
        if idx == len(arr) or arr[idx] != x:
            arr.insert(idx, x)
        ans[i] = str(len(arr))
    elif q == '1':   # find x
        ans[i] = '1' if idx < len(arr) and arr[idx] == x else '0'
    elif q == '2':           # delete x
        if idx < len(arr) and arr[idx] == x:
            del arr[idx]
    else:                   # dump L R
        r_idx = bisect.bisect_right(arr, int(arg[1]))
        ans[i] = '\n'.join(map(str, arr[idx:r_idx]))
    #print(q, *arg, '\t', arr)

[print(x) for x in ans if x]
# -----------------------------
print("elapsed:", time.time() - start)
sys.stdin = sys.__stdin__