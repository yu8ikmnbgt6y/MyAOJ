import sys
import io
import time
import pprint

input_txt = """
10
0 2 1 1 2 3
1 2 3 3 2 1
2 2 3 1 6 10
3 1 4 1
4 1 7 1
5 2 3 1 6 1
6 2 3 1 8 1
7 2 5 1 8 4
8 1 9 100000
9 0
"""

#sys.stdin = open("ALDS1_11_D_in11.txt","r")#io.StringIO(input_txt)

#sys.stdin = io.StringIO(input_txt)
sys.stdin = open("ALDS1_12_C_in8.txt", 'r')
#tmp = input()
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
import sys
from collections import defaultdict
from typing import Dict


def find_shortest_distance(start_vertex: int, n: int,  relations: Dict[int, Dict]) -> Dict[int, int]:
    unreached_vertices = [x for x in range(1, n)]
    distance = {x: sys.maxsize for x in range(n)}
    distance[start_vertex] = 0
    vtx = None
    tmp_distance = [sys.maxsize for x in range(n)]
    for k, v in relations[start_vertex].items():
        tmp_distance[k] = v

    while True:
        min_dist = sys.maxsize
        for i in unreached_vertices:
            dist = tmp_distance[i]
            if dist < min_dist:
                min_dist = dist
                vtx = i
        if min_dist == sys.maxsize:
            break
        unreached_vertices.remove(vtx)
        distance[vtx] = min_dist
        neighbor_vertices = relations[vtx]
        for n_vtx, n_dist in neighbor_vertices.items():
            n_dist_from_start = distance[vtx] + n_dist
            tmp_dist = tmp_distance[n_vtx]
            if tmp_dist == sys.maxsize:
                tmp_distance[n_vtx] = n_dist_from_start
            else:
                if n_dist_from_start < tmp_dist:
                    tmp_distance[n_vtx] = n_dist_from_start
    return distance


def main():
    n = int(input())
    relations = defaultdict(dict)

    lines = sys.stdin.readlines()
    for i in range(n):
        u, k, *vtx_wght = map(int, lines[i].split())
        for v_i in range(k):
            relations[u][vtx_wght[2*v_i]] = vtx_wght[2*v_i+1]

    dist_from_0 = find_shortest_distance(0, n, relations)

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
