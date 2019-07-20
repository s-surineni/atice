class BinaryTreeNode:
    def __init__(self,
                 ele=None,
                 l_child=None,
                 r_child=None,
                 visit=None):
        self.ele = ele
        self.l_child = l_child
        self.r_child = r_child
        self.visit = visit


class LinkedBinaryTree:

    def __init__(self):
        self.root = None
        self.tree_size = 0

    def is_empty(self):
        return self.tree_size == 0

    def size(self):
        return self.tree_size

    def in_order(self, visit=None):
        if visit:
            self.visit = visit
            self.the_in_order(self.root)

    def the_in_order(self, node):
        if node != None:
            self.the_in_order(node.l_child)
            self.visit(node)
            self.the_in_order(node.r_child)

    def visit(self, node):
        print(node.ele, end=' ')
