class Solution:
    def isPalindrome(self, s: str) -> bool:
        front, back = 0, len(s) - 1 #two pointers. Checking by-character front and back

        while front < back: #while the pointers don't cross
            while (not s[front].isalnum()) and front < back:    #if the char at front isn't alphanumeric, while front still less than back
                front += 1  #than move front ahead
            while (not s[back].isalnum()) and front < back: #same for back
                back -= 1
            
            if s[front].lower() != s[back].lower(): #then check if the current chars are equal. If not, then False
                return False
                 
            front += 1  #else increment and decrement by one
            back -= 1   
        return True #if all conditions passed, then it's a palindrome

# time: O(n)
# space: O(1)