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
