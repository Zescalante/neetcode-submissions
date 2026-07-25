class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # can't use built-in library to convert

        #edge case: if either inputs are 0, then just return 0
        if num1 == '0' or num2 == '0':
            return '0'

        #arr to hold output, adding size of both inputs
        res = [0]*(len(num1) + len(num2))

        # we'll iterate through inputs reverse
        num1, num2 = num1[::-1], num2[::-1]

        #double looping
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1])*int(num2[i2])
                res[i1 + i2] += digit
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] = res[i1 + i2] % 10

        #reverse result, since we built it in reverse

        res, beg = res[::-1], 0

        # iterate through the unwanted 0s in the result
        while beg < len(res) and res[beg] == 0:
            beg += 1
        
        #now convert the significant digits to a string
        res = map(str, res[beg:])

        return ''.join(res)
