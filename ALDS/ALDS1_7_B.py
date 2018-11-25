import sys
import io

input_txt = """
4
1 0 -1
0 2 -1
2 3 -1
3 -1 -1
"""


sys.stdin = io.StringIO(input_txt)
tmp = input()


# copy the below part and paste to the submission form.
# ---------function------------
class Node:
    parent = ""
    sibling = ""
    depth = ""
    height = ""

    def __init__(self, left, right):
        self.left = left
        self.right = right

        if self.right == -1 and self.left == -1:
            self.degree = 0
            self.type = 'leaf'
        elif self.right == -1 or self.left == -1:
            self.degree = 1
            self.type = 'internal node'
        else:
            self.degree = 2
            self.type = 'internal node'


def add_parent_node_and_depth(nodes, parent_node_no, node_no, depth):
    nodes[node_no].parent = parent_node_no
    nodes[node_no].depth = depth

    left_node_no = nodes[node_no].left
    right_node_no = nodes[node_no].right

    left_height, right_height = 0, 0
    if left_node_no != -1:
        left_height = add_parent_node_and_depth(nodes, node_no, left_node_no, depth+1)
        nodes[left_node_no].sibling = right_node_no
    if right_node_no != -1:
        right_height = add_parent_node_and_depth(nodes, node_no, right_node_no, depth+1)
        nodes[right_node_no].sibling = left_node_no

    if left_node_no == -1 and right_node_no == -1:
        nodes[node_no].height = 0
    else:
        nodes[node_no].height = max(left_height, right_height) + 1
    return nodes[node_no].height


def main():
    n = int(input())
    nodes = {}
    for i in range(n):
        node_no, left, right = [int(x) for x in input().split()]
        nodes[node_no] = Node(left, right)

    lefts = [nodes[x].left for x in nodes]
    rights = [nodes[x].right for x in nodes]
    root_no = list(set(nodes.keys()) - set(lefts + rights))[0]

    nodes[root_no].type = 'root'
    nodes[root_no].sibling = -1
    add_parent_node_and_depth(nodes, -1, root_no, 0)

    for i in range(n):
        node = nodes[i]
        print("node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}".format(
            i, node.parent, node.sibling, node.degree, node.depth, node.height, node.type
        ))

    return

main()
# -----------------------------
sys.stdin = sys.__stdin__
