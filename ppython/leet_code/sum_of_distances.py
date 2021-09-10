# https://leetcode.com/problems/sum-of-distances-in-tree
from collections import defaultdict


def post_order(graph, parent, node, child_count, dist_sum):
    for ch in graph[node]:
        # (Better) (Notice) This is to stop sending method to go into infinite loop
        # because of the way we are storing graph
        if ch != parent:
            # (Better) (Notice) the above case also takes care of stop case
            # for recursion as leaf has only one child and child == parent
            post_order(graph, node, ch, child_count, dist_sum)
            child_count[node] += child_count[ch]
            dist_sum[node] += dist_sum[ch] + child_count[ch]
            # (Notice) need not return anything as result is being stored in lists
            # child_count, dist_sum

            # (Notice) dist_sum is just being used to calculate root result
            # it is not used while calculating values for individual node


def pre_order(graph, parent, node, child_count, dist_sum):
    for ch in graph[node]:
        if ch != parent:
            dist_sum[ch] = (
                dist_sum[node] - child_count[ch] + len(child_count) - child_count[ch]
            )
            pre_order(graph, node, ch, child_count, dist_sum)


def find_sum_of_distances(edge_count, edge_list):
    graph = defaultdict(set)

    for p1, p2 in edge_list:
        graph[p1].add(p2)
        graph[p2].add(p1)

    print("*" * 80)
    print("ironman graph", graph)
    child_count = [1] * edge_count
    dist_sum = [0] * edge_count
    post_order(graph, None, 0, child_count, dist_sum)
    pre_order(graph, None, 0, child_count, dist_sum)
    return dist_sum


n = 6
edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
print(find_sum_of_distances(n, edges))
