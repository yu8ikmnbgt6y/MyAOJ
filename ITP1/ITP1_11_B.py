import sys
import io
import time
import pprint

input_txt = """
1 2 3 4 5 6
3
6 5
1 3
3 2
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
        self.f_keys = [self.__TOP,  # 0
                       self.__FRONT,  # 1
                       self.__RIGHT,  # 2
                       self.__LEFT,  # 3
                       self.__BACK,  # 4
                       self.__BOTTOM  # 5
                       ]

        if face_val is None or len(face_val) != 6:
            face_val = ['1', '2', '3', '4', '5', '6']

        self.f_key_to_val = {}
        self.f_val_to_key = {}
        for f_key, val in zip(self.f_keys, face_val):
            self.f_key_to_val[f_key] = val
            self.f_val_to_key[val] = f_key

    MOVE_SWAP_FACES = {
        'S': [(__BACK, __TOP), (__TOP, __FRONT), (__FRONT, __BOTTOM), (__BOTTOM, __BACK)],
        'W': [(__RIGHT, __TOP), (__TOP, __LEFT), (__LEFT, __BOTTOM), (__BOTTOM, __RIGHT)],
        'E': [(__LEFT, __TOP), (__TOP, __RIGHT), (__RIGHT, __BOTTOM), (__BOTTOM, __LEFT)],
        'N': [(__FRONT, __TOP), (__TOP, __BACK), (__BACK, __BOTTOM), (__BOTTOM, __FRONT)],
        'RCW' : [(__LEFT, __FRONT), (__FRONT, __RIGHT), (__RIGHT, __BACK), (__BACK, __LEFT)],   # rotate clockwise
        'RCCW': [(__RIGHT, __FRONT), (__FRONT, __LEFT), (__LEFT, __BACK), (__BACK, __RIGHT)],   # rotate counter clockwise
    }

    def dice_move(self, direction_list):
        for direction in direction_list:
            prev_faces = self.f_keys[:]
            for prev_f, next_f in self.MOVE_SWAP_FACES[direction]:
                self.f_keys[next_f] = prev_faces[prev_f]
            #print(self.f_keys)

    MOVE_TO_TOP = {__TOP:[], __FRONT:['N'], __RIGHT:['W'], __LEFT:['E'], __BACK:['S'], __BOTTOM:['N','N']}

    def dice_fix(self, top, front):
        if type(top) == str:
            top = self.f_val_to_key[top]
            front = self.f_val_to_key[front]

        # 上面を指定された面にする
        if top != self.f_keys[self.__TOP]:
            now_top = self.f_keys.index(top)
            move = self.MOVE_TO_TOP[now_top]
            self.dice_move(move)

        if top != self.f_keys[self.__TOP]:
            raise AssertionError # not top

        # 前面を指定された面にする
        if front != self.f_keys[self.__FRONT]:
            for i in range(3):
                self.dice_move(['RCW'])
                if front == self.f_keys[self.__FRONT]:
                    break
            else:
                raise AssertionError    # 3回回転するうちに指定された面がfrontに来ないとおかしい

    def get_value(self, face):
        return self.f_key_to_val[self.f_keys[face]]

    def __repr__(self):
        return f'({",".join(map(str, self.f_keys))})'


faces = input().split()
nq = int(input())

dice = Dice(faces)
for q in range(nq):
    top_val, front_val = input().split()
    dice.dice_fix(top=top_val, front=front_val)
    print(dice.get_value(Dice._Dice__RIGHT))


# -----------------------------
print("elapsed:", time.time()-start)
sys.stdin = sys.__stdin__
