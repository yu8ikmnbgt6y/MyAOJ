import sys
import io

input_txt = """
1 2 + 3 4 - *
"""

sys.stdin = io.StringIO(input_txt)
print(input())

# copy the below part and paste to the submission form.
# ---------function------------


def main():
    stack = []
    for char in input().split():
        if char in ['+', '-', '*']:
            right = int(stack.pop())
            left = int(stack.pop())
            if char == '+':
                c = left + right
            elif char == '-':
                c = left - right
            elif char == '*':
                c = left * right
            else:
                raise AssertionError
            stack.append(c)
        else:
            stack.append(int(char))

    print(stack[0])
    return


main()
# -----------------------------
sys.stdin = sys.__stdin__
