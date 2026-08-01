class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # linear search. Greedy. Locally optimal choice .
        # Whatever looks best right now/.
        # iterate in reverse 
        n = len(nums)

        target = n - 1 #target index

        for i in range(len(nums) - 2, -1 , -1): #iterate backwards, starting from second-to-last el
            jump = nums[i]
            if jump >= target - i:
                target = i

        return target == 0 
    
        # if nums[len(nums) - 2] == 0:
        #     return False

        # start = 0 
        # dist_remain = len(nums) - 2

        # for i in range(len(nums) - 2, -1 , -1): #iterate backwards, starting from second-to-last el
        #     max_jump = nums[i]


        #     nums[i] - nums[start],

# time: O(n)
# space: O(1) 