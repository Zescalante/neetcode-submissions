# TOP-DOWN (MEMOIZATION) SOLUTION

class Solution:
    def climbStairs(self, n: int) -> int:

        def memoization(i, cache):
            #base case
            # if n <= 1:
            #     return n
            # if n in cache:
            #     return cache[n]
            
            # cache[n] = climbStairs(n - 1, cache) + 

            if i >= n:
                return i == n
            if i in cache:
                return cache[i]

            cache[i] = memoization(i + 1, cache) + memoization(i + 2, cache)

            return cache[i]


        return memoization(0, {})