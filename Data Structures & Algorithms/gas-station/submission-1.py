class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # linear search?
        if sum(gas) < sum(cost):
            return -1

        # i, checked = 0, 0
        total = 0
        res = 0
        # while checked < len(gas):
        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                res = i + 1


            # print(i)
            # if i >= len(gas):
            #     i %= k
            #     print(i)
            # else: 
            #     i += 1
            # checked += 1
        return res
        # return i as starting index, if possible to circle, else -1

# time: O(n)
# space: O(1)