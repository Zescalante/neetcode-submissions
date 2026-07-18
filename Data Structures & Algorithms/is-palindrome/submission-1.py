class Solution:
    def isPalindrome(self, s: str) -> bool:
        # TWO POINTER ARRAY PROBLEM

        # strip the string of unecessary characters first, and make lowercase
        s = "".join(c for c in s if c.isalnum()).lower()

        start, end = 0, len(s) - 1  #initialize index pointers at start and end of string  

        while start <= end:         #while the start and end indices aren't crossing
            if s[start] == s[end]:  #if the strings are equal
                start += 1          #move both pointers in
                end -= 1
            else:                   #otherwise they don't match, so we don't have a palindrome
                return False

        return True                 #if we make it to to this point, then it's a palindrome

# time: O(n)
# space: O(n). Could make O(1) if we don't convert the whole input at start. Instead convert each char during the pass?