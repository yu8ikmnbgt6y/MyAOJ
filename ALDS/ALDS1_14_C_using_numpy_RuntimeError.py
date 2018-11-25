import sys
import io
import time
import pprint

input_txt = """
4 5
00010
00101
00010
00100
3 2
10
01
10
"""

sys.stdin = io.StringIO(input_txt); tmp = input()
#sys.stdin = open('ALDS1_14_D_in11.test')
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
import numpy as np

def main():
    H, W = map(int, input().split())
    array_in = [list(map(int, list(input()))) for x in range(H)]
    array = np.array(array_in)
    R, C = map(int, input().split())
    pattern_in = [list(map(int, list(input()))) for x in range(R)]
    pattern = np.array(pattern_in)

    count = 0
    for i in range(H-R+1):
        for j in range(W-C+1):
            if (array[i:i+R, j:j+C] == pattern).all():
                print(i, j)
    return

main()
# -----------------------------
print("elapsed:", time.time()-start)
sys.stdin = sys.__stdin__
