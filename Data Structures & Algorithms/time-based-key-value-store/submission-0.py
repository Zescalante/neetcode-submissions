class TimeMap:
    def __init__(self):
        self.hashmap = defaultdict(list) #store [key, [vals]] 

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
    #since timestamps sorted ascending, use binary search 

        #list of sublists containing [values, timestamp] pairs
        candidate_list = self.hashmap[key]

        l, r = 0, len(candidate_list) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2

            if candidate_list[mid][1] > timestamp:
                r = mid - 1
            elif candidate_list[mid][1] <= timestamp:
                res = candidate_list[mid][0]
                l = mid + 1
        
        return res

        # binary search 
