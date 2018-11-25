import sys
import io

input_txt="""
30
0 0 0 0 2 3 3 3 4 5 6 7 8 8 8 9 9 9 10 11 11 12 12 12 12 13 13 7000000 500000000 1000000000
16
2 0 5 11 3 16 4 6 1 10 7 14 15 7000000 9 5555555
"""


sys.stdin = io.StringIO(input_txt)
tmp = input()


# copy the below part and paste to the submission form.
# ---------function------------

def binary_search(array, tgt_no): #  arrayは昇順にソートされているものとする

    def compare_midpoint(tgt, array, start, end):
        midpoint = (end + start)//2
        if tgt == array[midpoint]:
            return True, None, None
        elif tgt < array[midpoint]:
            return False, start, midpoint
        elif tgt > array[midpoint]:
            return False, midpoint + 1, end

    start = 0
    end = len(array)
    while True:
        ret, start, end = compare_midpoint(tgt_no, array, start, end)
        if ret:
            return True
        if end <= start:
            return False


def main():
    _ = input()
    array_A = list(map(int, input().split()))
    _ = input()
    array_B = list(map(int, input().split()))

    cnt = 0
    for integer_B in array_B:
        if binary_search(array_A, integer_B):
            #print(integer_B)
            cnt += 1

    print(cnt)
    return


main()
# -----------------------------
sys.stdin = sys.__stdin__
