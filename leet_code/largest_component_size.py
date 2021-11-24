from collections import Counter, defaultdict
import math


class UnionFind:
    def __init__(self, nums):
        self.disjoint_set = list(range(nums))

    def find(self, ele):
        if self.disjoint_set[ele] != ele:
            self.disjoint_set[ele] = self.find(self.disjoint_set[ele])
        return self.disjoint_set[ele]

    def union(self, el1, el2):
        el1_p, el2_p = self.find(el1), self.find(el2)
        self.disjoint_set[el1_p] = el2_p


# def find_prime_factors(num, factor_set):
#     curr_factor = 2
#     while curr_factor <= math.sqrt(num) + 1:
#         if num % curr_factor == 0:
#             num //= curr_factor
#             factor_set.add(curr_factor)
#             return find_prime_factors(num, factor_set)
#         curr_factor += 1
#     if not factor_set:
#         factor_set.add(num)
#     return factor_set


# (Notice) interesting alternate implementation
# You can compare this with above implementation, beside having more code, it is still not enough to get correct res
def find_prime_factors(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return find_prime_factors(n // i) | set([i])
    return set([n])


def find_largest_component_size(nums):
    prime_indexes = defaultdict(list)
    num_len = len(nums)
    for idx, val in enumerate(nums):
        prime_factors = find_prime_factors(val)
        for a_fact in prime_factors:
            prime_indexes[a_fact].append(idx)
    print(prime_indexes)
    unfi = UnionFind(num_len)

    for fact, multiples in prime_indexes.items():
        for idx in range(len(multiples) - 1):
            unfi.union(multiples[idx], multiples[idx + 1])

    return max(Counter([unfi.find(ele) for ele in range(num_len)]).values())


nums = [2, 3, 6, 7, 4, 12, 21, 39]
print(find_largest_component_size(nums))
