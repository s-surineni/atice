class BinarySearchTree:
    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert_recur(self, root, val):
        if root.val > val:
            if not root.left:
                root.left = self.Node(val)
                return
            self.insert(root.left, val)
        else:
            if not root.right:
                root.right = self.Node(val)
                return
            self.insert(root.right, val)

    def insert(self, val):
        if not self.root:
            self.root = self.Node(val)
            return
        self.insert_recur(self.root, val)

    def search_recur(self, root, val):
        if not root.val:
            return None
        if root.val == val:
            return root
        if root.val > val:
            return self.search(root.left, val)
        else:
            return self.search(root.right, val)

    def search(self, val):
        return self.search_recur(self.root, val)
