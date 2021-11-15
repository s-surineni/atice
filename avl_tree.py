import random
import math

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and key < root.left.val:
            return self.right_rotate(root)
        elif balance < -1 and key > root.right.val:
            return self.left_rotate(root)
        elif balance > 1 and key > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        elif balance < -1 and key < root.right.val:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root

    def right_rotate(self, root):
        new_root = root.left
        root.left = new_root.right
        new_root.right = root
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))
        new_root.height = 1 + max(self.get_height(new_root.left),
                                  self.get_height(new_root.right))
        return new_root

    def left_rotate(self, root):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))
        new_root.height = 1 + max(self.get_height(new_root.left),
                                  self.get_height(new_root.right))
        return new_root

    def get_height(self, root):
        if not root:
            return 0
        else:
            return root.height

    def get_balance(self, root):
        if not root:
            return 0
        else:
            return self.get_height(root.left) - self.get_height(root.right)

    def in_order(self, root):
        if not root:
            return
        self.in_order(root.left)
        print(root.val)
        self.in_order(root.right)


myTree = AVLTree()
root = None

root = myTree.insert(root, 10)
root = myTree.insert(root, 20)
root = myTree.insert(root, 30)
root = myTree.insert(root, 40)
root = myTree.insert(root, 50)
root = myTree.insert(root, 25)

"""The constructed AVL Tree would be 
            30 
           /  \ 
         20   40 
        /  \     \ 
       10  25    50"""
  
# Preorder Traversal 
print("Inorder traversal of the",
      "constructed AVL tree is")
myTree.in_order(root)
print()
