import sys
import io

input_txt = """
10
4 1 3 2 16 9 10 14 8 7
"""

sys.stdin = io.StringIO(input_txt)
tmp = input()

# copy the below part and paste to the submission form.
# ---------function------------
def max_heapify(nodes, idx):
    left_idx = idx * 2
    right_idx = idx * 2 + 1

    max_idx = idx

    if left_idx <= len(nodes) and nodes[left_idx-1] > nodes[max_idx-1]:
        max_idx = left_idx
    if right_idx <= len(nodes) and nodes[right_idx-1] > nodes[max_idx-1]:
        max_idx = right_idx

    if max_idx != idx:
        tmp = nodes[idx-1]
        nodes[idx-1] = nodes[max_idx-1]
        nodes[max_idx-1] = tmp
        max_heapify(nodes, max_idx)
    return


def build_maxheap(nodes):
    for i in range(1, len(nodes)//2 + 1)[::-1]:
        max_heapify(nodes, i)
    return


def main():
    num_node = int(input())
    nodes = [int(x) for x in input().split()]
    build_maxheap(nodes)
    print(" " + " ".join(map(str, nodes)))
    return


main()
# -----------------------------
sys.stdin = sys.__stdin__
