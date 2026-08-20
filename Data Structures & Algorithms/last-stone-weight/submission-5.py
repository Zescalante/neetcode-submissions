import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max heap
        
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            s1, s2 = -heapq.heappop(stones), -heapq.heappop(stones) #s1 >= s2

            if s1 > s2:
                heapq.heappush(stones, -(s1 - s2))
            elif s1 == s2:
                continue

        return -stones[0] if stones else 0


# time: O(nlogn)
# space: O(n)