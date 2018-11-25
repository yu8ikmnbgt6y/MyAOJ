import sys
import io
import time
import pprint

input_txt = """
20
 -1 100 2 -1 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
 100 -1 3 1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
 2 3 -1 1 10 12 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
 -1 1 1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
 5 -1 10 -1 -1 2 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
 -1 -1 12 -1 2 -1 19 3 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
 -1 -1 -1 -1 -1 19 -1 17 -1 -1 3 4 -1 -1 -1 -1 -1 -1 -1 -1
 -1 -1 -1 -1 -1 3 17 -1 5 2 1000 -1 -1 -1 -1 -1 -1 -1 -1 -1
 -1 -1 -1 -1 -1 -1 -1 5 -1 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
 -1 -1 -1 -1 -1 -1 -1 2 5 -1 1 -1 -1 50 -1 -1 -1 -1 -1 -1
 -1 -1 -1 -1 -1 -1 3 1000 -1 1 -1 8 100 -1 -1 -1 -1 -1 -1 -1
 -1 -1 -1 -1 -1 -1 4 -1 -1 -1 8 -1 7 -1 -1 -1 -1 -1 -1 -1
 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 100 7 -1 1 5 2 -1 -1 -1 -1
 -1 -1 -1 -1 -1 -1 -1 -1 -1 50 -1 -1 1 -1 -1 -1 -1 -1 -1 -1
 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 5 -1 -1 2 3 -1 3 -1
 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 2 -1 2 -1 -1 -1 -1 -1
 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 3 -1 -1 5 -1 -1
 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 5 -1 1 1
 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 3 -1 -1 1 -1 3
 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 1 3 -1
"""

#sys.stdin = open("ALDS1_11_D_in11.txt","r")#io.StringIO(input_txt)

sys.stdin = io.StringIO(input_txt)
tmp = input()
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
import sys
from collections import defaultdict

def push_vertex(vtx: int,queue: list, weights: dict, done: dict):
    queue.extend(weights[vtx])
    done[vtx] = True
    [queue.remove(x) for x in queue[:] if done[x[0]]]
    del weights[vtx]
    queue.sort(key=lambda x: x[1], reverse=True)
    return


def main():
    n = int(input())
    weights = defaultdict(list)
    for i in range(n):
        for idx, weight in enumerate(input().split()):
            if weight != '-1':
                weights[i+1].append((idx+1, int(weight)))
    done = {}
    for i in weights.keys():
        done[i] = False
    mst_weights = 0
    queue = []
    vtx = [*weights][0]
    push_vertex(vtx, queue, weights, done)

    while len(weights) != 0:
        new_vtx, new_vtx_weight = queue.pop()
        mst_weights += new_vtx_weight
        #print(f"connect to {new_vtx} ,weight={new_vtx_weight}")
        push_vertex(new_vtx, queue, weights, done)

    print(mst_weights)
    return

main()
# -----------------------------
print("elapsed:", time.time()-start)
sys.stdin = sys.__stdin__
