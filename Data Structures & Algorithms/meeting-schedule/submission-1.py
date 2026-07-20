"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        if not intervals:   #if there's no meetings at all, return True
            return True

        intervals.sort(key=lambda x: x.start)   #sort intervals based on start times

        for i in range(len(intervals) - 1):     #intervals treated like a list. Step through from index 0 to n - 1
            if intervals[i].end > intervals[i+1].start: #if the end time of the first goes past the start time of the next, we have overlap
                return False        #so return False
        return True     #otherwise we've stepped through all without problem, so we can make all meetings

# time: O(nlogn + n) ~ O(nlogn)
# space: O(1) or O(n), depending on the sorting

        

