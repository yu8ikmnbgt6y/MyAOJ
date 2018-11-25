import sys
import io
import time
import pprint

input_txt = """
20
0 3 1 100 2 2 4 5
1 3 0 100 2 3 3 1
2 5 1 3 0 2 4 10 5 12 3 1
3 2 2 1 1 1
4 3 0 5 2 10 5 2
5 4 4 2 2 12 6 19 7 3
6 4 5 19 11 4 10 3 7 17
7 5 5 3 6 17 10 1000 9 2 8 5
8 2 7 5 9 5
9 4 8 5 7 2 10 1 13 50
10 5 9 1 7 1000 6 3 11 8 12 100
11 3 12 7 10 8 6 4
12 5 10 100 11 7 15 2 14 5 13 1
13 2 12 1 9 50
14 4 15 2 12 5 18 3 16 3
15 2 12 2 14 2
16 2 14 3 17 5
17 3 18 1 19 1 16 5
18 3 14 3 17 1 19 3
19 2 18 3 17 1
"""

#sys.stdin = open("ALDS1_11_D_in11.txt","r")#io.StringIO(input_txt)

sys.stdin = io.StringIO(input_txt)
tmp = input()
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
import sys
from collections import defaultdict


def main():
    n = int(input())
    lines = sys.stdin.readlines()
    vertex_weights = defaultdict(list)
    for i in range(n):
        u, k, *vtx_wght = map(int, lines[i].split())
        for v_i in range(k):
            vertex_weights[u].append((vtx_wght[2*v_i], vtx_wght[2*v_i+1]))

    dist_from_0 = {}
    vertices = [(0, 0)]
    while len(dist_from_0) != n:
        vertices.sort(key=lambda x: x[1], reverse=True)
        vtx, vtx_dist = vertices.pop()
        dist_from_0[vtx] = vtx_dist

        neighbor_vtx = vertex_weights[vtx]

        for n_vtx, n_dist in neighbor_vtx:
            if n_vtx not in dist_from_0.keys():
                vertices.append((n_vtx, vtx_dist + n_dist))

        [vertices.remove(x) for x in vertices[:] if x[0] in dist_from_0]


    answers = [None] * n
    sorted_dist = sorted(dist_from_0.items(), key=lambda x: x[0])
    for i in range(n):
        answers[i] = f"{sorted_dist[i][0]} {sorted_dist[i][1]}"
    [print(ans) for ans in answers]
    return


main()
# -----------------------------
print("elapsed:", time.time()-start)
sys.stdin = sys.__stdin__
