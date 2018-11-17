import sys
import io
import time
import pprint

input_txt = """
16
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
"""

sys.stdin = io.StringIO(input_txt); tmp = input()
#sys.stdin = open('ALDS1_1_C_in4.test')
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
import math
import sys


def is_prime(n: int)-> bool:
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    num = int(input())
    lines = sys.stdin.readlines()
    count_prime = 0
    for i in range(num):
        if is_prime(int(lines[i])):
            count_prime += 1
    print(count_prime)
    return

main()
# -----------------------------
print("elapsed:", time.time()-start)
sys.stdin = sys.__stdin__
