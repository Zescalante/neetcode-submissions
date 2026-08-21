import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        neg_arr = [-val for val in nums]
        heapq.heapify(neg_arr)
        
        for _ in range(k):
            val = -heapq.heappop(neg_arr)
        return val
# time: O(nlogk); n = size of nums arr, k = rank of largest number returned
# space: O(k)