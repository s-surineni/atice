# https://leetcode.com/problems/bitwise-and-of-numbers-range/
def find_bitwise_AND_range(start, end):
    move_factor = 1
    while start != end:
        start >>= 1
        end >>= 1
        move_factor <<= 1
    return start * move_factor


start = 5
end = 7
print(find_bitwise_AND_range(start, end))
