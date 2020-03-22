val = 'atta'

for idx in range(len(val)):
    for idx2 in range(idx, len(val)):
        if val[idx:idx2 + 1] == val[idx:idx2 + 1][::-1]:
            print(val[idx:idx2 + 1])
