class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0 #Final count of non-vals in the list
        j = 0 #Index count for placing the non-val vals at the beginning of list 

        for i, num in enumerate(nums): #Loop through the list 
            if num != val:             #if the num at index i is not val
                nums[j] = num          #Place value at i at index j (start of list)
                j += 1                 #Increment j by 1
                k += 1                 #increment k (counter) by 1

        return k 