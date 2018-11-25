import sys
import io
import time
import pprint

input_txt = """
3
"""

sys.stdin = io.StringIO(input_txt);input()
#sys.stdin = open('in.test')
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
n = int(input())
masks = [1 << x for x in range(n)]

for i in range(1 << n):
    sub = [idx for idx, mask in enumerate(masks) if i & mask != 0b00]
    print('{}: {}'.format(i, ' '.join(map(str, sub)))) if len(sub) != 0 else print(f'{i}:')

# -----------------------------
print("elapsed:", time.time() - start)
sys.stdin = sys.__stdin__