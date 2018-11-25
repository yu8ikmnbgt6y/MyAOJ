import sys
import io

input_txt = """
6
D 3
H 2
D 1
S 3
D 2
C 1
"""


sys.stdin = io.StringIO(input_txt)
tmp = input()


# copy the below part and paste to the submission form.
# ---------function------------
def partition(array, first, end):
    criteria = array[end]
    i_ins = first
    for i_cur in range(first, end):
        if array[i_cur] <= criteria:
            array[i_ins], array[i_cur] = array[i_cur], array[i_ins]
            i_ins += 1
    array[i_ins], array[end] = array[end], array[i_ins]
    return i_ins


def main():
    n = int(input())
    array = [int(x) for x in input().split()]
    i_ins = partition(array, 0, n-1)
    output_txt = ""
    if i_ins != 0:
        output_txt += " ".join([str(x) for x in array[:i_ins]]) + " "
    output_txt += "[{}]".format(array[i_ins])
    if i_ins < n-1:
        output_txt += " " + " ".join([str(x) for x in array[i_ins + 1:]])
    print(output_txt)
    return


main()
# -----------------------------
sys.stdin = sys.__stdin__
