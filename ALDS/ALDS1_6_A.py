import sys
import io

input_txt = """
7
2 5 1 3 2 3 0
"""


sys.stdin = io.StringIO(input_txt)
tmp = input()


# copy the below part and paste to the submission form.
# ---------function------------
def counting_sort(array, max_val=10000):
    max_val = min(max(array), max_val)
    counting_array = [0] * (max_val+1)
    sorted_array = [0 for x in range(len(array))]

    for i in array:
        counting_array[i] += 1

    for i in range(1, max_val + 1):
        counting_array[i] += counting_array[i-1]

    for i in range(len(array))[::-1]:
        val = array[i]
        sorted_array[counting_array[val]-1] = val
        counting_array[val] -= 1

    return sorted_array


def main():
    n = int(input())
    array = [int(x) for x in input().split()]
    sorted_array = counting_sort(array)
    print(" ".join(map(str, sorted_array)))
    return

main()
# -----------------------------
sys.stdin = sys.__stdin__
