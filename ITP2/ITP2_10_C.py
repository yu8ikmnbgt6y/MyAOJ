import sys
import io
import time
import pprint

input_txt = """
14
1 0
1 1
1 2
2 1
0 0
0 1
0 2
0 3
3 3
4
5
6
7
8
"""

sys.stdin = io.StringIO(input_txt);input()
#sys.stdin = open('in.test')
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
import sys

class BitFlag:
    ALL_ON  = 0xffffffffffffffff
    ALL_OFF = 0x0000000000000000

    def __init__(self):
        self.FLAGS = self.ALL_OFF
        self.Masks = [1 << i for i in range(64)]

    def _test(self, i):
        return self.FLAGS & self.Masks[i] != self.ALL_OFF

    def _set(self, i):
        self.FLAGS |= self.Masks[i]

    def _clear(self, i):
        self.FLAGS &= ~self.Masks[i]

    def _flip(self, i):
        self.FLAGS ^= self.Masks[i]

    def _all(self):
        return self.FLAGS & self.ALL_ON == self.ALL_ON

    def _any(self):
        return self.FLAGS & self.ALL_ON != self.ALL_OFF

    def _none(self):
        return self.FLAGS & self.ALL_ON == self.ALL_OFF

    def _count(self):
        return bin(self.FLAGS).count('1')

    def _val(self):
        return self.FLAGS


bf = BitFlag()

commands = {'0': bf._test,
            '1': bf._set,
            '2': bf._clear,
            '3': bf._flip,
            '4': bf._all,
            '5': bf._any,
            '6': bf._none,
            '7': bf._count,
            '8': bf._val
            }

qn = int(input())
lines = sys.stdin.readlines()
ans = [None] * qn

for i in range(qn):
    q, *arg = lines[i].split()
    if len(arg):
        ans[i] = commands[q](int(arg[0]))
    else:
        ans[i] = commands[q]()

[print(int(x)) for x in ans if x is not None]
# -----------------------------
print("elapsed:", time.time() - start)
sys.stdin = sys.__stdin__