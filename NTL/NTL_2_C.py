import sys
import io
import time
import pprint

input_txt = """
64909177115977673656394812939088 25
"""

input_txt = """
0 1
"""
sys.stdin = io.StringIO(input_txt); tmp = input()
#sys.stdin = open("CGL_2_B_in17.test")
#sys.stdout = open("out.dat","w")
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
def main():
   a,b = map(int, input().split())
   print(a*b)


main()
# -----------------------------
print("elapsed:", time.time()-start)
sys.stdin = sys.__stdin__