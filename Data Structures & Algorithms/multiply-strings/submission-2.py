class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1 == '0' or num2 == '0':
            return '0'
        
        res = [0]*(len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]

        for i in range(len(num1)):
            for j in range(len(num2)):

                res[i + j] += int(num1[i])*int(num2[j])
                res[i + j + 1] += res[i + j] // 10
                res[i + j] %= 10

        i = len(res) - 1
        while i > 0:
            if res[i] == 0:
                i -= 1
            else:
                break
        res = res[:i+1]
        res = res[::-1]
        res_string = ''

        for val in res:
            res_string += str(val)
        return res_string

            
            


# time: O(m*n)
# space: O(m + n)
