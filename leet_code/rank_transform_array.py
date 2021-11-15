def parse_input():
    nums = [int(i) for i in input('Please enter numbers separated by commas: ').split(',')]
    return nums

def rank_transform(arr):
    if not arr:
        return 
    vals_dict = {}


    dup_arr = arr[:]
    dup_arr.sort()
    rank_arr = []
    curr_rank = 1
    prev_val = dup_arr[0]
    for val in dup_arr:
        if  vals_dict.get(val):
            continue
        vals_dict[val] = curr_rank
        curr_rank += 1

    for val in arr:
        rank_arr.append(vals_dict[val])
    return rank_arr

arr = parse_input()
print(rank_transform(arr))


def arrayRankTransform(self, A):
    rank = {}
    for a in sorted(A):
        rank.setdefault(a, len(rank) + 1)
    return [rank[a] for a in A]
