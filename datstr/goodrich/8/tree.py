class Tree:
    # abstract base class
    class Position:
        def element(self):
            raise NotImplementedError("must be implemented by subclass")

        def __eq__(self, other):
            raise NotImplementedError("must be implemented by subclass")

        def __ne__(self, other):
            return not (self == other)

    # ret pos of root else None
    def root(self):
        raise NotImplementedError("must be implemented by subclass")

    # ret pos of p's parent
    def parent(self,p):
        raise NotImplementedError("must be implemented by subclass")

    # ret #children of p
    def num_children(self,p):
        raise NotImplementedError("must be implemented by subclass")

    # ret iteration of pos of children
    def children(self,p):
        raise NotImplementedError("must be implemented by subclass")

    # ret #elems in tree
    def __len__(self):
        raise NotImplementedError("must be implemented by subclass")

    # concrete methods
    # ret True if pos p does not have any children
    def is_root(self,p):
        return self.root() == p

    # ret True is pos p doesnt have any children
    def is_leaf(self,p):
        return self.num_children(p) == 0

    # ret True if tree is empty
    def is_empty(self):
        return len(self) == 0

    # depth = #ancestors of p encluding p
    def depth(self,p):
        if self.is_root(p):
            return 0
        else:
            par = self.parent(p)
            return self.depth(par) + 1

    # height of subtree with root==p
    def height(self,p):
        if self.is_leaf(p):
            return 0
        else:
            heightList = []
            for i in self.children(p):
                heightList.append(self.height(i))
            return 1 + max(heightList)
        
