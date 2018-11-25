import sys
import io

input_txt = """
44
"""

sys.stdin = io.StringIO(input_txt)
tmp = input()

# copy the below part and paste to the submission form.
# ---------function------------
def fibonacci(n):
    if n <= 1:
        return 1
    fib_array = [1] * 45

    for i in range(2, n+1):
        fib_array[i] = fib_array[i-1] + fib_array[i-2]
    return fib_array[n]

def main():
    n = int(input())
    fib = fibonacci(n)
    print(fib)
    return


main()
# -----------------------------
sys.stdin = sys.__stdin__
