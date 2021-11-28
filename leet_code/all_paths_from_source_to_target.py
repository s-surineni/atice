# https://leetcode.com/problems/all-paths-from-source-to-target/
def find_all_paths_from_source_to_target_recur(graph, node, path, res):
    if node == len(graph) - 1:
        res.append(path)
        return
    else:
        for target in graph[node]:
            find_all_paths_from_source_to_target_recur(
                graph, target, path + [target], res
            )


def find_all_paths_from_source_to_target(graph):
    res = []
    # (Notice) observe how only one array is used to get all possible path
    find_all_paths_from_source_to_target_recur(graph, 0, [0], res)
    return res


graph = [[1, 2], [3], [3], []]
print(find_all_paths_from_source_to_target(graph))
