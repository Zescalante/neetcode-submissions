class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0 #sliding window. Growing from left
        sub = set()  #set to store longest substring with unique els
        res = 0 #initialize result length
        hashmap = {} #store char, index pairs

        while r < len(s):   
            if s[r] in hashmap and hashmap[s[r]] >= l:
                # sub.remove(s[l])
                l = max(hashmap[s[r]] + 1, l)
                # while l < r and s[r] in sub:
                #     sub.remove(s[l])
                #     l += 1
            hashmap[s[r]] = r
            # sub.add(s[r])
            res = max(r - l + 1, res)
            r += 1

        return res

# time: O(n)
# space: O(m)