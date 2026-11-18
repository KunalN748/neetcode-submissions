import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.heap = nums 
        self.target = k

    def add(self, val: int) -> int:

        heapq.heappush(self.heap, val)
        while len(self.heap) > self.target:
            heapq.heappop(self.heap)
        return self.heap[0]
