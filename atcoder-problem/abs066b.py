S = input()

# half_index = int(len(S)/2)
# front_s = S[:half_index]

# for i in range(len(S)-1, half_index-1, -1):
#     concat = front_s+S[half_index:i]
#     # print(concat[:int(len(concat)/2)], concat[int(len(S)/2):])

#     if concat[:int(len(concat)/2)] == concat[int(len(concat)/2):]:
#         print(len(concat))
#         exit()
#     # print(concat)

for i in range(len(S)-1, 0, -1):
    concat = S[:i]

    if concat[:int(len(concat)/2)] == concat[int(len(concat)/2):]:
        print(len(concat))
        exit()
