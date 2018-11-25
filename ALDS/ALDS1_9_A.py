import sys
import io

input_txt = """
6
10 8 5 1 2 3
"""

sys.stdin = io.StringIO(input_txt)
tmp = input()

# copy the below part and paste to the submission form.
# ---------function------------
def main():
    num_node = int(input())
    nodes = [int(x) for x in input().split()]

    for i in range(num_node):
        idx = i + 1
        print("node {}: key = {}, ".format(idx, nodes[i]), end="")
        # print parent key
        parent_idx = idx // 2
        if parent_idx != 0:
            print("parent key = {}, ".format(nodes[parent_idx-1]), end="")
        # print left_key
        left_idx = idx * 2
        if left_idx <= num_node:
            print("left key = {}, ".format(nodes[left_idx-1]), end="")
        # print right_key
        right_idx = idx * 2 + 1
        if right_idx <= num_node:
            print('right key = {}, '.format(nodes[right_idx-1]), end="")
        print("")
    return


main()
# -----------------------------
sys.stdin = sys.__stdin__
