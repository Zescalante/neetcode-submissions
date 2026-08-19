import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # kth largest is smallest among top k largest elements
        self.heap = nums
        self.k = k

        heapq.heapify(self.heap)

    def add(self, val: int) -> int:

        heapq.heappush(self.heap, val)

        while len(self.heap) > self.k:
            heapq.heappop(self.heap) #removes smallest element
        
        return self.heap[0]