class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    # not sorted. Should I sort? Want val1 + val2 + val3 = 0. hashmap?
        nums.sort()
        res = []
        for i in range(len(nums)):
            target = -1*nums[i]

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, len(nums) - 1 #search space to right of i
            while j < k :
                if nums[j] + nums[k] == target:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    k -= 1
        return res

# time: O(n^2)
# space: O(1)