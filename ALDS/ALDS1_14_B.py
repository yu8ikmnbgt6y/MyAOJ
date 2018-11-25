import sys
import io
import time
import pprint

input_txt = """
abcdefg012345abcdefg
01234
"""

sys.stdin = io.StringIO(input_txt); tmp = input()
#sys.stdin = open('ALDS1_14_B_in29.test')
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
def main():
    text = input()
    len_text = len(text)
    pattern = input()
    len_pattern = len(pattern)

    for i in range(len_text - len_pattern + 1):
        if text[i:i+len_pattern] == pattern:
            print(i)
    return


main()
# -----------------------------
print("elapsed:", time.time()-start)
sys.stdin = sys.__stdin__
