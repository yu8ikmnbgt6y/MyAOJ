import sys
import io
import time
import pprint

input_txt = """
6
1 2 3 4 5 6
1 2 3 4 5 7
4 6 5 2 1 3
6 2 3 4 5 1
6 2 4 3 5 1
5 6 4 3 1 2
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
        for f_key, val in zip(self.f_keys, face_val):
            self.f_key_to_val[f_key] = val

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

    def dice_fix(self, top: int, front: int):
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

    OPPOSITE_AND_ROUNDS = {0: (5, (1, 3, 4, 2)),
                           1: (4, (0, 2, 5, 3)),
                           2: (3, (0, 4, 5, 1)),
                           3: (2, (0, 1, 5, 4)),
                           4: (1, (0, 3, 5, 2)),
                           5: (0, (1, 2, 4, 3))
                           }

    def is_identical(self, other) -> bool:
        # 含まれるvalueが同じであることをチェック
        self_values = [self.get_value(x) for x in self.f_keys]
        other_values = [other.get_value(x) for x in other.f_keys]
        if set(self_values) != set(other_values):
            return False

        other_top = other.get_value(self.__TOP)

        #other_topと同じ値を持つselfの面を取得
        self_top_faces = filter(lambda x: x[1] == other_top, self.f_key_to_val.items())

        #for　それぞれの面
        other_rounds = [other.get_value(x) for x in self.OPPOSITE_AND_ROUNDS[0][1]]
        other_rounds += other_rounds
        for self_top in self_top_faces:
            #   対面が同じ値 and 側面を回る面の値の列の循環が一致　を満たす場合があったらTrueなかったらFalse
            opposite, rounds = self.OPPOSITE_AND_ROUNDS[self_top[0]]
            if self.get_value(opposite) != other.get_value(self.__BOTTOM):
                continue
            self_rounds = []
            for face in rounds:
                self_rounds.append(self.get_value(face))
            for i in range(4):
                if self_rounds == other_rounds[i:i+4]:
                    return True
        return False

    def __repr__(self):
        return f'({",".join(map(str, self.f_keys))})'


def main():
    n = int(input())
    dice1 = Dice(input().split())

    for i in range(n-1):
        dice2 = Dice(input().split())
        if dice1.is_identical(dice2):
            print('No')
            break
    else:
        print('Yes')


main()


# -----------------------------
print("elapsed:", time.time()-start)
sys.stdin = sys.__stdin__
