import sys
import io
import time
import pprint

input_txt = """
3 8
"""

sys.stdin = io.StringIO(input_txt); tmp = input()
#sys.stdin = open("CGL_2_B_in17.test")
#sys.stdout = open("out.dat","w")
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
def ext_gcd(a, b):
    if b == 0:
        return 1, 0
    q, t = divmod(a, b)
    x, y = ext_gcd(b, t)
    return y, (x - q * y)


def main():
   a, b = map(int, input().split())
   print(*ext_gcd(a,b))
   return


main()
# -----------------------------
print("elapsed:", time.time()-start)
sys.stdin = sys.__stdin__