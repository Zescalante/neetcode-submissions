class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # every value in nums should be a valid index, since all els are in [1, n]
        # need to find a cycle, so use slow, fast pointers

        slow, fast = nums[0], nums[0]

        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = nums[0]

        while slow != slow2:
            slow, slow2 = nums[slow], nums[slow2]

        return slow2
# time: O(n)
# space: O(1)