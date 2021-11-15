class BinarySearchTree:
    class Node:
        def __init__(self, ele):
            self.ele = ele
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def _add_root(self, ele):
        self.root = self.Node(ele)

    def _insert_value_recur(self, root, ele):
        if not self.root:
            self._add_root(ele)

        if ele > self.root.ele:
            self._insert_value_recur(root.right, ele)
        else:
            self._insert_value_recur(root.left, ele)

    def insert_value(self, ele):
        self._insert_value_recur(self.root, ele)

    def _delete_value_recur(self, root, ele):
        if not self.root:
            print("Value is not in the tree")
            return None

        if ele > root.ele:
            root.right = self._delete_value_recur(root.right, ele)
        elif ele == root.ele:
            return None
        else:
            root.left = self._delete_value_recur(root.left, ele)
        return root

    def delete_value(self, ele):
        self._delete_value_recur(self.root, ele)
