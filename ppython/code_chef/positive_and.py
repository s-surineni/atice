# https://www.codechef.com/OCT20B/problems/POSAND
import math


test_cases = int(input().strip())

for a_tc in range(test_cases):
    count = int(input().strip())
    if count == 1:
        print(1)
    elif math.log2(count) % 1 == 0:
        print(-1)

    elif count >= 3:
        print(2, 3, 1, end=' ')
        num = 4
        p2 = 4
        while num <= count:
            if num == p2:
                p2 *= 2
                if num + 1 <= count:
                    print(num + 1, num, end=' ')
                    num += 2
            else:
                print(num, end=' ')
                num += 1
        print()
    else:
        for val in [2, 3, 1][:count]:
            print(val, end=' ')
        print()
