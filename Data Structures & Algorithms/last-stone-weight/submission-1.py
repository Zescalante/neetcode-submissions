import heapq

class Solution:
    # max heap solution
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-val for val in stones] #prepare stones arr for max heaping

        heapq.heapify(max_heap)     #make the max heap

        while len(max_heap) > 1:    #while there's at least two elements in the heap
            x = -heapq.heappop(max_heap)    #grab the two largest elements
            y = -heapq.heappop(max_heap)    #x is always >= y, since we popped it first

            if x != y:      #if the two largest values are not equal
                heapq.heappush(max_heap, -(x - y))  #then we push the difference into the heap


        if len(max_heap) == 0:  #if no remaining elements in the heap
            return 0            #return 0 as request


        return -max_heap[0]     #otherwise we return the last remaining element
        