class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # every value in nums should be a valid index, since all els are in [1, n]
        # need to find a cycle, so use slow, fast pointers

        slow, fast = nums[0], nums[0]   #start them at the same spot, to avoid confusion

        while True:     #just use a true loop until the pointer are equal
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = nums[0] #then start a second slow at the start

        while slow != slow2:    # and loop until they're equal
            slow, slow2 = nums[slow], nums[slow2]

        return slow2    #slow2 will have the duplicate element
# time: O(n)
# space: O(1)