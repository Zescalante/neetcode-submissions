class Solution:
    def myPow(self, x: float, n: int) -> float:

        def recursion(val, power):
            #base cases
            if val == 0:
                return 0
            
            if power == 0:
                return 1


            half = recursion(val, power // 2)

            if power % 2 == 0:
                return half*half
            else:
                return half*half*val

            # # if the power is odd
            # if power % 2:
            #     # if power < 0:
            #     #     return val*recursion(val, power // 2)
            #     # else:
            #     return recursion(val, power // 2) * val
            # else: 
            #     return recursion(val, power // 2)**2

        if n < 0:
            res = 1 / recursion(abs(x), -n)
        else: 
            res = recursion(abs(x), n)
        return res
        # return res if n % 2 == 0 else 1 / res