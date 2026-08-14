class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0 #left pointer to increment when our replacement exceeds k
        counts = defaultdict(int)   #dict to store freq of current window elements
        max_freq = 0    #initialize max frequency 
        res = 0 #this is the length of largest substring. The result
        for right in range(len(s)): #iterate to end of string
            counts[s[right]] += 1   #update dict occurrences

            max_freq = max(counts[s[right]], max_freq)  #update max_freq so far

            while (right - left + 1) - max_freq > k: #if (length of sub) - max_freq is gt k
                counts[s[left]] -= 1   #then we increment left forward and update the dict
                left += 1
            res = max(right - left + 1, res)
        return res
# time: O(n); n = length of string
# space: O(m); m = number of unique chars the string