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

sys.stdin = open("ALDS1_11_D_in11.txt","r")#io.StringIO(input_txt)

#sys.stdin = io.StringIO(input_txt)
sys.stdin = open("ALDS1_12_C_in8.txt", 'r')
#tmp = input()
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
import sys
from collections import defaultdict
import heapq

def main():
    n = int(input())
    lines = sys.stdin.readlines()
    neighbor_vertices = defaultdict(dict)   # {vertex: weight}
    for i in range(n):
        u, k, *vertex_weight = map(int, lines[i].split())
        for v_i in range(k):
            neighbor_vertices[u][vertex_weight[2*v_i]] = vertex_weight[2*v_i+1]

    distance = [sys.maxsize for x in range(n)]
    distance[0] = 0

    start = 0
    heap = []       # [(distance_from_starting_vertex, vertex)]
    heapq.heappush(heap, (0, start))
    done = [True] + [False] * (n-1)

    while len(heap) != 0:
        dist_from_start, vertex = heapq.heappop(heap)
        neighbor_vtx_weight = neighbor_vertices[vertex]
        for vertex, dist_from_vertex in neighbor_vtx_weight.items():
            if not done[vertex]:
                new_dist = dist_from_start + dist_from_vertex
                if distance[vertex] > new_dist:
                    distance[vertex] = new_dist
                    #print("push",new_dist,k)
                    heapq.heappush(heap, (new_dist, vertex))

    for i in range(n):
        print(i, distance[i])
    return




main()
# -----------------------------
print("elapsed:", time.time()-start)
sys.stdin = sys.__stdin__
