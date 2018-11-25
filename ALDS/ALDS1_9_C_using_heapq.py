import sys
import io


sys.stdin = open("ALDS1_9_C_in4.txt", 'r')
#tmp = input()

# copy the below part and paste to the submission form.
# ---------function------------
import sys
import heapq
nodes = []
outputs = [None] * 2000000
_num_outputs = 0


calc_time = True
if calc_time:import time
def main():
    global _num_outputs
    if calc_time: start = time.time()
    commands = sys.stdin.readlines()
    for command in commands:
        if command[0] == 'i':
            #heapq.heappush(nodes, Node(int(command[7:])))
            heapq.heappush(nodes, -(int(command[7:])))
        elif command[1] == 'x':
            outputs[_num_outputs] = -heapq.heappop(nodes)
            _num_outputs += 1
        elif command[1] == 'n':
            break

    if calc_time: print(time.time() - start)
    for i in range(_num_outputs):
        #print(outputs[i])
        pass
    return


main()
# -----------------------------
sys.stdin = sys.__stdin__
