import sys
import io

input_txt = """
1
1
"""

sys.stdin = io.StringIO(input_txt)
print(input())

# copy the below part and paste to the submission form.
# ---------function------------

def insertion_sort(array, gap):
    n = len(array)
    cnt = 0
    for i in range(gap, n):
        moving = array[i]
        j = i - gap
        while j >= 0 and array[j] > moving:
            array[j + gap] = array[j]
            j -= gap
            cnt += 1
        array[j + gap] = moving
    return array, cnt


def main():
    n = int(input())
    array = []
    for i in range(n):
        array.append(int(input()))

    cnt = 0
    gaps = []
    i = 1
    gap = 1
    while gap <= n:
        gaps.append(gap)
        i += 1
        gap = (3 ** i - 1) // 2
    gaps = gaps[:100][::-1]

    # shell_sort
    for gap in gaps:
        array, tmp_cnt = insertion_sort(array, gap)
        cnt += tmp_cnt

    print(len(gaps))
    print(" ".join(map(str, gaps)))
    print(cnt)
    for i in array:
        print(i)
    return

main()
# -----------------------------
sys.stdin = sys.__stdin__
