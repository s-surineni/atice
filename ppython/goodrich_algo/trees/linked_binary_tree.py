from .abstract_binary_tree import BinaryTree


class LinkedBinaryTree(BinaryTree):
    class _Node:
        __slots__ = '_element', '_parent', '_left_child', '_right_child'

        def __init__(self, element,
                     parent=None,
                     left_child=None,
                     right_child=None):
            self._element = element
            self._parent = parent
            self._left_child = left_child
            self._right_child = right_child

    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def get_element(self):
            return self._node._element

        def __eq__(self, other):
            return (type(self) is type(other) and
                    (self._node is other._node))

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        return self.Position(self, node) if node else None

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def get_root(self):
        return self._make_position(self._root)

    def get_parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def get_left_child(self, p):
        node = self._validate(p)
        return self._make_position(node._left_child)

    def get_right_child(self, p):
        node = self._validate(p)
        return self._make_position(node._right_child)

    def get_children_count(self, p):
        node = self._validate(p)
        count = 0

        if node._left_child:
            count += 1
        if node._right_child:
            count += 1
        return count

    def _add_root(self, e):
        if self._root:
            raise ValueError('Root exists already')
        self._root = self._Node(e)
        self._size = 1
        return self._make_position(self._root)

    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left_child:
            raise ValueError('Left child exists already')
        node._left_child = self._Node(e, node)
        self._size += 1
        return self._make_position(node._left_child)

    def _add_right(self, p, e):
        node = self._validate(p)
        if node._right_child:
            raise ValueError('Right child exists already')
        node._right_child = self._Node(e, node)
        self._size += 1
        return self._make_position(node._right_child)

    def replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete_node(self, p):
        if self.get_children(p) == 2:
            raise ValueError('Node has 2 children')  # deliberately wrote this before validate
        node = self._validate(p)
        node_child = node._left_child if node._left_child else node._right_child
        if node_child:
            node_child._parent = node._parent
        if node is self._root:  # then node will not have any parent
            self._root = node_child
        else:
            if node._parent._left_child is node:
                node._parent.left_child = node_child
            else:
                node.parent.righ_child = node_child
        self._size -= 1
        node._parent = node
        return node

    def _attach(self, p, t1, t2):
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('p must be leaf')
        if not type(t1) is type(t2) is type(self):
            raise TypeError('t1 and t2 must be of tree type')
        self._size += len(t1) + len(t2)

        if not t1.is_empty():
            t1._root._parent = node
            node._left_child = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right_child = t2._root
            t2._root = None
            t2._size = 0

    def preorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self._root):
                yield p

    def _subtree_preorder(self, p):
        yield p
        for c in self.get_children(p):
            for other in self._subtree_preorder(p):
                yield other

    def positions(self):
        # return self.preorder()
        pass

    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self._root):
                yield p

    def _subtree_postorder(self, p):
        for c in self.get_children(p):
            for other in self._postorder(c):
                yield other
        yield p

    def breadth_first(self):
        if not self.is_empty():
            fringe = LinkedQueue()
            fringe.enqueue(self._root)
            while not fringe.is_empty():
                pos = fringe.dequeue()
                yield pos
                for a_child in pos.get_children():
                    fringe.enqueue(a_child)

    def inorder(self):
        if not self.is_empty():
            for p in self._subtree_inorder(self._root):
                yield p

    def _subtree_inorder(self, pos):
        if self.get_left_child(pos):  # is this check necessary?
            for other in self._subtree_inorder(self.get_left_child(p)):
                yield other
        yield p
        if self.get_right_child(pos):
            for other in self._subtree_inorder(self.get_right_child(p)):
                yield other

    # def get_root(self, e):
    #     return self._make_position(self._root)

    def num_children(self, p):
        node = self._validate(p)

        count = 0
        if node._left_child:
            count += 1
        if node._right_child:
            count += 1
        return count
