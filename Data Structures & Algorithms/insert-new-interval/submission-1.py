class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #linear array seach
        output = [] #store the output ranges
        i = 0       #initialize the index counter for searching
        n = len(intervals)  #get the # of ranges

        #while we haven't reached the end of the list, and the end of the current
        # range is still smaller than the start of the new
        while i < n and intervals[i][1] < newInterval[0]:
            output.append(intervals[i])     #just add the range to the output
            i += 1          #and increment index

        # then, while we're still not at the end, and the start of the current range
        # is leq to the new range's end
        while i < n and intervals[i][0] <= newInterval[1]: 

            #then we find the smallest and largest values of the two
            smallest_val = min(intervals[i][0], newInterval[0])
            largest_val = max(intervals[i][1], newInterval[1])

            #and update the new to this range
            newInterval[0] = smallest_val
            newInterval[1] = largest_val
            i += 1      #and increment

        output.append(newInterval)  #then append the new range the output

        #if there's still remaining ranges to search, we just append them
        while i < n:
            output.append(intervals[i])
            i += 1
                
        return output

# time: O(n)
# space: O(n)