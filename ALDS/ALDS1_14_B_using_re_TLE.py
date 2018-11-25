import sys
import io
import time
import pprint

input_txt = """
aabbcacabdab
ab
"""

#sys.stdin = io.StringIO(input_txt); tmp = input()
sys.stdin = open('ALDS1_14_B_in34.test')
start_time = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
import re

def main():
    text = input()
    pattern = input()

    pattern = f'(?={pattern})'
    indices=[]
    for match in re.finditer(pattern, text):
        indices.append(match.start())
    [print(x) for x in indices]
    return


main()
# -----------------------------
print("elapsed:", time.time()-start_time)
sys.stdin = sys.__stdin__
