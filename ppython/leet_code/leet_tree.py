from collections import deque


class Tree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def construct_tree(node_list):
    node = Tree(node_list[0])
    bfs_structure = deque()
    bfs_structure.append(node)
    idx = 1

    while bfs_structure and idx < (node_list):
        node = bfs_structure.popleft()
        lc = node_list[idx]
        if lc != 'null':
            l_node = Tree(lc)
            node.left = l_node
            bfs_structure.append(l_node)
        idx += 1
