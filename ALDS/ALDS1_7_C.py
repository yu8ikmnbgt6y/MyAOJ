import sys
import io

input_txt = """
11
0 1 4
1 2 3
2 -1 -1
3 9 10
4 5 8
5 6 7
6 -1 -1
7 -1 -1
8 -1 -1
9 -1 -1
10 -1 -1
"""


sys.stdin = io.StringIO(input_txt)
tmp = input()


# copy the below part and paste to the submission form.
# ---------function------------
class Node:
    def __init__(self, left, right):
        self.left_node_no = left
        self.right_node_no = right


def preorder_tree_walk(nodes, node_no, order):
    if node_no not in nodes:
        return
    order.append(node_no)
    preorder_tree_walk(nodes, nodes[node_no].left_node_no, order)
    preorder_tree_walk(nodes, nodes[node_no].right_node_no, order)
    return


def inorder_tree_walk(nodes, node_no, order):
    if node_no not in nodes:
        return
    inorder_tree_walk(nodes, nodes[node_no].left_node_no, order)
    order.append(node_no)
    inorder_tree_walk(nodes, nodes[node_no].right_node_no, order)
    return

def postorder_tree_walk(nodes, node_no, order):
    if node_no not in nodes:
        return
    postorder_tree_walk(nodes, nodes[node_no].left_node_no, order)
    postorder_tree_walk(nodes, nodes[node_no].right_node_no, order)
    order.append(node_no)
    return

def main():
    n = int(input())
    nodes = {}
    for i in range(n):
        node_no, left, right = [int(x) for x in input().split()]
        nodes[node_no] = Node(left, right)

    children = set([val.left_node_no for val in nodes.values()] + [val.right_node_no for val in nodes.values()])
    root_node_no = list(set(nodes.keys()) - children)[0]

    preorder = []
    preorder_tree_walk(nodes, root_node_no, preorder)
    print("Preorder")
    print(" " + " ".join(map(str, preorder)))

    inorder = []
    inorder_tree_walk(nodes, root_node_no, inorder)
    print("Inorder")
    print(" " + " ".join(map(str, inorder)))

    postorder = []
    postorder_tree_walk(nodes, root_node_no, postorder)
    print("Postorder")
    print(" " + " ".join(map(str, postorder)))
    return


main()
# -----------------------------
sys.stdin = sys.__stdin__
