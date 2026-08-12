class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    # not sorted. Should I sort? Want val1 + val2 + val3 = 0. hashmap?
        nums.sort() #first the elements so we can use two pointers 
        res = []    #initialize result array
        for i in range(len(nums)):  #first iteration over the whole array
            target = -1*nums[i] #this is our target, since we want val1 = -val2 - val3 

            if i > 0 and nums[i] == nums[i - 1]:    #checking that we don't make duplicates
                continue

            j, k = i + 1, len(nums) - 1 #search space to right of i, using j and k
            while j < k :   #we don't want to compare the els in the same indices
                if nums[j] + nums[k] == target: #check if the vals sum to target
                    res.append([nums[i], nums[j], nums[k]]) #if yes, then append
                    while j < k and nums[j] == nums[j + 1]: #then we have to make j,k along so there's no duplcates
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] < target:    #if the sum is less than target, then increment j only
                    j += 1
                else:   #otherwise the sum is greater than the target, so decrement k only
                    k -= 1
        return res

# time: O(n^2)
# space: O(1)