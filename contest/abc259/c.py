import copy
import sys

import numpy as np

S = list(input())
T = list(input())

def RLE_for(seq):
    comp_seq = []
    lengths = []

    comp_seq.append(seq[0])
    temp = seq[0]
    length = 1

    for i in range(1, len(seq)):
        if seq[i] != temp:
            lengths.append(length)
            comp_seq.append(seq[i])
            temp = seq[i]
            length = 1
        else:
            length+=1
    lengths.append(length)

    return comp_seq, lengths


S_comp_seq, S_lengths = RLE_for(S)
T_comp_seq, T_lengths = RLE_for(T)

if len(S_comp_seq) != len(T_comp_seq):
    print("No")
    exit()
else:
    for i in range(len(S_comp_seq)):
        if S_comp_seq[i] == T_comp_seq[i]:
            if S_lengths[i] >= 2 and S_lengths[i] <= T_lengths[i]:
                continue
            elif S_lengths[i] == 1 and S_lengths[i] == T_lengths[i]:
                continue
            else:
                print("No")
                exit()
        else:
            print("No")
            exit()
print("Yes")
