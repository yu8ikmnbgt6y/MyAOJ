import sys
import io

input_txt = """
43
insert 30
insert 17
insert 88
insert 53
insert 5
insert 20
insert 18
insert 28
insert 27
insert 60
print
find -1
find 2
find 3
find 4
find 5
find 6
find 10
find 17
find 28
find 29
find 30
find 31
find 50
find 51
find 52
find 53
find 54
find 60
find 88
find 89
insert 2000000000
insert 55
insert 63
insert -1
insert 8
print
delete 53
delete 2000000000
delete 20
delete 5
delete 8
print
"""



sys.stdin = io.StringIO(input_txt)
tmp = input()


# copy the below part and paste to the submission form.
# ---------function------------
import sys

class Node:
    __slots__ = ['key', 'parent', 'left', 'right']

    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

    def __repr__(self):
        return "({},{},{},{})".format(self.key, self.parent, self.left, self.right)

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return self.left is None and self.right is None

    def has_one_child(self):
        if self.is_leaf():
            return False
        elif (self.left is None) and (self.right is not None):
            return self.right
        elif (self.left is not None) and (self.right is None):
            return self.left
        else:
            return False

    def has_two_child(self):
        return (self.left is not None) and (self.right is not None)


root_node_no = None


def insert(nodes: dict, in_node: Node):
    global root_node_no

    cur_node_no = root_node_no
    parent_node_no = None
    while cur_node_no:
        parent_node_no = cur_node_no
        if in_node.key < cur_node_no:
            cur_node_no = nodes[cur_node_no].left
        else:
            cur_node_no = nodes[cur_node_no].right

    in_node.parent = parent_node_no

    if root_node_no is None:
        root_node_no = in_node.key
    elif in_node.key < parent_node_no:
        nodes[parent_node_no].left = in_node.key
    else:
        nodes[parent_node_no].right = in_node.key

    nodes[in_node.key] = in_node

def inorder_tree_walk(nodes, node_no ,inorder):
    if node_no is None:
        return
    inorder_tree_walk(nodes, nodes[node_no].left, inorder)
    inorder.append(node_no)
    inorder_tree_walk(nodes, nodes[node_no].right, inorder)

def preorder_tree_walk(nodes, node_no, preorder):
    if node_no is None:
        return
    preorder.append(node_no)
    preorder_tree_walk(nodes, nodes[node_no].left, preorder)
    preorder_tree_walk(nodes, nodes[node_no].right, preorder)


def find(nodes, tgt_node_no):
    cur_node_no = root_node_no
    while cur_node_no is not None:
        cur_node = nodes[cur_node_no]
        if cur_node.key == tgt_node_no:
            return True
        elif tgt_node_no < cur_node.key:
            cur_node_no = cur_node.left
        else:
            cur_node_no = cur_node.right
    return False


def switch_child_of_parent(nodes: dict, del_node: Node, switch_node_no):
    if nodes[del_node.parent].left == del_node.key:
        nodes[del_node.parent].left = switch_node_no
    elif nodes[del_node.parent].right == del_node.key:
        nodes[del_node.parent].right = switch_node_no
    return


def delete_node(nodes: dict, delete_node_no: int):
    del_node = nodes[delete_node_no]

    if del_node.is_leaf():
        # delete leaf
        switch_child_of_parent(nodes, del_node, None)
    elif not del_node.has_two_child():
        # delete one child node
        child = del_node.has_one_child()
        switch_child_of_parent(nodes, del_node, child)
        nodes[child].parent = del_node.parent
    else:
        # delete two child node
        inorder = []
        inorder_tree_walk(nodes, del_node.right, inorder)
        swap_node = Node(inorder[0])
        switch_child_of_parent(nodes, del_node, swap_node.key)

        swap_node.parent = del_node.parent
        swap_node.left = del_node.left
        if swap_node.key == del_node.right:
            swap_node.right = None
        else:
            swap_node.right = del_node.right
            nodes[swap_node.right].parent = swap_node.key
        nodes[swap_node.left].parent = swap_node.key
        delete_node(nodes, swap_node.key)
        nodes[swap_node.key] = swap_node

    del nodes[delete_node_no]
    return


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
        elif commands[i][0] == 'd':
            delete_node(nodes, int(commands[i][7:]))

main()
# -----------------------------
sys.stdin = sys.__stdin__
