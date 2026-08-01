class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # linear search. Greedy. Locally optimal choice. W
        # Whatever looks best right now.
        # iterate in reverse 

        n = len(nums)   #get size of arr

        target = n - 1 #target index is the last index

        for i in range(len(nums) - 2, -1 , -1): #iterate backwards, starting from second-to-last el
            jump = nums[i]  #get the current max jump dist. We can jump up to this far
            if jump >= target - i:  #if we can close the distance between here and target index
                target = i      #then we update target index to here

        return target == 0  #True if the target index got to index 0, else False

# time: O(n)
# space: O(1) 