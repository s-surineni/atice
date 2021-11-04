def reverse(array, st, ed):
    while st < ed:
        array[st], array[ed] = array[ed], array[st]
        st += 1
        ed -= 1


def rotate_array(array, ki):
    ki %= len(array)
    reverse(array, 0, len(array) - 1)
    reverse(array, 0, ki - 1)
    reverse(array, ki, len(array) - 1)


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate_array(nums, k)
print(nums)
