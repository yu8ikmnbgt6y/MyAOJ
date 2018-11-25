import sys
import io
import time
import pprint

input_txt = """
5
0 1
0 2
0 3
1 1
2
"""

#sys.stdin = io.StringIO(input_txt);input()
sys.stdin = open('ITP2_1_C_in9.test')
#sys.stdout = open('out.test','w')
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
import sys


class Node:
    __slots__ = ['prev', 'next', 'id', 'val']

    def __init__(self, prev_node, next_node, id, val):
        self.prev = prev_node
        self.next = next_node
        self.id = id
        self.val = val

    def __repr__(self):
        return f'{self.id},{self.val}'


class LinkedList:
    def __init__(self):
        begin_node = Node(None, None, 0, -sys.maxsize)
        end_node = Node(None, None, 1, sys.maxsize)
        begin_node.next = end_node
        end_node.prev = begin_node
        self.Nodes = {0: begin_node, 1: end_node}
        self.id = 2
        self.cursor = self.Nodes[1]

    def move(self, d):
        if d < 0:
            for i in range(abs(d)):
                self.cursor = self.cursor.prev
        elif d > 0:
            for i in range(abs(d)):
                self.cursor = self.cursor.next

    def print_all_nodes(self):
        out = ''
        while self.cursor.prev is not None:
            self.cursor = self.cursor.prev

        self.cursor = self.cursor.next
        while self.cursor.next is not None:
            out += f'{self.cursor.val}\n'
            self.cursor = self.cursor.next
        print(out, end='')

    def insert(self, val):
        tmp_node = Node(self.cursor.prev, self.cursor, self.id, val)
        self.cursor.prev.next = tmp_node
        self.cursor.prev = tmp_node
        self.Nodes[self.id] = tmp_node
        self.cursor = tmp_node
        self.id += 1

    def erase(self):
        self.cursor.prev.next = self.cursor.next
        self.cursor.next.prev = self.cursor.prev
        del self.Nodes[self.cursor.id]
        self.cursor = self.cursor.next


linkedlist = LinkedList()


nq = int(input())
lines = sys.stdin.readlines()
for i in range(nq):
    query, *arg = lines[i].split()
    #print(query,arg)
    if query == '0':  # insert x
        linkedlist.insert(arg[0])
    elif query == '1':  # move d
        linkedlist.move(int(arg[0]))
    elif query == '2':  # erase
        linkedlist.erase()
    else:
        raise AssertionError

linkedlist.print_all_node()
# -----------------------------
print("elapsed:", time.time()-start)
sys.stdin = sys.__stdin__