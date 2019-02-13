class KStacks:
    def __init__(self, k, n):
        self.k = k
        self.n = n
        self.list = [0] * n
        # All 'k' stacks are empty to begin with  (-1 denotes stack is empty)
        self.top = [-1] * self.k
        # Top of the free stack.
        self.free = 0
        # Points to the next element in either One of the 'k' stacks or The 'free' stack.
        self.next = [i + 1 for i in range(self.n)]
        self.next[self.n - 1] = -1

    def is_empty(self, sn):
        return self.top[sn] == -1

    # Check whether there is space left for pushing new elements or not.
    def is_full(self):
        return self.free == -1
