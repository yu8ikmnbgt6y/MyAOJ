import sys
import io
import time
import pprint

input_txt = """
1 2 3 4
6 7 8 0
5 10 11 12
9 13 14 15
"""

sys.stdin = io.StringIO(input_txt); tmp = input()
#sys.stdin = open('ALDS1_14_D_in11.test')
#sys.stdout = open('out.txt','w')
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
from collections import deque
CORRECT_STATE = "123456780"


class PuzzleState:
    __slots__ = ['state', 'spc_x', 'spc_y', 'depth']

    def __init__(self, state: str, depth=0):
        self.state = state
        index = state.find('0')
        self.spc_x = index % 3
        self.spc_y = index // 3
        self.depth = depth

    def swap_state(self, ch_x, ch_y):
        conv_char = self.state[ch_y * 3 + ch_x]
        self.state = self.state.replace('0', 'X')
        self.state = self.state.replace(conv_char, '0')
        self.state = self.state.replace('X', conv_char)
        self.spc_x, self.spc_y = ch_x, ch_y

    def is_correct(self):
        return self.state == CORRECT_STATE

    def __repr__(self):
        return f'{self.state}'


move = [(0, -1), (0, 1), (-1, 0), (1, 0)]
def puzzle8_breadth_first_search(puzzle: PuzzleState):
    mem_state = {puzzle.state: ''}
    p_queue = deque()
    p_queue.append(puzzle)

    while len(p_queue) != 0:
        u = p_queue.popleft()
        if u.is_correct():
            #print("CORRECT")
            return u.depth
        for mx, my in move:
            sp_new_x = u.spc_x + mx
            sp_new_y = u.spc_y + my
            if not(0 <= sp_new_x <= 2 and 0 <= sp_new_y <= 2):
                continue
            new_puzzle = PuzzleState(u.state, depth=u.depth+1)
            new_puzzle.swap_state(sp_new_x, sp_new_y)

            if new_puzzle.state not in mem_state:
                mem_state[new_puzzle.state] = ''
                p_queue.append(new_puzzle)
    return False


def main():
    input_text = ""
    for i in range(3):
        input_text += "".join(input().split())

    # 8 puzzle main
    ans_puzzle = puzzle8_breadth_first_search(PuzzleState(input_text))
    print(ans_puzzle)
    return

main()
# -----------------------------
print("elapsed:", time.time()-start)
sys.stdin = sys.__stdin__
