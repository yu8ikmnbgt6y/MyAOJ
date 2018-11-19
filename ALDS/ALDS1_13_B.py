import sys
import io
import time
import pprint

input_txt = """
6 4 7
8 5 0
3 2 1
"""

sys.stdin = io.StringIO(input_txt); tmp = input()
#sys.stdin = open('ALDS1_14_D_in11.test')
#sys.stdout = open('out.txt','w')
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
from collections import deque
import bisect

CORRECT_STATE = "123456780"

class PuzzleState:
    def __init__(self, state: str, depth=0):
        self.state = state
        index = state.find('0')
        self.sp_x = index % 3
        self.sp_y = index // 3
        self.depth = depth
        self.limit = 0

    def swap_state(self, x1, y1, x2, y2):
        tmp = self.state[y2*3+x2]
        self.state = self.state.replace('0', 'X')
        self.state = self.state.replace(tmp, '0')
        self.state = self.state.replace('X', tmp)
        self.sp_x, self.sp_y = x2, y2

    def is_correct(self):
        return self.state == CORRECT_STATE

    def __repr__(self):
        return f'{self.state}'


move = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def move_space(puzzle: PuzzleState):
    mem_state = [puzzle.state]
    p_queue = deque()
    p_queue.append(puzzle)

    while len(p_queue) != 0:
        u = p_queue.popleft()
        if u.is_correct():
            #print("CORRECT")
            return u.depth
        for mx, my in move:
            space_new_x = u.sp_x + mx
            space_new_y = u.sp_y + my

            if not(0 <= space_new_x <= 2 and 0 <= space_new_y <= 2):
                continue
            tmp = PuzzleState(u.state, depth=u.depth+1)
            tmp.swap_state(tmp.sp_x, tmp.sp_y, space_new_x, space_new_y)

            idx = bisect.bisect_left(mem_state, tmp.state)
            if idx == len(mem_state) or mem_state[idx] != tmp.state:
                mem_state.insert(idx, tmp.state)
                #bisect.insort_left(mem_state, tmp.state)
                p_queue.append(tmp)
    return False


def solve_puzzle(input_state):
    return move_space(PuzzleState(input_state))


def main():
    intext =""
    for i in range(3):
        intext += "".join(input().split())

    # 8 puzzle
    ans_puzzle = solve_puzzle(intext)
    print(ans_puzzle)



main()
# -----------------------------
print("elapsed:", time.time()-start)
sys.stdin = sys.__stdin__
