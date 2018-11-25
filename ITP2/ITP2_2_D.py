import sys
import io
import time
import pprint

input_txt = """
3 10
0 0 1
0 0 2
0 0 3
0 1 4
0 1 5
2 1 0
0 2 6
1 0
1 1
1 2
"""

#sys.stdin = io.StringIO(input_txt);input()
sys.stdin = open('ITP2_2_D_in11.test')
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
import sys

class Node:
    def __init__(self, next_node, prev_node, val):
        self.next = next_node
        self.prev = prev_node
        self.val = val

    def __repr__(self):
        return f'{self.val}'


class DoubleLinkedList:
    def __init__(self):
        self.head = Node(None, None, None)
        self.tail = self.head

    def append(self, val):
        node = Node(None, self.tail, val)
        self.tail.next = node
        self.tail = node

    def dump(self):
        cur = self.head.next
        out = ''
        while cur is not None:
            out += f'{cur.val} '
            cur = cur.next
        print(out[:-1])

    def splice(self, other):
        self.tail.next = other.head.next
        self.tail = other.tail

    def clear(self):
        self.__init__()


n, q = map(int, input().split())

lists = {str(i): DoubleLinkedList() for i in range(n)}

lines = sys.stdin.readlines()
for i in range(q):
    query, *arg = lines[i].split()
    #print(i, query, arg)
    if query == '0':    # insert t x
        lists[arg[0]].append(arg[1])

    elif query == '1':  # dump t
        lists[arg[0]].dump()

    elif query == '2':  # splice s t
        lists[arg[1]].splice(lists[arg[0]])
        lists[arg[0]].clear()

    else:
        raise AssertionError





# -----------------------------
print("elapsed:", time.time()-start)
sys.stdin = sys.__stdin__