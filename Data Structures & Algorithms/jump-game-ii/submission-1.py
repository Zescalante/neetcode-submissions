class Solution:
    def jump(self, nums: List[int]) -> int:
        # linear search again. Greedy? Valid solution is guaranteed
        #initialize indices for furthest index reachable from any prior index to curr_end,
        #curr_end as furthest reachable index with curr jump value, and
        #jumps as a counter of steps taken
        furthest, curr_end, jumps = 0, 0, 0 

        for i in range(len(nums) - 1):  #iterate from idx 0 to n - 2 (don't care about value of last el)
            furthest = max(furthest, i + nums[i]) #update furthest idx

            if i == curr_end:   #if we've reached the current reachable end idx
                jumps += 1      #then we increment jump
                curr_end = furthest #and set the new curr_end

        return jumps    #return number of jumps. This will be the minimimum jumps

# time: O(n)
# space: O(1)