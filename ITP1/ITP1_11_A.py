import sys
import io
import time
import pprint

input_txt = """
1 2 4 8 16 32
SE
"""

sys.stdin = io.StringIO(input_txt);input()
#sys.stdin = open('ITP2_1_C_in9.test')
#sys.stdout = open('out.test','w')
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
import sys


class Dice:
    __TOP = 0
    __FRONT = 1
    __RIGHT = 2
    __LEFT = 3
    __BACK = 4
    __BOTTOM = 5

    def __init__(self, face_val=None):
        self.faces = [self.__TOP,       # 0
                      self.__FRONT,     # 1
                      self.__RIGHT,     # 2
                      self.__LEFT,      # 3
                      self.__BACK,      # 4
                      self.__BOTTOM     # 5
                      ]

        if face_val is None or len(face_val) != 6:
            face_val = ['1', '2', '3', '4', '5', '6']

        self.FaceValue = {}
        for face, val in zip(self.faces, face_val):
            self.FaceValue[face] = val

    MOVE_SWAP_FACES = {
        'S': [(__BACK, __TOP), (__TOP, __FRONT), (__FRONT, __BOTTOM), (__BOTTOM, __BACK)],
        'W': [(__RIGHT, __TOP), (__TOP, __LEFT), (__LEFT, __BOTTOM), (__BOTTOM, __RIGHT)],
        'E': [(__LEFT, __TOP), (__TOP, __RIGHT), (__RIGHT, __BOTTOM), (__BOTTOM, __LEFT)],
        'N': [(__FRONT, __TOP), (__TOP, __BACK), (__BACK, __BOTTOM), (__BOTTOM, __FRONT)]
    }

    def dice_move(self, direction: str):
        prev_faces = self.faces[:]
        for prev_f, next_f in self.MOVE_SWAP_FACES[direction]:
            self.faces[next_f] = prev_faces[prev_f]

    def top_value(self):
        return self.FaceValue[self.faces[0]]

    def __repr__(self):
        return f'({",".join(map(str,self.faces))})'


faces = input().split()
directions = input()

dice = Dice(faces)
for direction in directions:
    #print(direction, dice, end=',to,')
    dice.dice_move(direction)
    #print(dice)

print(dice.top_value())


# -----------------------------
print("elapsed:", time.time()-start)
sys.stdin = sys.__stdin__
