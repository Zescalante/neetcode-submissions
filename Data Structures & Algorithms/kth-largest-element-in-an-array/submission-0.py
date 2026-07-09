import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #min heap solution
        min_heap = nums
        heapq.heapify(min_heap)     #heapify the input into a min heap

        while len(min_heap) > k:    #if heap length is longer than k 
            heapq.heappop(min_heap) #pope the smallest elements until length is k

        if len(min_heap) == 0:      #edge case if final heap is empty. Don't think this is necessary
            return 0

        return min_heap[0]          #return the first element of heap. Guaranteed the k-th largest element