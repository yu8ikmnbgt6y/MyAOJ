import sys
import io

input_txt = """
5 100
p1 150
p2 80
p3 200
p4 350
p5 20
"""

sys.stdin = io.StringIO(input_txt)
print(input())

# copy the below part and paste to the submission form.
# ---------function------------


def main():
    n, q = map(int, input().split())
    queue = [[x for x in input().split()] for _ in range(n)]
    queue = [(x[0], int(x[1])) for x in queue]

    elapsed_time = 0
    while len(queue) > 0:
        process, time = queue.pop(0)
        if time > q:
            queue.append((process, time - q))
            elapsed_time += q
        else:
            elapsed_time += time
            print('{} {}'.format(process, str(elapsed_time)))

    return


main()
# -----------------------------
sys.stdin = sys.__stdin__
