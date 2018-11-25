import sys
import io
import time
import pprint

input_txt = """
6
"""

sys.stdin = io.StringIO(input_txt); tmp = input()
#sys.stdin = open("CGL_2_B_in17.test")
#sys.stdout = open("out.dat","w")
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
import math
from collections import defaultdict

def prime_factorize(n: int):
    prime_factors = defaultdict(int)

    for i in range(2, int(math.sqrt(n)) + 1):
        while True:
            div, mod = divmod(n, i)
            if mod == 0:
                prime_factors[i] += 1
                n = div
            else:
                break
        if n == 1:
            break
    if n != 1:
        prime_factors[n] = 1

    return prime_factors


def main():
   n = int(input())
   primes = prime_factorize(n)

   ret = 1
   for k, v in primes.items():
      ret *= pow(k, v) - pow(k, v-1)
   print(ret)
   return



main()
# -----------------------------
print("elapsed:", time.time()-start)
sys.stdin = sys.__stdin__