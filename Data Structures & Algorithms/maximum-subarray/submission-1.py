class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        best_sum = nums[0]
        curr_sum = nums[0]

        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            best_sum = max(best_sum, curr_sum)

        return best_sum


        