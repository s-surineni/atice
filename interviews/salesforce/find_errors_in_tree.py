# https://github.com/xieqilu/Qilu-leetcode/blob/master/B219.GetSExpressionBT.cs
class Node:
    def __init__(self, ele):
        self.ele = ele
        self.children = []
        self.parent = None

def construct_tree(tree_nodes):
    node_objs = {}
    roots_objs = {}
    tree_nodes = tree_nodes.split()

    for a_node in tree_nodes:
        parent = a_node[1]
        child = a_node[3]

    if parent in node_objs:
        parent_node = node_objs[parent]
    else:
        parent_node = Node(parent)
        node_objs[parent] = parent_node

    if child in node_objs:
        child_node = node_objs[child]
    else:
        child_node = Node(child)
        node_objs[child] = child_node

    if not parent_node.parent:
        roots_objs[parent] = parent_node

    if child in roots_objs:
        del roots_objs[child]
    # may be this is another error
    if child_node.parent:
        return 'E2'
    else:
        child_node.parent = parent_node

    if child in parent_node.children:
        return 'E2'
    else:
        parent_node.children.append(child_node)

    if len(parent_node.children) > 2:
        return 'E1'


tree_nodes = '(B,D) (D,E) (A,B) (C,F) (E,G) (A,C)'
