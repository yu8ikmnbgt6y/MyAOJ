import sys
import io

input_txt="""
4 2
1
2
2
6
"""


sys.stdin = io.StringIO(input_txt)
tmp = input()


# copy the below part and paste to the submission form.
# ---------function------------
import sys
def can_load(num_baggages, baggages, num_truck, max_load):
    bag_no = 0

    for i in range(num_truck):
        load_cap = max_load
        while load_cap > 0:
            if bag_no >= num_baggages:
                #print(max_load, "True")
                return True
            if load_cap >= baggages[bag_no]:
                load_cap -= baggages[bag_no]
                bag_no += 1
            else:
                break
    #print(max_load, bag_no >= num_baggages)
    return bag_no >= num_baggages

def main():
    num_baggages, num_trucks = map(int, input().split())
    baggages = list(map(int, sys.stdin.read().splitlines()))

    start = max(sum(baggages) // num_trucks, min(baggages))
    end = sum(baggages)

    while start < end:
        mid = (start + end) // 2
        if can_load(num_baggages, baggages, num_trucks, mid):
            end = mid
        else:
            start = mid + 1

    print(start)
    return


main()
# -----------------------------
sys.stdin = sys.__stdin__
