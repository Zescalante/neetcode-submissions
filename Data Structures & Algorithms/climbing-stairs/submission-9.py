# BOTTOM-UP (TABULATION) SOLUTION

class Solution:
    def climbStairs(self, n: int) -> int:
        
        def dp(n):
            # if n <= 2:
            #     return n

            # dp = [1, 1]
            one, two = 1, 1
            # i = 2
            for _ in range(n - 1):
                temp = one
                one = one + two
                two = temp

            return one
        
        return dp(n)