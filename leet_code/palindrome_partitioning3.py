def calc_cost(sent, st, end):
    cost = 0
    while st < end:
        # print(st, end)
        if sent[st] != sent[end]:
            cost += 1
        st += 1
        end -= 1
    return cost
def palindrome_partition_dp(sent, idx, splits):
    sent_len = len(sent)
    if splits == 1:
        return calc_cost(sent, idx, sent_len - 1)
    elif splits == sent_len - idx:
        return 0
    else:
        cost = float('inf')
        for idx2 in range(idx, sent_len):
            cost = min(cost, calc_cost(sent, idx, idx2) + palindrome_partition_dp(sent, idx2 + 1, splits - 1))
        # print(idx, splits)
        
        # print('cost', cost)
        return cost


palindrome_partition_dp("aabbc", 0, 3)
