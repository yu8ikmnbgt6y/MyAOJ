import sys
import io

input_txt = """
13
0 3 1 4 10
1 2 2 3
2 0
3 0
4 3 5 6 7
5 0
6 0
7 2 8 9
8 0
9 0
10 2 11 12
11 0
12 0
"""


sys.stdin = io.StringIO(input_txt)
tmp = input()


# copy the below part and paste to the submission form.
# ---------function------------
class Node:
    parent = ""
    depth = ""

    def __init__(self, children=[]):
        self.children = children
        if len(children) == 0:
            self.type = 'leaf'
        else:
            self.type = 'internal node'


def add_parent_node_and_depth(nodes, parent_node_no, node_no, depth):
    nodes[node_no].parent = parent_node_no
    nodes[node_no].depth = depth
    for child in nodes[node_no].children:
        add_parent_node_and_depth(nodes, node_no, child, depth+1)
    return


def main():
    n = int(input())
    nodes = {}
    leafs = {}
    for i in range(n):
        node_no, child_num, *children = [int(x) for x in input().split()]
        if child_num == 0:
            leafs[node_no] = Node([])
        else:
            nodes[node_no] = Node(children)

    nodes.update(leafs)
    # search root node no
    node_no = list(leafs.keys())[0]
    while True:
        parent_node_no = [key for key, value in nodes.items() if node_no in value.children]
        if len(parent_node_no) == 0:
            root_node_no = node_no
            nodes[root_node_no].type = 'root'
            break
        node_no = parent_node_no[0]

    # add parent node no and depth to all nodes
    add_parent_node_and_depth(nodes, parent_node_no=-1, node_no=root_node_no, depth=0)

    for i in range(n):
        node = nodes[i]
        print("node {}: parent = {}, depth = {}, {}, [{}]".
              format(str(i), node.parent, node.depth, node.type, ", ".join(map(str, node.children))))

    return


main()
# -----------------------------
sys.stdin = sys.__stdin__
