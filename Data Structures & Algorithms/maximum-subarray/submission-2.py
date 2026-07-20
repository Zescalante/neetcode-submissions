# DP SOLUTION. KADANE'S
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        best_sum = nums[0]  #initialize best and curr sums to first element
        curr_sum = nums[0]

        for i in range(1, len(nums)):   #loop through nums
            # set the current sum to the maximum of the current element and the curr_sum plus this value
            curr_sum = max(nums[i], curr_sum + nums[i])

            #update the best overall sum to the max of the best_sum so far and the current sum 
            best_sum = max(best_sum, curr_sum)

        return best_sum
# time: O(n)
# space: O(1)


        