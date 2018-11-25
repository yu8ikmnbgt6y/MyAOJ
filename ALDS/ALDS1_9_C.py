import sys
import io


sys.stdin = open("ALDS1_9_C_in3.txt", 'r')
#tmp = input()

# copy the below part and paste to the submission form.
# ---------function------------
import sys
nodes = ['OFFSET'] + [-1] * 4000000
_num_nodes = 0
outputs = [None] * 2000000
_num_outputs = 0

def max_heapify(idx):
    left_idx = idx * 2
    right_idx = left_idx + 1

    max_idx = idx

    if nodes[left_idx] > nodes[max_idx]:
        max_idx = left_idx
    if nodes[right_idx] > nodes[max_idx]:
        max_idx = right_idx

    if max_idx != idx:
        tmp = nodes[idx]
        nodes[idx] = nodes[max_idx]
        nodes[max_idx] = tmp
        max_heapify(max_idx)
    return


def insert(node_no):
    global _num_nodes
    nodes[_num_nodes+1] = node_no
    _num_nodes += 1
    idx = _num_nodes
    while idx > 1:
        parent_idx = idx // 2
        if nodes[idx] > nodes[parent_idx]:
            tmp = nodes[parent_idx]
            nodes[parent_idx] = nodes[idx]
            nodes[idx] = tmp
        else:
            break
        idx = parent_idx
    return


def extract():
    global _num_outputs
    outputs[_num_outputs] = nodes[1]
    _num_outputs += 1
    global _num_nodes
    nodes[1] = nodes[_num_nodes]
    nodes[_num_nodes] = -1
    _num_nodes -= 1
    max_heapify(1)
    return


calc_time = False
if calc_time:import time
def main():
    if calc_time: start = time.time()
    commands = sys.stdin.readlines()
    for command in commands:
        if command[0] == 'i':
            insert(int(command[7:]))
        elif command[1] == 'x':
            extract()
        elif command[1] == 'n':
            break

    for i in range(_num_outputs):
        print(outputs[i])
    if calc_time: print(time.time() - start)
    return


main()
# -----------------------------
sys.stdin = sys.__stdin__
