import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # neg_arr = [-val for val in nums]
        heapq.heapify(nums)
        
        # for _ in range(k):
        #     val = -heapq.heappop(neg_arr)
        # return val

        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]
# time: O(nlogk); n = size of nums arr, k = rank of largest number returned
# space: O(k)