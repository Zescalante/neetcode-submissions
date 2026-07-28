class Solution:
    def myPow(self, x: float, n: int) -> float:

        def recursion(val, power):
            #base cases
            if val == 0:    #if the value is zero then power does nothing
                return 0
            
            if power == 0:  #if the power is zero then x^0 = 1
                return 1

            # recurse with interger division power // 2 
            half = recursion(val, power // 2)

            # for the output, if the power is even, then 
            # we multiply by itself to get original power
            if power % 2 == 0:
                return half*half

            # if power is odd, we need an extra factor of the value
            else:
                return half*half*val

        #in main function, check if power is negative
        # if yes, then we just take the inverse of the output
        if n < 0:
            res = 1 / recursion(abs(x), -n)
        #otherwise we store the output as normal
        else: 
            res = recursion(abs(x), n)
        return res

# time: O(logn)
# space: O(logn)