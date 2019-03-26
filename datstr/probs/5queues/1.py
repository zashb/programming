class Queue:
    def __init__(self, limit=10):
        self.queue = []
        self.limit = limit
        self.front = None
        self.rear = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def enQueue(self, item):
        if self.size >= self.limit:
            return print("queue overflow")
        else:
            self.queue.append(item)
        # if no element and elem is added at rear, thus front = rear
        if self.front is None:
            self.front = self.rear = 0
        else:
            self.rear = self.size
        self.size += 1

    def deQueue(self):
        if self.size == 0:
            return print("queue underflow")
        else:
            self.queue.pop(0)
            self.size -= 1
            if self.size == 0:
                self.front = self.rear = None
            else:
                self.rear = self.size - 1

    def queueRear(self):
        if self.rear is None:
            print("queue is empty")
        return self.queue[self.rear]

    def queueFront(self):
        if self.front is None:
            print("queue is empty")
        return self.queue[self.front]

    def size(self):
        return self.size


from collections import deque


# rem the whole thing
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        d = deque()
        out = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            # append pos to deque
            d += i,
            if d[0] == i - k:
                d.popleft()
            if i >= k - 1:
                out += nums[d[0]],
        return out


class checkStackPairwiseOrder(object):
    def checkStackPairwiseOrder(self, stk):
        queue = deque()
        pairwiseOrd = True
        # while stk is not empty,pop elems into queue
        while stk:
            queue.append(stk.pop())
        # while queue is not empty, dequeue into stack
        while queue:
            stk.append(queue.popleft())
        # while stk is not empty
        while stk:
            # stk pop() and queue append()
            n = stk.pop()
            queue.append(n)
            if stk:
                # stk pop() and queue append again
                m = stk.pop()
                queue.append(m)
                if abs(n - m) != 1:
                    pairwiseOrd = False
                    break
        while queue:
            stk.append(queue.popleft())
        return pairwiseOrd


if __name__ == "__main__":
    # print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))

    stk = deque()
    for i in [-2, -3,-4,-3, 11, 10, 5, 6, 20, 21]:
        stk.append(i)
    print(checkStackPairwiseOrder().checkStackPairwiseOrder(stk))
