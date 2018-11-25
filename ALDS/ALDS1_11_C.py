import sys
import io
import time
import pprint

input_txt = """
10 5
0 1
1 2
2 9
3 4
6 7
12
0 1
0 2
0 9
3 4
6 7
7 6
0 5
0 6
3 7
3 5
5 8
8 5
"""

sys.stdin = open("ALDS1_11_D_in11.txt","r")#io.StringIO(input_txt)

#sys.stdin = io.StringIO(input_txt)
#tmp = input()
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
import sys
from collections import defaultdict

def main():
    lines = sys.stdin.readlines()
    n, m = map(int, lines[0].split())
    relation_lines = lines[1:1+m]

    relations = defaultdict(list)

    for idx, relation_line in enumerate(relation_lines):
        s, t = relation_line.split()
        relations[s].append(t)
        relations[t].append(s)

    group = {}
    for key in relations.keys():
        group[key] = -1
    group_num = 0

    # assign a group number for ids
    for key, val in relations.items():
        if group[key] != -1:
            continue

        group[key] = group_num
        group_num += 1

        group_no = group[key]
        friends = [key]

        while len(friends) != 0:
            n_fs = relations[friends.pop()]
            for n_f in n_fs:
                if group[n_f] == -1:
                    group[n_f] = group_no
                    friends.append(n_f)

    q = int(lines[1+m])
    question_lines = lines[1+m+1:]
    answers = [None] * q
    for i, question in enumerate(question_lines):
        s, t = question.split()

        if s not in group or t not in group:
            answers[i] = 'no'
        elif group[s] == group[t]:
            answers[i] = 'yes'
        else:
            answers[i] = 'no'

    # answer
    [print(ans) for ans in answers]
    return

main()
# -----------------------------
print("elapsed:", time.time()-start)
sys.stdin = sys.__stdin__
