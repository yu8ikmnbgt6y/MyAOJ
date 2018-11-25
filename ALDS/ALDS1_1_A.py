import sys
import io

input_txt = """
3
1 2 3
"""

sys.stdin = io.StringIO(input_txt)
print(input())

# copy the below part and paste to the submission form.
# ---------function------------
def main():
    _ = input()
    array = [int(x) for x in input().split()]
    print(" ".join(map(str, array)))

    for i in range(1, len(array)):
        moving = array[i]
        j = i - 1
        while j >= 0 and moving < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = moving
        print(" ".join(map(str, array)))
    return


main()
# -----------------------------
sys.stdin = sys.__stdin__
