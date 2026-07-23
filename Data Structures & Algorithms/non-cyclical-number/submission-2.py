class Solution:
    def isHappy(self, n: int) -> bool:
        # memoization? two pointers
        seen = set()    #we just need to store the summed number, not the individual numbers

        # helper to square the values and sum
        def square_sum(val):
            # string = str(val)
            # return sum([int(x)**2 for x in string])
            tot = 0
            while val:
                 x = val % 10
                 x = x**2
                 tot += x
                 val = val // 10
            return tot



        num = n     #initialize a variable to hold current value
        while True: #start looping
            if num == 1:    #if the number is 1
                return True #then return 1 as requested

            if num in seen:     #or, if the number was already seen
                return False    #then we're in a cycle, so return False
            seen.add(num)       #otherwise, we add the number to seen
            num = square_sum(num)   #and update the number

# time: O(logn)
# space: O(logn)

