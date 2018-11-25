import sys
import io

input_txt = """
5
3 5 2 1 4
"""


sys.stdin = io.StringIO(input_txt)
tmp = input()


# copy the below part and paste to the submission form.
# ---------function------------
import sys
time_check = False
if time_check:
    import time

num_of_inversions = 0
array = [0 for x in range(200000)]

def merge(left, mid, right):
    n_fore = mid - left
    n_rear = right - mid
    l_fore = array[left:left + n_fore]
    l_fore.append(sys.maxsize)
    l_rear = array[mid:mid + n_rear]
    l_rear.append(sys.maxsize)

    i = j = 0
    global num_of_inversions
    offset = len(l_fore) - 1 + left

    for k in range(left, right):
        if l_fore[i] < l_rear[j]:
            array[k] = l_fore[i]
            i += 1
        else:
            array[k] = l_rear[j]
            num_of_inversions += j - k + offset
            #print(l_fore,l_rear, array[:23])
            #print(num_of_inversions,len(l_fore),len(l_rear),i,j,k)
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

    #print(" ".join(map(str, array[:n])))
    print(num_of_inversions)

    return


main()
# -----------------------------
sys.stdin = sys.__stdin__
