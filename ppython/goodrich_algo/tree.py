class Tree:
    '''Abstract base class representing a tree structure.'''
    class Position:
        '''An abstraction representing the location of a single element.'''
        def element(self):
            '''Return the element stored at this Position.'''
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            '''Return True if other Position represents the same location.'''
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            '''Return True if other Position does not represent
            the same location.'''
            return self != other

    def root(self):
        '''Return Position representing the tree's root (or None if empty).'''
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        '''Return Position representing p's parent (or None if p is root).'''
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        '''Return the number of children that Position p has.'''
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        '''Generate an iteration of Positions representing p's children.'''
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        '''Return the total number of elements in the tree.'''
        raise NotImplementedError('must be implemented by subclass')

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        '''Return the number of levels separating Position p from the root.'''
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))  # going top to bottom because of parent

    def _height1(self):
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))
    # shouldn't children be the method of node?
    def _height2(self, p):
        if self.root(p):        
            return 0
        else:
            return max(1 + (self._height2(c) for c in self.children(p)))  # why not p.children ?

    def height(self, p=None):
        if not p:
            p = self.root()
        return self._height2(p)
