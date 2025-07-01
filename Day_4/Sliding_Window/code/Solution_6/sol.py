import heapq
from collections import defaultdict

class DualHeap:
    def __init__(self, k):
        self.small = []  # Max heap
        self.large = []  # Min heap
        self.delayed = defaultdict(int)
        self.k = k
        self.small_size = 0
        self.large_size = 0

    def prune(self, heap):
        while heap and self.delayed[heap[0][1 if heap is self.large else 0]] > 0:
            val = heap[0][1 if heap is self.large else 0] if heap is self.large else -heap[0]
            self.delayed[val] -= 1
            heapq.heappop(heap)

    def balance(self):
        if self.small_size > self.large_size + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, (val, val))
            self.small_size -= 1
            self.large_size += 1
            self.prune(self.small)
        elif self.small_size < self.large_size:
            val = heapq.heappop(self.large)[0]
            heapq.heappush(self.small, -val)
            self.large_size -= 1
            self.small_size += 1
            self.prune(self.large)

    def insert(self, num):
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            self.small_size += 1
        else:
            heapq.heappush(self.large, (num, num))
            self.large_size += 1
        self.balance()

    def erase(self, num):
        self.delayed[num] += 1
        if num <= -self.small[0]:
            self.small_size -= 1
            if num == -self.small[0]:
                self.prune(self.small)
        else:
            self.large_size -= 1
            if self.large and num == self.large[0][0]:
                self.prune(self.large)
        self.balance()

    def get_median(self):
        if self.k % 2 == 1:
            return float(-self.small[0])
        else:
            return (-self.small[0] + self.large[0][0]) / 2

def medianSlidingWindow(nums, k):
    dh = DualHeap(k)
    res = []
    for i in range(k):
        dh.insert(nums[i])
    res.append(dh.get_median())

    for i in range(k, len(nums)):
        dh.insert(nums[i])
        dh.erase(nums[i - k])
        res.append(dh.get_median())

    return res
