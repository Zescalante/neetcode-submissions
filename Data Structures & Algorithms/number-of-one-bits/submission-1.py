class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0   #initialize count of bits
        while n > 0:    #while the integer is still greater than 0
            if n & 1:   #then if there's a 1 on the far right, we have a single bit
                count +=1   #so incremement the count
            n = n >> 1      #and then bitshift to the right so we see next placement
        return count    #return the count of bits (1s) at the end

# time: O(n)
# space: O(1)