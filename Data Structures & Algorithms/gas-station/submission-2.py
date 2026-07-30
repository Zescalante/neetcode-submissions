class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # linear search?
        if sum(gas) < sum(cost):    #if total gas sum is less than cost sum
            return -1       #then surely not possible

        total = 0   #initialize variable to hold running total of gas
        res = 0     #this holds the index i that allows circling around 
        for i in range(len(gas)):   #iteate through all stations
            total += gas[i] - cost[i]   #update the total of gas

            if total < 0:   #if total ever goes negative 
                total = 0   #we reset the total 
                res = i + 1 #and move the result index to i + 1

        return res

# time: O(n)
# space: O(1)