class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0 #sliding window. Growing from left
        res = 0 #initialize result length
        hashmap = {} #store char, index pairs

        while r < len(s):   #while there's still chars to check
            if s[r] in hashmap and hashmap[s[r]] >= l:  #if we find c is in hashmap and in the current sliding window range
                l = max(hashmap[s[r]] + 1, l)   #then update left pointer to index AFTER duplicate char, or l if it's greater
            hashmap[s[r]] = r   #place c, i in the hashmap
            res = max(r - l + 1, res)   #update largest size 
            r += 1  #and increment r

        return res

# time: O(n)
# space: O(m)