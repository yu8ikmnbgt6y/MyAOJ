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
from typing import List


def prime_numbers_determination_list(n: int)-> List[bool]:
    """
    determine integers less than given n are prime or not using The Sieve of Eratosthenes
    :param n: int
    :return: list of bools which represents whether the index number is a prime
    """
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(math.sqrt(n)+1)):
        if is_prime[i]:
            for j in range(i*2, n+1, i):
                is_prime[j] = False
    return is_prime


def main():
    num = int(input())
    lines = sys.stdin.readlines()
    count_prime = 0
    is_prime = enumerate_prime_numbers(pow(10,8))
    for i in range(num):
        if is_prime[int(lines[i])]:
            count_prime += 1
    print(count_prime)
    return

main()
# -----------------------------
print("elapsed:", time.time()-start)
sys.stdin = sys.__stdin__
