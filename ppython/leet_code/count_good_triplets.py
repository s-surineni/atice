def find_if_good_triplet(a, b, c, x, y, z):
    if not abs(a - b) <= x:
        return False
    if not abs(b - c) <= y:
        return False
    if not abs(a - c) <= z:
        return False
    else:
        return True


def count_good_triplets(nums, x, y, z):
    num_len = len(nums)
    good_triplet_count = 0
    for a in range(num_len):
        for b in range(a + 1, num_len):
            for c in range(b + 1, num_len):
                if find_if_good_triplet(nums[a], nums[b], nums[c], x, y, z):
                    good_triplet_count += 1
    return good_triplet_count
