class TimeMap:
    def __init__(self):
        self.hashmap = defaultdict(list) #store [key, [vals]] in a hashmap!

    def set(self, key: str, value: str, timestamp: int) -> None:

        # if not using default dict
        # if key not in self.hashmap:
        #     self.hashmap[key] = []

        self.hashmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
    #since timestamps sorted ascending, use binary search 
        #list of sublists containing [values, timestamp] pairs
        candidate_list = self.hashmap[key]

        l, r = 0, len(candidate_list) - 1
        res = ""    #if no sufficient answer, return ""

        while l <= r:
            mid = (l + r) // 2  #standard binary search

            #if we go past the time, then move right and keep searching
            if candidate_list[mid][1] > timestamp:
                r = mid - 1
            else:   #otherwise we're leq timestamp, so update res to rightmost value and move l
                res = candidate_list[mid][0]
                l = mid + 1
        
        return res

        # binary search 
