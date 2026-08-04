class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # distance between first intersection and the beginning of the cycle
        # is same distance from the beginning to start of cycle
        slow, fast = 0, 0 #slow and fast index pointers

        while True: #start iterating
            slow = nums[slow]     #treat nums[i] as the "next" pointer. Move slow one step
            fast = nums[nums[fast]] #and move the fast by two

            if slow == fast:    #if the pointers are ever equal, then exit
                break

        slow2 = 0   #start a second slow pointer from start of list

        while slow != slow2:    #and step both slows one at time
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow2    #when both slows meet, that's the duplicate value

# time: O(n)
# space: O(1)