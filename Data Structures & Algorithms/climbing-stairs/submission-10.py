# BOTTOM-UP (TABULATION) SOLUTION

class Solution:
    def climbStairs(self, n: int) -> int:

        one, two = 1, 1 #initialize base cases. One way to finish with zero or one step

        for _ in range(n - 1):  #now take n - 1 steps
            temp = one          #temporarily store the old value of one
            one = one + two     #update one
            two = temp          #and put the old one into two now

        return one  #one now holds the solution!
    
# time: O(n)
# space: O(1)        
