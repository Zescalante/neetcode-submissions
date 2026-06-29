class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0 #initialize count of ints not equal to val
        j = 0 #initialize index length of "new list"
        for i in range(len(nums)): #loop through length of nums
            if nums[i] != val:     #for values that aren't the val of interest
                k += 1             #increment count k by 1
                nums[j] = nums[i]  #swap values at indices j and i 
                j += 1             #increment j by 1
            # print(nums)
        nums = nums[:j]            #New "in-place" list is just rearranged list up to index j

        return k

# time: O(n)
# space: O(n)