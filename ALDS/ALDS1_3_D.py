import sys
import io

input_txt="""
\\///\_/\/\\\\/_/\\///__\\\_\\/_\/_/\
"""

fin = open('ALDS1_3_D_in.txt', 'r')
sys.stdin = fin


# copy the below part and paste to the submission form.
# ---------function------------
def main():
    line = input()
    deepen_x = []
    cur_x = 0
    ponds = []      # [(水たまりの最初の位置, 水量)]
    while len(line) > 0:
        #print(cur_x, ponds, deepen_x)
        tmp_char = line[0]
        if tmp_char == '\\':
            deepen_x.append(cur_x)
        elif tmp_char == '/' and len(deepen_x) != 0:
            pre_x = deepen_x.pop()
            volume = cur_x - pre_x
            if len(ponds) == 0:
                ponds.append([pre_x, volume])
            else:
                if pre_x < ponds[-1][0]:
                    # 前の水たまりと結合する
                    a = list(filter(lambda x: x[0] > pre_x, ponds))
                    pond = 0
                    for item in a:
                        pond += item[1]
                    [ponds.pop() for x in range(len(a))]
                    ponds.append([pre_x, pond + volume])
                else:
                    # 新しい水たまりを作成
                    ponds.append([pre_x, volume])
        cur_x += 1
        line = line[1:]

    print(sum([x[1] for x in ponds]))
    if len(ponds) == 0:
        print('0')
    else:
        print("{} ".format(len(ponds)) + " ".join([str(x[1]) for x in ponds]))

    return


main()
# -----------------------------
sys.stdin = sys.__stdin__
