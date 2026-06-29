class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)       #Get length of array
        ans = [0]*2*n       #Initialize zero array of size 2n
        ans[:n], ans[n:] = nums[:n], nums[:n] #Fill the zero array with original array, twice

        return ans

# time: O(n)?
# space: O(n)