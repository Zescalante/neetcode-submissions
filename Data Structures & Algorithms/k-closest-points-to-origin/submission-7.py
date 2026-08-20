import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #use arr that maintains only k points. Efficient insertion/removal
        #min heap?

        arr = [[-(p[0]**2 + p[1]**2), p] for p in points] #dist from origin
        heapq.heapify(arr)

        while len(arr) > k:
            heapq.heappop(arr)

        return [p[1] for p in arr]

# time: O(nlogk)
# space: O(n)
