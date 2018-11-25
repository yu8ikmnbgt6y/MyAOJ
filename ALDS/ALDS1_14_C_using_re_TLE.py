import sys
import io
import time
import pprint

input_txt = """
15 18
cacaababbcbacbbccc
accababbccbacbaccb
acbbcccccaccaababc
bccacabbbcbbbcbcbb
caabbbccbaaabbaaaa
abcabbcaabacacaacc
bbbaccbaacbbcaabac
aaccbccbccabbccaac
ccabcccbcaaacbacbc
babbccacbaccaabaca
acccaaaacaaaacacaa
bbcccaccbbaaabcaba
bcbaacbbbcbabccaac
baccccaabbbbbcaabb
cabcacabcccabbaaba
3 1
a
a
b
"""

sys.stdin = io.StringIO(input_txt); tmp = input()
#sys.stdin = open('ALDS1_14_D_in11.test')
start_time = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
import re

def main():
    text = ""
    H, W = map(int, input().split())
    for i in range(H):
        text += input()
    R, C = map(int, input().split())
    pattern_list = [input() for x in range(R)]

    pattern = f'[a-zA-z0-9]{{{W-C}}}'.join(pattern_list)

    ptn = re.compile(pattern)

    w_limit = W-C
    start = 0
    while True:
        match = ptn.search(text, start)
        if not match:
            break
        start = match.start()
        h, w = divmod(start, W)
        if w <= w_limit:
            print(h, w)
        start += 1

main()
# -----------------------------
print("elapsed:", time.time()-start_time)
sys.stdin = sys.__stdin__
