class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        output = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            output.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            smallest_val = min(intervals[i][0], newInterval[0])
            largest_val = max(intervals[i][1], newInterval[1])

            newInterval[0] = smallest_val
            newInterval[1] = largest_val
            i += 1

        output.append(newInterval)

        while i < n:
            output.append(intervals[i])
            i += 1
                
        return output

# time: O(n)
# space: O(1)