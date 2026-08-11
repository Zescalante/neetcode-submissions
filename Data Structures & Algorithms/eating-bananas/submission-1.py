import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search. want minimum eating rate k to eat all piles. Max k would be
        # if all piles had max banana piles

        k_low = 1 #need to eat at least one banana an hour or else nothing happens
        k_high = max(piles) #upper k bound. If all piles had max # bananas then you need this rate to eat them all
        min_k = k_high
        while k_low <= k_high:
            candidate_k = (k_low + k_high) // 2

            run_h = 0
            for p in piles:
                run_h += math.ceil(p / candidate_k)
            
            if h < run_h:
                k_low = candidate_k + 1
            elif h >= run_h:
                min_k = min(min_k, candidate_k)
                k_high = candidate_k - 1
                
        return min_k

# time: O(nlogm); n = number of piles, m = max value in piles
# space: O(1)