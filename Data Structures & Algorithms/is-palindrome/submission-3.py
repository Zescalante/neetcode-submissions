class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s.lower()
        # print(s)
        # s = s.replace(" ", "")

        front, back = 0, len(s) - 1

        while front < back:
            # print(s[front])
            while (not s[front].isalnum()) and front < back:
                front += 1
            while (not s[back].isalnum()) and front < back:
                back -= 1
            
            if s[front].lower() != s[back].lower():
                return False
                 
            front += 1
            back -= 1
        return True
        # return s == s[::-1]

# time: O(n)
# space: O(1)