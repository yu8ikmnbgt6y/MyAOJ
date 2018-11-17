import sys
import io
import time
import pprint

input_txt = """
31 8
"""

sys.stdin = io.StringIO(input_txt); tmp = input()
#sys.stdin = open("CGL_2_B_in17.test")
#sys.stdout = open("out.dat","w")
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
def main():
    m, n = map(int, input().split())
    print(pow(m, n, 1_000_000_007))

main()
# -----------------------------
print("elapsed:", time.time()-start)
sys.stdin = sys.__stdin__