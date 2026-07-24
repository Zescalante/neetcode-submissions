class Solution:
    def countBits(self, n: int) -> List[int]:
        size = n + 1    #n + 1 because we want to include 0
        res = [0]*size

        #val also happens to be the index of the array
        for val in range(size):
            idx = val

            while val:
                if val & 1:
                    res[idx] += 1
                val >>= 1
            
        return res
            