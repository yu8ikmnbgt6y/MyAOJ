import sys
import io

input_txt = """
20
S 10000000
C 7777
H 2500000
D 2500000
H 2
D 999999999
S 999999999
H 10000000
H 7777
S 2500000
C 999999999
C 2500000
D 7777
D 10000000
D 2
S 2
C 2
H 999999999
S 7777
C 10000000
"""


sys.stdin = io.StringIO(input_txt)
tmp = input()


# copy the below part and paste to the submission form.
# ---------function------------
import sys


def partition_for_second_element(array, first, end):
    criteria = array[end][1]
    i_ins = first
    for i_cur in range(first, end):
        if array[i_cur][1] <= criteria:
            array[i_ins], array[i_cur] = array[i_cur], array[i_ins]     # swap
            i_ins += 1
    array[i_ins], array[end] = array[end], array[i_ins]     # swap
    return i_ins


def quick_sort(array, first, end):
    if first < end:
        #print(first,end,array[end],end='-->')
        criteria_idx = partition_for_second_element(array, first, end)
        #print(criteria_idx,array)
        quick_sort(array, first, criteria_idx - 1)
        quick_sort(array, criteria_idx + 1, end)


def shcd_order(cards):
    orders = {}
    for card in cards:
        if card[1] not in orders:
            orders[card[1]] = [card[0]]
        else:
            orders[card[1]].append(card[0])
    return orders


def is_identical_order(prev_orders, after_orders):
    for key, value in prev_orders.items():
        if after_orders[key] != value:
            return False
    return True


def main():
    input_lines = sys.stdin.readlines()
    n = int(input_lines[0].rstrip())
    cards = [(x.split()[0], int(x.split()[1])) for x in input_lines[1:]]
    prev_orders = shcd_order(cards)
    quick_sort(cards, 0, n-1)
    after_orders = shcd_order(cards)
    if is_identical_order(prev_orders, after_orders):
        print('Stable')
    else:
        print('Not stable')
    [print(x[0], x[1]) for x in cards]
    return


main()
# -----------------------------
sys.stdin = sys.__stdin__
