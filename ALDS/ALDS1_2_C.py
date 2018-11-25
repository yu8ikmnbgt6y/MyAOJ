import sys
import io

input_txt = """
5
H4 C9 S4 D2 C3
"""

sys.stdin = io.StringIO(input_txt)
print(input())

# copy the below part and paste to the submission form.
# ---------function------------
def bubble_sort(array):
    n = len(array)

    while True:
        flag = False
        for i in range(1, n)[::-1]:
            if array[i-1][1] > array[i][1]:
                tmp = array[i]
                array[i] = array[i-1]
                array[i-1] = tmp
                flag = True
        if not flag:
            break
    return array


def selection_sort(array):
    n = len(array)

    for i in range(n):
        min_idx = i
        for j in range(i, n):
            if array[j][1] < array[min_idx][1]:
                min_idx = j
        if min_idx != i:
            tmp = array[i]
            array[i] = array[min_idx]
            array[min_idx] = tmp
    return array


def accum_hcsd_order(array):
    hcsd_order = {}
    for item in array:
        if item[1] in hcsd_order:
            hcsd_order[item[1]].append(item[0])
        else:
            hcsd_order[item[1]] = [item[0]]
    return hcsd_order


def check_stable(array, hcsd_order):
    tgt_hcsd_order = accum_hcsd_order(array)

    for no, hcsd in hcsd_order.items():
        if len(hcsd) == 1:
            continue
        tgt_hcsd = tgt_hcsd_order[no]
        for src, tgt in zip(hcsd, tgt_hcsd):
            if src != tgt:
                return False
    return True


def main():
    n = int(input())
    array = [(x[0], int(x[1:])) for x in input().split()]
    str_stable_or_not = {True: "Stable", False: "Not stable"}

    hcsd_order = accum_hcsd_order(array)

    # bubble_sort
    array_b = bubble_sort(array[:])
    print(" ".join(map(lambda x: "{}{}".format(x[0], x[1]), array_b)))
    print(str_stable_or_not[check_stable(array_b, hcsd_order)])

    # selection_sort
    array_s = selection_sort(array[:])
    print(" ".join(map(lambda x: "{}{}".format(x[0], x[1]), array_s)))
    print(str_stable_or_not[check_stable(array_s, hcsd_order)])

    return

main()
# -----------------------------
sys.stdin = sys.__stdin__
