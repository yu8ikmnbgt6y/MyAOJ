import sys
import io
import time
import pprint

input_txt = """
aabaaa
4
aa
ba
bb
xyz
"""

#sys.stdin = io.StringIO(input_txt); tmp = input()
sys.stdin = open('ALDS1_14_D_in11.test')
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
import sys
import re


def main():
    text = input()
    len_text = len(text)
    num_query = int(input())
    queries = [input() for i in range(num_query)]
    queries_ = '|'.join(queries)

    for match in re.finditer(queries_, text):
        print(match)




    return

    #lines = sys.stdin.readlines()
    ans = ['0'] * num_query
    for i_query in range(num_query):
        print(i_query)
        ptn = input() #lines[i_query].rstrip()
        len_ptn = len(ptn)
        if ptn in text:
            ans[i_query] = '1'
    print("\n".join(ans))
    return

main()
# -----------------------------
print("elapsed:", time.time()-start)
sys.stdin = sys.__stdin__
