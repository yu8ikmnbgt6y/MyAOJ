import sys
import io
import time
import pprint

input_txt = """
3
3 0 1 3
1 3
3 0 1 2
8
1 0
2 1
3 1
4 2
5 2
6 2
7 2
8 2
"""

sys.stdin = io.StringIO(input_txt);input()
#sys.stdin = open('in.test')
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
import sys


class BitFlag:
    #ALL_ON  = 0xffffffffffffffff
    ALL_OFF = 0x0000000000000000

    def __init__(self, mask_digits):
        self.FLAGS = self.ALL_OFF
        self.MaskFor1bit = [1 << i for i in range(64)]
        self.Masks = [self.make_mask(digits) for digits in mask_digits]

    @staticmethod
    def make_mask(digits):
        ret = 0
        for digit in digits:
            ret += 1 << digit
        return ret

    def _test(self, i):
        return self.FLAGS & self.MaskFor1bit[i] != self.ALL_OFF

    def _set(self, m):
        self.FLAGS |= self.Masks[m]

    def _clear(self, m):
        self.FLAGS &= ~self.Masks[m]

    def _flip(self, m):
        self.FLAGS ^= self.Masks[m]

    def _all(self, m):
        return self.FLAGS & self.Masks[m] == self.Masks[m]

    def _any(self, m):
        return self.FLAGS & self.Masks[m] != self.ALL_OFF

    def _none(self, m):
        return self.FLAGS & self.Masks[m] == self.ALL_OFF

    def _count(self, m):
        return bin(self.FLAGS & self.Masks[m]).count('1')

    def _val(self, m):
        return self.FLAGS & self.Masks[m]


nm = int(input())
digits = []
for i in range(nm):
    k, *arg = map(int, input().split())
    digits.append(arg)

bf = BitFlag(digits)

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
    q, arg = lines[i].split()
    ans[i] = commands[q](int(arg))

[print(int(x)) for x in ans if x is not None]
# -----------------------------
print("elapsed:", time.time() - start)
sys.stdin = sys.__stdin__