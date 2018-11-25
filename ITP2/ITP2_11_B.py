import sys
import io
import time
import pprint

input_txt = """
4
2 0 2
"""

sys.stdin = io.StringIO(input_txt);input()
#sys.stdin = open('in.test')
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
n = int(input())
k, *b_arr = map(int, input().split())
masks = [1 << x for x in range(n)]
b_mask = 0
for b in b_arr:
    b_mask += 1 << b

for i in range(1 << n):
    if i & b_mask != b_mask:
        continue
    sub = [idx for idx, mask in enumerate(masks) if i & mask != 0b00]
    print('{}: {}'.format(i, ' '.join(map(str, sub)))) if len(sub) != 0 else print(f'{i}:')

# -----------------------------
print("elapsed:", time.time() - start)
sys.stdin = sys.__stdin__