import sys
import io

input_txt = """
4
4 3 2 1
"""


sys.stdin = io.StringIO(input_txt)
tmp = input()


# copy the below part and paste to the submission form.
# ---------function------------
def main():
    n = int(input())
    array = [int(x) for x in input().split()]
    sorted_array = sorted(array)

    groups = []
    for i in range(len(array)):
        moving_src_val = array[i]
        if not moving_src_val:
            continue
        group = [moving_src_val]
        while True:
            moving_tgt_idx = sorted_array.index(moving_src_val)
            moving_tgt_val = array[moving_tgt_idx]
            if moving_tgt_val in group:
                break
            group.append(moving_tgt_val)
            array[moving_tgt_idx] = False
            moving_src_val = moving_tgt_val
        array[i] = False
        groups.append(group)

    #print(groups)

    min_cost = 0
    min_in_array = sorted_array[0]
    for group in groups:
        n_group = len(group)
        if n_group == 1:
            continue
        min_in_group = min(group)
        sum_without_min = sum(group) - min_in_group

        cost1 = (n_group - 1) * min_in_group
        cost2 = (n_group + 1) * min_in_array + 2 * min_in_group

        if cost1 < cost2:
            min_cost += cost1 + sum_without_min
        else:
            min_cost += cost2 + sum_without_min

    print(min_cost)
    return


main()
# -----------------------------
sys.stdin = sys.__stdin__
