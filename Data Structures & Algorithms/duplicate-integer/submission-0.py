class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        diction = {}
        
        if not nums:
            return False

        for val in nums:
            if val in diction:
            # diction[val] > 1:
                return True
            else:
                diction[val] = 1

        return False