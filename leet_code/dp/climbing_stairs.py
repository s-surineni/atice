# https://leetcode.com/problems/climbing-stairs/solution/
def find_ways_to_climb_stairs_rec(curr_step, total_stairs, mem):

    if curr_step > total_stairs:
        return 0
    elif curr_step == total_stairs:
        return 1
    elif mem[curr_step]:
        return mem[curr_step]
    mem[curr_step] = find_ways_to_climb_stairs_rec(
        curr_step + 1, total_stairs, mem
    ) + find_ways_to_climb_stairs_rec(curr_step + 2, total_stairs, mem)
    return mem[curr_step]


def find_ways_to_climb_stairs(total_stairs):
    mem = [0] * (total_stairs + 1)
    return find_ways_to_climb_stairs_rec(0, total_stairs, mem)


total_stairs = 1
total_stairs = 2
total_stairs = 3
total_stairs = 4
print(find_ways_to_climb_stairs(total_stairs))
