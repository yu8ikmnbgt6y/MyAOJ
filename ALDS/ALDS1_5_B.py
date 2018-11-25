import sys
import io

input_txt="""
200
0 33 43 62 29 0 8 52 56 56 19 11 51 43 5 8 93 30 66 69 32 17 47 72 68 80 23 49 92 64 69 51 27 90 24 35 20 44 10 62 84 63 1 10 36 76 31 29 97 75 91 90 44 34 25 29 30 27 26 43 34 4 60 49 20 56 32 72 13 90 9 19 5 95 49 27 19 97 24 96 49 56 84 93 45 7 6 9 54 52 65 83 38 1 90 30 37 95 56 63 11 27 42 6 68 12 1 10 80 58 71 31 14 47 64 97 25 38 31 18 87 51 87 13 79 95 50 50 13 62 34 73 47 21 30 40 57 78 26 3 97 8 93 88 38 85 93 88 20 11 46 87 10 9 87 68 3 73 0 74 5 83 52 70 87 2 10 5 10 0 96 42 85 60 47 24 31 58 86 19 0 15 55 82 74 61 6 2 68 65 70 18 23 89 6 19 30 55 32 93
"""


sys.stdin = io.StringIO(input_txt)
tmp = input()


# copy the below part and paste to the submission form.
# ---------function------------
import sys
time_check = True
if time_check:
    import time

num_of_inversions = 0
array = [0 for x in range(500000)]

def merge(left, mid, right):
    n_fore = mid - left
    n_rear = right - mid
    l_fore = array[left:left + n_fore]
    l_fore.append(sys.maxsize)
    l_rear = array[mid:mid + n_rear]
    l_rear.append(sys.maxsize)

    i = j = 0
    global num_of_inversions
    compare_counter += (right - left)
    for k in range(left, right):
        if l_fore[i] < l_rear[j]:
            array[k] = l_fore[i]
            i += 1
        else:
            array[k] = l_rear[j]
            j += 1


def merge_sort(left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        merge_sort(left, mid)
        merge_sort(mid, right)
        merge(left, mid, right)
    return


def main():

    n = int(input())
    for idx, value in enumerate(input().split()):
        array[idx] = int(value)

    if time_check:
        start = time.time()

    merge_sort(0, n)

    if time_check:
        print("elapsed_time:", time.time() - start)

    print(" ".join(map(str, array[:n])))
    print(num_of_inversions)

    return


main()
# -----------------------------
sys.stdin = sys.__stdin__
