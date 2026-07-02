import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        #h is always greater than or equal to len(piles)
        # we can find the upper bound for k
        #it's the max banana pile. If koko can eat that pile in one hour, then she can eat any in one hour
        upper_k = max(piles) 

        lower_k = 1         #set the lower bound for k. Can't have 0 bananas per hour.

        min_k = upper_k     #initialize minimum rate to the highest possible rate k      

        while lower_k <= upper_k:   #while the pointers don't cross
            mid_k  = (lower_k + upper_k) // 2   #find the middle k 

            # this is the condition to check. Sum the ceiling of each pile/mid k rate to find the total hours it'll take
            tot_hours = sum(math.ceil(p/mid_k) for p in piles)

            if tot_hours <= h:      #if less than h, then this is a candidate rate. 
                min_k = min(mid_k, min_k)   #So update min_k
                upper_k = mid_k - 1         #and move upper_k in
            else:                   #otherwise the tot_hours taken exceed the allotted hours
                lower_k = mid_k + 1 #so we need to increase the rate lower_k    
            
        return min_k                #after exiting while loop, return the minimum k

        