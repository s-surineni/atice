# https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
# uncompleted
#!/bin/python3

import math
import os
import random
import re
import sys


def freqQuery(queries):
    arr = []
    dicti = {}
    freq_dict = {}
    for query in queries:
        print(query)
        if query[0] == 1:
            dicti[query[1]] = dicti.get(query[1], 0) + 1
            if freq_dict.get(dicti[query[1]]):
                freq_dict[(dicti[query[1]])] += 1
                if freq_dict.get(dicti[query[1]] - 1):
                    freq_dict[dicti[query[1]] - 1] -= 1
            else:
                freq_dict[dicti[query[1]]] = 1
                if freq_dict.get(dicti[query[1]] - 1):
                    freq_dict[dicti[query[1]] - 1] -= 1
        elif query[0] == 2:
            if dicti.get(query[1]):
                freq = dicti[query[1]]
                freq_dict[freq] -= 1
                dicti[query[1]] = (dicti[query[1]] - 1)
        else:
            freq = query[1]
            if freq in freq_dict:
                arr.append(1)
            else:
                arr.append(0)
        print('dicti', dicti)
        print('freq_dict', freq_dict)
    # print(dicti)
    return arr


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)
    print(ans)
    # for a in ans:
        # print(a)
    # fptr.write('\n'.join(map(str, ans)))
    # fptr.write('\n')

    # fptr.close()
