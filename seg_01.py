# https://practice.geeksforgeeks.org/problems/segregate-0s-and-1s/0
tc = int(input().strip())

for trk in range(tc):
    cnt = int(input().strip())
    arr = input().strip().split()
    arr = [int(i) for i in arr]
    left = 0
    right = len(arr) - 1

    while left < right:
        while left < right and arr[left] == 0:
            left += 1
        while left < right and arr[right] == 1:
            right -= 1

        if left < right:
            arr[left] = 0
            arr[right] = 1
            left += 1
            right -= 1

    for a_val in arr:
        print(a_val, end=' ')
    print()
