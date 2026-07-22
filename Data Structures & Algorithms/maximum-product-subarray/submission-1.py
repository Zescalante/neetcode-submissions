# BOTTOM UP DP. KADANE'S?
# we want the maximum product, NOT the indices of the subarray
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
    
        max_curr_prod = nums[0]     #need to store the current product from the subarray
        min_curr_prod = nums[0]
        max_prod = nums[0]      #store the maximum product acquired so far

        res = 0 

        for i in range(1, len(nums)):
            # curr_prod = max(nums[i]*curr_prod, nums[i])
            # max_prod = max(max_prod, curr_prod)

            old_max_curr = max_curr_prod
            max_curr_prod = max(nums[i]*old_max_curr, nums[i]*min_curr_prod, nums[i])
            min_curr_prod = min(nums[i]*old_max_curr, nums[i]*min_curr_prod, nums[i])

            res = max(max_curr_prod, res)

        return res

# time: O(n)
# space: O(1)