import sys
import io
import time
import pprint

input_txt = """
012340abcdabcd012340
012340
"""

#sys.stdin = io.StringIO(input_txt); tmp = input()
sys.stdin = open('ALDS1_14_B_in21.test')
start_time = time.time()
# copy the below part and paste to the submission form.
# ---------function------------

def bmsearch(text, pattern):
    indices = []
    len_pattern = len(pattern)

    chars = []
    [chars.append(chr(ord('0')+i)) for i in range(10)]
    [chars.append(chr(ord('A')+i)) for i in range(26)]
    [chars.append(chr(ord('a')+i)) for i in range(26)]

    move_table = {c: len_pattern for c in chars}
    for char in sorted(set(pattern)):
        for i, idx in zip(range(len_pattern), range(len_pattern)[::-1]):
            if char == pattern[idx]:
                move_table[char] = i
                break

    move_table[pattern[-1]] = 1
    #print(move_table)
    i = 0
    end_search = len(text) - len_pattern
    while i <= end_search:
        match = True
        for j in range(len_pattern)[::-1]:
            if text[i+j] != pattern[j]:
                i += move_table[text[i+j]]
                #print(i,"not match", j, 'char:', text[i+j], " move:", move_table[text[i+j]])
                match = False
                break
        if match:
            print("match", text[i:i+len_pattern])
            indices.append(i)
            i += 1

    return indices

def main():
    text = input()
    pattern = input()

    indices = bmsearch(text, pattern)
    [print(index) for index in indices]
    return


main()
# -----------------------------
print("elapsed:", time.time()-start_time)
sys.stdin = sys.__stdin__
