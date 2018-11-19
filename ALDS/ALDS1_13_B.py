import sys
import io
import time
import pprint

input_txt = """
4 2 0
7 3 1
6 5 8
"""

sys.stdin = io.StringIO(input_txt); tmp = input()
#sys.stdin = open('ALDS1_14_D_in11.test')
#sys.stdout = open('out.txt','w')
start = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
import copy
from collections import deque

CORRECT_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
LIMIT = 100

class PuzzleState:
    def __init__(self, state, depth=0):
        self.state = state
        for j in range(3):
            for i in range(3):
                if state[j][i] == 0:
                    self.space_x = i
                    self.space_y = j
        self.depth = depth
        self.limit = 0

    def swap_state(self, x1, y1, x2, y2):
        self.state[y1][x1], self.state[y2][x2] = self.state[y2][x2], self.state[y1][x1]
        self.space_x, self.space_y = x2, y2

    def is_correct(self):
        return self.state == CORRECT_STATE

    def __repr__(self):
        tmp =""
        for j in range(3):
            for i in range(3):
                tmp += str(self.state[j][i])
            #tmp += '\n'
        return f'{tmp}'


move = {'up': (0, -1), 'down': (0, 1), 'left': (-1, 0), 'right': (1, 0)}
# directions_dict = {
#     'init' : ['up', 'down', 'left', 'right'],
#     'down' : [      'down', 'left', 'right'],
#     'up'   : ['up'        , 'left', 'right'],
#     'right': ['up', 'down'        , 'right'],
#     'left' : ['up', 'down', 'left'         ]
# }
def move_space(puzzle: PuzzleState):
    mem_state = []
    mem_state.append(puzzle.state)
    p_queue = deque()
    p_queue.append(puzzle)

    while len(p_queue) != 0:
        u = p_queue.popleft()
        if u.is_correct():
            #print("CORRECT")
            return u.depth
        for direction in ['up', 'down', 'left', 'right']:
            mx, my = move[direction]
            space_new_x, space_new_y = u.space_x + mx, u.space_y + my

            if not(0 <= space_new_x <= 2 and 0 <= space_new_y <= 2):
                continue
            tmp = PuzzleState(u.state,depth=u.depth+1)
            tmp.state = copy.deepcopy(u.state)
            tmp.swap_state(tmp.space_x, tmp.space_y, space_new_x, space_new_y)

            if tmp.state not in mem_state:
                mem_state.append(tmp.state)
                p_queue.append(tmp)
    return False


def solve_puzzle(input_state):
    return move_space(PuzzleState(input_state))


def main():
    tmp = [input().split() for x in range(3)]
    input_state = [[int(tmp[j][i]) for i in range(3)] for j in range(3)]


    # 8 puzzle
    ans_puzzle = solve_puzzle(input_state)
    print(ans_puzzle)



main()
# -----------------------------
print("elapsed:", time.time()-start)
sys.stdin = sys.__stdin__
