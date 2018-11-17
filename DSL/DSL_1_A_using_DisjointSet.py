import sys
import io
import time
import pprint

input_txt = """
8 18
0 0 1
0 2 3
0 4 5
0 7 6
0 6 5
1 1 2
0 5 4
1 3 6
0 7 4
0 7 4
1 6 7
0 0 1
0 1 0
1 7 3
0 2 6
1 3 4
0 0 4
1 1 2
"""

#sys.stdin = io.StringIO(input_txt); tmp = input()
sys.stdin = open("DSL_1_A_in32.txt")
#sys.stdout = open("out.dat","w")
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
#import sys
from typing import Dict, List


class Node:
    def __init__(self, parent: str):
        self.parent = parent
        self.height = 1

class Disjoint_Set:
    def __init__(self, n: int):
        self.nodes = {str(x): Node(str(x)) for x in range(n)}

    def find_root(self, i: str) -> str:
        path_nodes = []
        parent = None
        while True:
            parent = self.nodes[i].parent
            if parent == i:
                break
            path_nodes.append(i)
            i = parent
        for passing_node in path_nodes:
            self.nodes[passing_node].parent = parent
        return parent

    def unite_nodes(self, node1: str, node2: str):
        root1 = self.find_root(node1)
        root2 = self.find_root(node2)
        if root1 != root2:
            # unite
            if self.nodes[root1].height <= self.nodes[root2].height:
                #unite root2 to root1
                self.nodes[root2].parent = root1
                self.nodes[root1].height = self.nodes[root2].height + 1
            else:
                #unite root1 to root1
                self.nodes[root1].parent = root2
                self.nodes[root2].height = self.nodes[root1].height + 1
        return

    def is_same_set(self, node1: str, node2: str):
        return self.find_root(node1) == self.find_root(node2)


def main():
    n, q = map(int, input().split())
    query_lines = sys.stdin.readlines()
    queries = [query_lines[x].split() for x in range(q)]

    answers = [None] * q
    num_ans = 0

    disjoint_set = Disjoint_Set(n)

    for query in queries:
        if query[0] == '0':     # unite
            disjoint_set.unite_nodes(query[1], query[2])
        else:                   # same
            answers[num_ans] = ['0', '1'][disjoint_set.is_same_set(query[1], query[2])]
            num_ans += 1
    [print(answers[x]) for x in range(num_ans)]
    return


main()
# -----------------------------
print("elapsed:", time.time()-start)
sys.stdin = sys.__stdin__