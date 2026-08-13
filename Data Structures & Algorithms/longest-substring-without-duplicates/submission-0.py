class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0 #sliding window. Growing from left
        sub = set() 
        res = 0
        while r < len(s):
            if s[r] in sub:
                while l < r and s[r] in sub:
                    sub.remove(s[l])
                    l += 1

            sub.add(s[r])
            res = max(r - l + 1, res)
            r += 1

        return res


        # max_sub_len = 0
        # for i in range(s):
        #     if s[i] in sub:
        #         max_sub_len = 0
        #         sub = set()
        #     else:
        #         sub.add(s[i])
        #         max_sub_len += 1

# time: O(n)
# space: O(m)