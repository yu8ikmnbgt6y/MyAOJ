import sys
import io
import time
import pprint

input_txt = """
1 6 15 0
14 11 5 7
10 9 8 3
2 13 12 4
"""
# input_txt=''''
# 1 2 3 4
# 6 7 8 0
# 5 10 11 12
# 9 13 14 15
# '''

sys.stdin = io.StringIO(input_txt); tmp = input()
#sys.stdin = open('ALDS1_14_D_in11.test')
#sys.stdout = open('out.txt','w')
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
import heapq
from collections import defaultdict


class ManhattanDistance:
    CORRECT_STATE = "bcdefghijklmnopa"  # b-p means 1 to 15; a means 0
    PANEL = [(0, 0), (1, 0), (2, 0), (3, 0),
             (0, 1), (1, 1), (2, 1), (3, 1),
             (0, 2), (1, 2), (2, 2), (3, 2),
             (0, 3), (1, 3), (2, 3), (3, 3)]

    MOVE_DIRECTION = defaultdict(list)
    MOVE = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    def __init__(self):
        self. MTD_TABLE = {ch: {} for ch in self.CORRECT_STATE}

        for true_ch, true_pos in zip(self.CORRECT_STATE, self.PANEL):
            for panel_ch, panel_pos in zip(self.CORRECT_STATE, self.PANEL):
                self.MTD_TABLE[true_ch][panel_ch] =\
                    abs(true_pos[0] - panel_pos[0]) + abs(true_pos[1] - panel_pos[1])

        for panel_x, panel_y in self.PANEL:
            for move_x, move_y in self.MOVE:
                new_x, new_y = panel_x + move_x, panel_y + move_y
                if 0 <= new_x < 4 and 0 <= new_y < 4:
                    self.MOVE_DIRECTION[panel_y * 4 + panel_x].append(new_y * 4 + new_x)

    def calc_total_manhattan_distance(self, state: str) -> int:
        total_dist = 0
        for true_ch, state_ch in zip(self.CORRECT_STATE, state):
            total_dist += self.MTD_TABLE[true_ch][state_ch]
        return total_dist

MTD = ManhattanDistance()

class PuzzleState:
    __slots__ = ['state', 'spc_idx', 'depth', 'dist', 'estimate']

    def __init__(self, state: str, spc_idx: int, depth=0, dist=-1):
        self.state = state
        self.spc_idx = spc_idx #state.find('a')
        self.depth = depth
        if dist != -1:
            self.dist = dist
        else:
            self.dist = MTD.calc_total_manhattan_distance(state)
        self.estimate = self.depth + self.dist

    def swap_state(self, new_spc_idx):
        swt_char = self.state[new_spc_idx]


        # 'a'と新しい位置の文字をスワップ
        if self.spc_idx < new_spc_idx:
            self.state = self.state[:self.spc_idx] + swt_char + self.state[self.spc_idx + 1:new_spc_idx] + 'a' + self.state[new_spc_idx+1:]
        else:# new_spc_idc < self.spc_idx
            self.state = self.state[:new_spc_idx] + 'a' + self.state[new_spc_idx+1:self.spc_idx] + swt_char + self.state[self.spc_idx+1:]

        true_ch_in_spc = MTD.CORRECT_STATE[self.spc_idx]
        true_ch_in_swt = MTD.CORRECT_STATE[new_spc_idx]

        #新しい距離 = 現在のMHT距離 + a,sw_charの移動先でのMHT距離 - a,sw_charの移動前のMHT距離
        self.dist += MTD.MTD_TABLE[true_ch_in_swt]['a']      + MTD.MTD_TABLE[true_ch_in_spc][swt_char] \
                   - MTD.MTD_TABLE[true_ch_in_swt][swt_char] - MTD.MTD_TABLE[true_ch_in_spc]['a']

        self.spc_idx = new_spc_idx
        self.estimate = self.depth + self.dist

    def __lt__(self, other):
        return self.estimate <= other.estimate

    #def __repr__(self):
    #    return f'{self.state}'
        #tmp = list(self.state)
        #tmp = ''.join(tmp[0:4]) + '\n' + ''.join(tmp[4:8]) +'\n' + ''.join(tmp[8:12]) + '\n' + ''.join(tmp[12:16])
        #return tmp



def puzzle15_breadth_first_search(puzzle: PuzzleState):
    state_depth = {puzzle.state: 0}
    puzzle_q = []
    heapq.heappush(puzzle_q, puzzle)

    while len(puzzle_q) != 0:
        u = heapq.heappop(puzzle_q)
        if u.state == MTD.CORRECT_STATE:
            return u.depth
        for new_spc_idx in MTD.MOVE_DIRECTION[u.spc_idx]:
            new_puzzle = PuzzleState(u.state, u.spc_idx, depth=state_depth[u.state]+1, dist=u.dist)
            new_puzzle.swap_state(new_spc_idx)

            if new_puzzle.state in state_depth:

                if new_puzzle.depth < state_depth[new_puzzle.state]:
                    state_depth[new_puzzle.state] = new_puzzle.depth
            else:
                #print('enqueue')
                state_depth[new_puzzle.state] = new_puzzle.depth
                heapq.heappush(puzzle_q, new_puzzle)

    return False


def main():
    input_text = ""
    for i in range(4):
        input_text += ''.join([chr(x + ord('a')) for x in map(int, input().split())])

    # 15 puzzle main
    idx = input_text.find('a')
    ans_puzzle = puzzle15_breadth_first_search(PuzzleState(input_text, idx))
    print(ans_puzzle)
    return


main()
# -----------------------------
print("elapsed:", time.time()-start)
sys.stdin = sys.__stdin__
