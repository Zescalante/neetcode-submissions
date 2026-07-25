class Solution:
    def reverseBits(self, n: int) -> int:
        
        res = 0     #initialize reversed integer
        for i in range(32): #this is 32 bit integer, so loop 32 times
            if (n >> i) & 1 == 1:   #bitshift right and check if there's a 1
                res |= (1 << (31 - i))  #now we use logical or (|) to place the 1 in res
        return res
# time: O(1)
# space: O(1)