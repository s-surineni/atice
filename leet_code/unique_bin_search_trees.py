# https://leetcode.com/problems/unique-binary-search-trees
def find_uniqe_bin_search_trees(nodes):
    res = [1, 1]
    for trk1 in range(2, nodes + 1):
        res.append(0)
        for trk2 in range(1, trk1 + 1):
            res[-1] += res[trk2 - 1] * res[trk1 - trk2]
    return res[-1]


nodes = 3
print(find_uniqe_bin_search_trees(nodes))
