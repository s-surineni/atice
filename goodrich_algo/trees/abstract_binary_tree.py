from .abstract_tree import Tree


class BinaryTree(Tree):
    def get_left_child(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def get_right_child(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def sibling(self, p):
        parent = self.get_parent(p)
        if not parent:
            return None
        else:
            if p == self.get_left_child(parent):
                return self.get_right_child(parent)
            else:
                return self.get_left_child(parent)

    def get_children(self, p):
        left_child = self.get_left_child(p)
        if left_child:
            yield left_child
        right_child = self.get_right_child(p)
        if right_child:         # book has is not None, may be to work in situations when element is 0?
            yield right_child
