import sys
import io
import time
import pprint

input_txt = """
6
1 2 2 4
2 1 5
3 2 5 6
4 0
5 1 4
6 1 6
"""

sys.stdin = io.StringIO(input_txt)
tmp = input()
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
import sys

def push_vertex(frame, vtx, search_queue, outputs, vertices):
    #print("frame:{} push:{}".format(frame, vtx))
    outputs[vtx] = [frame, None]
    search_queue.append(vtx)
    [vertices[key].remove(vtx) for key in vertices.keys() if vtx in vertices[key]]

    return

def main():
    n = int(input())
    lines = sys.stdin.readlines()
    outputs = {}

    vertices = {}
    for i in range(n):
        idx, idx_n, *idx_vertices = lines[i].rstrip().split()
        vertices[int(idx)] = [int(x) for x in idx_vertices]

    vtx = 1
    frame = 1
    search_stack = []
    push_vertex(frame, vtx, search_stack, outputs, vertices)

    while len(vertices) != 0:
        frame += 1
        if len(search_stack) != 0:
            vtx = search_stack[-1]
        else:
            vtx = list(vertices.keys())[0]
            push_vertex(frame, vtx, search_stack, outputs, vertices)
            continue

        if len(vertices[vtx]) != 0:
            next_vtx = vertices[vtx][0]
            push_vertex(frame, next_vtx, search_stack, outputs, vertices)
        else:
            search_stack.pop()
            #print("frame:{},pop:{}".format(frame, vtx))
            del vertices[vtx]
            outputs[vtx][1] = frame

    #pprint.pprint(outputs)
    for key, value in sorted(outputs.items(), key=lambda x: x[0]):
        print("{} {} {}".format(key, value[0], value[1]))


main()
# -----------------------------
print("elapsed:", time.time()-start)
sys.stdin = sys.__stdin__