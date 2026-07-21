#DP?? DFS?
class Solution:
    def rob(self, nums: List[int]) -> int:
        # print(nums)

        # money = 0 

        # for i in range(len(nums)):

        cache = {}
        def memo(i):
            if i > len(nums) - 1:
                return 0
            if i in cache:
                return cache[i]

            cache[i] = max(nums[i] + memo(i + 2), memo(i + 1))

            return cache[i]
        
        return memo(i=0)