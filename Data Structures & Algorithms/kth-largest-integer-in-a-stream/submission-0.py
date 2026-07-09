import heapq

class KthLargest:
    #min heap problem. Smallest value sits at the root. 
    #pop from root k times at start.
    # allowed to use heap library
    def __init__(self, k: int, nums: List[int]):
        self.nums = nums       #initialze nums
        self.k = k             #initialize k

        heapq.heapify(self.nums)    #turn nums into a min heap

        while len(self.nums) > self.k:  #if self.nums has more than k values
            heapq.heappop(self.nums)    #keep removing the smallest value until length = k

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)  #push a new value to the heap. Automatically gets sort correctly 

        if len(self.nums) > self.k:     #if the length of numns exceeds k
            heapq.heappop(self.nums)    #pop the smallest value!
        
        return self.nums[0]             #the root holds the k-th smallest value
        
