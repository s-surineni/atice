# https://practice.geeksforgeeks.org/editorial.php?pid=3020
test_cases = int(input().strip())

for a_tc in range(test_cases):
    pat_len = int(input().strip())

    for t1 in range((2 * pat_len) - 1):
        for t2 in range((2 * pat_len) - 1):
            print(1 + max(abs(pat_len - t1 - 1),
                          abs(pat_len - t2 - 1)), end='')
        print()
