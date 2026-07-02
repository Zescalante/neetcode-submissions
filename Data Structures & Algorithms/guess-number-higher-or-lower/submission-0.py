# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        #typical binary search

        left, right = 0, n      #initialize left and right pointers to start and end values (the range)

        while left <= right:            #while the pointer aren't equal or crossed 
            mid = (left + right) // 2     #calculate the middle value
            print(mid, guess(mid))
            if guess(mid) > 0:          #if guess(middle value) return is > 0
                left = mid + 1          #then guess too small, so bring in left pointer
            elif guess(mid) < 0:        #or if guess too large
                right = mid - 1         #bring in the right (end) pointer value
            else:                       #else the guess(mid) returns 0
                return mid              #meaning the guess is equal to the target, so return the value
        
        return -1                       #if the pointers cross, value not found so return -1

            