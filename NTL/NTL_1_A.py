import sys
import io
import time
import pprint

input_txt = """
999999792
"""

sys.stdin = io.StringIO(input_txt); tmp = input()
#sys.stdin = open("CGL_2_B_in17.test")
#sys.stdout = open("out.dat","w")
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
import math
from typing import List


def is_prime(n: int)-> bool:
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    # when n is a prime number
    # x^(n-1) ≡ 1 (mod n)
    return pow(2, (n-1), n) == 1


def prime_factorize(n: int) ->List[int]:
    prime_factors = []

    for i in range(2, int(math.sqrt(n)) + 1):
        if not is_prime(i):
            continue
        while True:
            div, mod = divmod(n, i)
            if mod == 0:
                prime_factors.append(i)
                n = div
            else:
                break
        if n == 1:
            break
    return prime_factors


def main():
    n = int(input())
    prime_factors = prime_factorize(n)
    print("{}: {}".format(n, ' '.join(map(str, prime_factors))))


main()
# -----------------------------
print("elapsed:", time.time()-start)
sys.stdin = sys.__stdin__