class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        i = 0
        n = len(intervals)

        # iterate up to the point where we need to start inserting newinterval
        while i < n and newInterval[0] > intervals[i][1]:
            output.append(intervals[i])
            i += 1

        #now we handle overlapping
        while i < n and newInterval[1] >= intervals[i][0]:
            new_min = min(intervals[i][0], newInterval[0])
            new_max = max(intervals[i][1], newInterval[1])
            newInterval = [new_min, new_max]
            i += 1
        
        output.append(newInterval)

        while i < n:
            output.append(intervals[i])
            i += 1
            
        return output

# time: O(n)
# space: O(1)