import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #linear iteration?
        # finite range of values (26). Bucket to get the counts
        counts = [0]*26
        time = 0
        
        for t in tasks:     #fill counts arr with frequencies
            counts[ord(t) - ord('A')] += 1
        max_heap = [-freq for freq in counts if freq != 0]  #store only non-zero freqs
        heapq.heapify(max_heap) #heapify the arr as a max heap

        q = deque() #initialize queue to store freqs and time when it can be processed 
        while q or max_heap:
            time += 1

            if q and q[0][1] == time:
                count_remain, _ = q.popleft()
                heapq.heappush(max_heap, -count_remain)
            if max_heap:
                frequency = -heapq.heappop(max_heap)
                frequency -= 1
                if frequency > 0:
                    q.append((frequency, time + n + 1))

        return time
        
# time: O(m); m = input array size
# space: O(1)