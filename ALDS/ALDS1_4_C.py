import sys
import io

input_txt="""
13
insert AAA
insert AAC
insert AGA
insert AGG
insert TTT
find AAA
find CCC
find CCC
insert CCC
find CCC
insert T
find TTT
find T
"""


sys.stdin = io.StringIO(input_txt)
tmp = input()


# copy the below part and paste to the submission form.
# ---------function------------
import sys

def main():
    lines = sys.stdin.readlines()
    n = int(lines[0])

    repo = {}
    for i in range(1, n + 1):
        command, acgt = lines[i].split()
        if command[0] == 'i':
            if acgt not in repo:
                repo[acgt] = 0
        elif command[0] == 'f':
            if acgt in repo:
                print('yes')
            else:
                print('no')
    return


main()
# -----------------------------
sys.stdin = sys.__stdin__
