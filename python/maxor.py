#https://www.hackerearth.com/tracks/pledge-2015-easy/panda-and-xor/
arr = [1,2,3]
freq = [0] *128
lenOFreq = len(freq)
for i in range(lenOFreq):
    temp = [0]*128
    for j in range(128):
        if freq[j] != 0:
            temp[j^arr[i]] += freq[j]
    for j in range(128):
        freq[j] += temp[j]
    freq[arr[i]] += 1

    print freq
