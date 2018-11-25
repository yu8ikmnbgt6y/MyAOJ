import sys
import io
import time
import pprint

input_txt = """
6
30 35
35 15
15 5
5 10
10 20
20 25
"""

sys.stdin = io.StringIO(input_txt)
tmp = input()
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------


def least_multiplication(mtx):
    N = len(mtx)
    mul = [[None] * N for x in range(N)]

    for i in range(N):
        mul[i][i] = 0
    #pprint.pprint(mul)

    for chain in range(1, N):
        for begin in range(N-chain):
            end = begin + chain
            cand = []
            for j in range(begin, end):
                left = mul[begin][j]
                down = mul[j+1][end]
                this = mtx[begin][0] * mtx[j][1] * mtx[end][1]
                cand.append(left + down + this)
            mul[begin][begin+chain] = min(cand)
        #pprint.pprint(mul)
    return mul[0][N-1]


def main():
    n = int(input())
    matrices = []
    for i in range(n):
        col, row = map(int, input().split())
        matrices .append((col, row))
    ans = least_multiplication(matrices)
    print(ans)


main()
# -----------------------------
print("elapsed:", time.time()-start)
sys.stdin = sys.__stdin__