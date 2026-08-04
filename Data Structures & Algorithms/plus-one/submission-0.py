class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        size = len(digits)
        # digits ordered most to least significant
        
        res = [0]*(size + 1)
        carry, i = 1, 0
        for val in digits[::-1]: #start from least significant digit
            temp = carry + val

            res[i] += temp % 10
            carry = temp // 10

            i += 1
        if carry != 0:
            res[i] = carry
        
        res = res[::-1]

        k = 0
        while k < size:
            if res[k] == 0:
                k += 1
            else:
                break

        return res[k:]

# time: O(n)
# space: O(n)