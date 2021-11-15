# TODO: do an example to see shared subproblems
def dp_find_if_matchstick_forms_square(matches, mask, used_so_far, cache,
                                       side_length, sides_formed):
    # used_so_far tells sum of match sticks what have been used so far
    if (mask, sides_formed) in cache:
        return cache[(mask, sides_formed)]
    match_count = len(matches)
    if sides_formed == 3:
        return True
    current_side = used_so_far % side_length
    left_in_side = side_length - current_side
    for bitt, val in enumerate(matches):
        if mask & (1 << bitt) and current_side + val <= side_length:
            current_side += val
            if current_side == side_length:
                sides_formed += 1
            ans = dp_find_if_matchstick_forms_square(matches, mask ^ 1 << bitt,
                                                     used_so_far + val, cache,
                                                     side_length, sides_formed)
            if ans: return ans
    cache[(mask, sides_formed)] = False
    return False


def find_if_matchstick_forms_square(matches):
    total = sum(matches)
    if total % 4:
        return False
    side_length = total / 4
    match_count = len(matches)
    used = (1 <<
            match_count) - 1  # will make number of bits equal to match count 1
    sides_formed = 0
    return dp_find_if_matchstick_forms_square(matches, used, 0, {},
                                              side_length, sides_formed)


# matches = [1, 1, 2, 2, 2]
matches = [3,3,3,3,4]
print(find_if_matchstick_forms_square(matches))
