class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int) #dict with default 0 values
    
        for val in nums:        #fill the hashmap with counts
            hashmap[val] += 1

        # bucket sort. Highest possible frequency is len(nums)
        # each sublist will the integer with identical frequencies
        buckets = [[] for _ in range(len(nums) + 1)]

        # now fill the buckets using the map
        for val, freq in hashmap.items():   #backwards iteration
            buckets[freq].append(val)

        res = [] #initialize output list to store k most frequent elements
        for i in range(len(buckets) - 1, 0, -1):    #iterate backwards to see most frequent
            for num in buckets[i]:  #append the integers from their sublists 
                res.append(num)     
                if len(res) == k:   #if we've reach k most frequent, then return
                    return res


        # group numbers based on their frequencies from 1 to k
        # index of buckets represents frequency

# time: O(n)
# space: O(n)