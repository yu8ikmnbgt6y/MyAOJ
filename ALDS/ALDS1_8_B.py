import sys
import io

input_txt = """
10
insert 30
insert 88
insert 12
insert 1
insert 20
find 12
insert 17
insert 25
find 16
print
"""



sys.stdin = io.StringIO(input_txt)
tmp = input()


# copy the below part and paste to the submission form.
# ---------function------------
import sys
class Node:
    parent = -1
    left = -1
    right = -1

    def __init__(self, key):
        self.key = key

    def __repr__(self):
        return "k:{},p:{},l:{},r:{}".format(self.key, self.parent, self.left, self.right)

root_node_no = -1

def insert(nodes :dict, in_node :Node):
    global root_node_no

    cur_node_no = root_node_no
    parent_node_no = -1
    while cur_node_no != -1:
        parent_node_no = cur_node_no
        if in_node.key < cur_node_no:
            cur_node_no = nodes[cur_node_no].left
        else:
            cur_node_no = nodes[cur_node_no].right

    in_node.parent = parent_node_no

    if root_node_no == -1:
        root_node_no = in_node.key
    elif in_node.key < parent_node_no:
        nodes[parent_node_no].left = in_node.key
    else:
        nodes[parent_node_no].right = in_node.key

    nodes[in_node.key] = in_node

def inorder_tree_walk(nodes, node_no ,inorder):
    if node_no == -1:
        return
    inorder_tree_walk(nodes, nodes[node_no].left, inorder)
    inorder.append(node_no)
    inorder_tree_walk(nodes, nodes[node_no].right, inorder)

def preorder_tree_walk(nodes, node_no, preorder):
    if node_no == -1:
        return
    preorder.append(node_no)
    preorder_tree_walk(nodes, nodes[node_no].left, preorder)
    preorder_tree_walk(nodes, nodes[node_no].right, preorder)


def find(nodes, tgt_node_no):
    cur_node_no = root_node_no
    while cur_node_no != -1:
        cur_node = nodes[cur_node_no]
        if cur_node.key == tgt_node_no:
            return True
        elif tgt_node_no < cur_node.key:
            cur_node_no = cur_node.left
        else:
            cur_node_no = cur_node.right

    return False


def main():
    num_com = int(input())
    commands = sys.stdin.readlines()
    nodes = {}
    for i in range(num_com):
        if commands[i][0] == 'i':
            insert(nodes, Node(int(commands[i][7:])))
        elif commands[i][0] == 'p':
            # inorder
            inorder = []
            inorder_tree_walk(nodes, root_node_no, inorder)
            print(" " + " ".join(map(str, inorder)))
            # preorder
            preorder = []
            preorder_tree_walk(nodes, root_node_no, preorder)
            print(" " + " ".join(map(str, preorder)))
        elif commands[i][0] == 'f':
            if find(nodes, int(commands[i][5:])):
                print('yes')
            else:
                print('no')


main()
# -----------------------------
sys.stdin = sys.__stdin__
