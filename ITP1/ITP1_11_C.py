import sys
import io
import time
import pprint

input_txt = """
1 2 3 4 5 6
6 5 4 3 2 1
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
                return False    # 3回回転するうちに指定された面がfrontに来ないとおかしい
        return True

    def get_value(self, face):
        return self.f_key_to_val[self.f_keys[face]]

    def is_identical(self, other) -> bool:
        # 含まれるvalueが同じであることをチェック
        self_values = [self.get_value(x) for x in self.f_keys]
        other_values = [other.get_value(x) for x in other.f_keys]
        if set(self_values) != set(other_values):
            return False

        #selfのtopとfrontをotherに合わせる、失敗したらidenticalではない
        other_top = other.get_value(self.__TOP)
        other_front = other.get_value(self.__FRONT)
        ret = self.dice_fix(other_top, other_front)
        if not ret:
            return False

        #全面が同じであることをチェック、すべて通過したらTrue
        for i in range(6):
            if self.get_value(i) != other.get_value(i):
                return False
        return True


    def __repr__(self):
        return f'({",".join(map(str, self.f_keys))})'


def main():
    d1_faces = input().split()
    dice1 = Dice(d1_faces)
    d2_faces = input().split()
    dice2 = Dice(d2_faces)
    print(['No','Yes'][dice1.is_identical(dice2)])

main()


# -----------------------------
print("elapsed:", time.time()-start)
sys.stdin = sys.__stdin__
