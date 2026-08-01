class Solution:
    def jump(self, nums: List[int]) -> int:
        # linear search again. Greedy? Valid solution is guaranteed
        # min_steps = len(nums) #max answer would be length of list itself
        furthest = 0
        curr_end = 0
        jumps = 0
        # l, r = 0, 0
        # for i in range(len(nums) - 1, -1, -1):
        # while l <= r and r < len(nums) - 1 :
        for i in range(len(nums) - 1):
            furthest = max(furthest, i + nums[i]) #furthest idx
            # curr_end = i + nums[i]
            if i == curr_end:
                jumps += 1
                curr_end = furthest
            # while i < current_end
            # l, r = i, min(i + nums[i], len(nums) - 1)
            # max_i = l
            # for j in range(l, r + 1):
            # max_i = max(max_i, nums[j])

            # min_steps = min(min_steps, )

        return jumps

# time: O(n)
# space: O(1)