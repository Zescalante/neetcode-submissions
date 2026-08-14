class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_size, s2_size = len(s1), len(s2)

        if s1_size > s2_size:   #s1 can't be longer than s2
            return False

        s1_counts = [0]*26

        for c in s1:
            s1_counts[ord(c) - ord('a')] += 1

        left, right = 0,0
        sub_counts = [0]*26
        for right in range(s2_size):
            sub_counts[ord(s2[right]) - ord('a')] += 1

            if right - left + 1 > s1_size:
                sub_counts[ord(s2[left]) - ord('a')] -= 1
                left += 1

            if s1_counts == sub_counts:
                return True
            

        return False

# time: O(n); n = max length of both strings
# space: O(1)