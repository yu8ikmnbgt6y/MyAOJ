import sys
import io

input_txt="""
5
1 1 2 2 3
2
1 2
"""


sys.stdin = io.StringIO(input_txt)
tmp = input()


# copy the below part and paste to the submission form.
# ---------function------------
def main():
    _ = input()
    array_A = input().split()
    _ = input()
    array_B = input().split()

    array_intersection = set(array_A) & set(array_B)

    print(len(array_intersection))

    return


main()
# -----------------------------
sys.stdin = sys.__stdin__
