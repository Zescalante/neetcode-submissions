class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # one pass iteration
        # res = nums[0]
        # count = 1

        # for val in nums:
        #     inner_res = val
        #     inner_count = 1
        #     if val == res:
        #         count += 1
            
        slow, fast = nums[0], nums[0] #slow and fast index pointers

        while True:
            slow = nums[slow]     #treat nums[i] as the "next" pointer
            fast = nums[nums[fast]]

            if slow == fast:
                break

        fast = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            # print(slow)
            # print(fast)

        return fast

# time: O(n)
# space: O(1)