class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0 
        counts = defaultdict(int)
        max_freq = 0

        for right in range(len(s)):
            counts[s[right]] += 1

            max_freq = max(counts[s[right]], max_freq)

            while (right - left + 1) - max_freq > k:
                counts[s[left]] -= 1
                left += 1

        return right - left + 1
# time: O(n); n = length of string
# space: O(m); m = number of unique chars the string