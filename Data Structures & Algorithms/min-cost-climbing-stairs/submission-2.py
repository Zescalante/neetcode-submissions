class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp bottom up solution
        cost.append(0) #make an index (val 0) for the top of the staircase. 

        for i in range(len(cost) - 3, -1, -1): #go backwards, start from 3rd to last
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])

# time: O(n)
# space: O(1)