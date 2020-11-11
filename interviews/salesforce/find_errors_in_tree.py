# https://github.com/xieqilu/Qilu-leetcode/blob/master/B219.GetSExpressionBT.cs
# https://github.com/niklabh/tree-error-checker/blob/master/checker.js

# Error Code          Type of error
# E1                 More than 2 children
# E2                 Duplicate Edges
# E3                 Cycle present
# E4                 Multiple roots
# E5                 Any other error
def construct_sexp(root):
    if not root:
        return ''
    lefts = rights = ''

    if root.children:
        root.children.sort(key=lambda node: node.ele)
        lefts = construct_sexp(root.children[0])
        if len(root.children) == 2:
            rights = construct_sexp(root.children[1])
    return '({}{}{})'.format(root.ele, lefts, rights)

class Node:
    def __init__(self, ele):
        self.ele = ele
        self.children = []
        self.parent = None

def construct_tree(tree_nodes):
    node_objs = {}
    roots_objs = set()
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
            roots_objs.add(parent)

        if child in roots_objs:
            roots_objs.remove(child)
        # may be this is another error
        # if child_node.parent:
        #     return 'E2'
        else:
            child_node.parent = parent_node

        if child in [ch.ele for ch in parent_node.children]:
            return 'E2'
        else:
            parent_node.children.append(child_node)

        if len(parent_node.children) > 2:
            return 'E1'

    if len(roots_objs) > 1:
        return 'E4'
    if not roots_objs:
        return 'E3'

    # checking for cycle
    visited = set()
    que = []
    root = roots_objs.pop()
    que.append(root)

    while que:
        nod = que.pop()
        if nod in visited:
            return 'E3'
        else:
            visited.add(nod)
            nodo = node_objs[nod]
            for ch in nodo.children:
                que.append(ch.ele)

    return construct_sexp(node_objs[root])

tree_nodes = '(B,D) (D,E) (A,B) (C,F) (E,G) (A,C)'
# (A(B(D(E(G))))(C(F)))

# tree_nodes = '(A,B) (A,C) (B,D) (D,C)'

print(construct_tree(tree_nodes))
