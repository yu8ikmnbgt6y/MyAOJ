import sys
import io
import time
import pprint

input_txt = """
147 105
"""

sys.stdin = io.StringIO(input_txt); tmp = input()
#sys.stdin = open('ALDS1_1_C_in4.test')
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
import math

def main():
    x, y = map(int, input().split())
    print(math.gcd(x, y))

main()
# -----------------------------
print("elapsed:", time.time()-start)
sys.stdin = sys.__stdin__
