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
import sys
from typing import Dict, List


def find_group(groups: Dict[int, List], tgt: str) -> (bool, str):
    for k, v in groups.items():
        if tgt in v:
            return k
    return "-1"


def main():
    n, q = map(int, input().split())
    query_lines = sys.stdin.readlines()
    queries = [query_lines[x].split() for x in range(q)]

    answers = [None] * q
    num_ans = 0

    groups = {str(i): [str(i)] for i in range(n)}
    groups_memo = {str(i): str(i) for i in range(n)}

    for query in queries:
        if query[0] == '0':     # unite
            q1 = query[1]
            q2 = query[2]
            g1 = find_group(groups, q1)
            g2 = find_group(groups, q2)
            if g1 == g2:
                continue
            assert g1 != -1 and g2 != -1
            for item in groups[g2]:
                groups_memo[item] = g1
            groups[g1] = groups[g1] + groups[g2]
            del groups[g2]
        else:                   # same
            if groups_memo[query[1]] == groups_memo[query[2]]:
                answers[num_ans] = 1
            else:
                answers[num_ans] = 0
            num_ans += 1

    [print(answers[x]) for x in range(num_ans)]
    return

main()
# -----------------------------
print("elapsed:", time.time()-start)
sys.stdin = sys.__stdin__