class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointers? max amount of water = width*height -> (height of the smaller segment)*(distance between segments)

        start, end = 0, len(heights) - 1   #start from outside, since that's maximum distance
        max_amount = 0  #initialize max amount to 0
        while start < end:  #we don't want to compare the same height, since that's 0 container amount
            amount = min(heights[start], heights[end])*(end - start)
            max_amount = max(amount, max_amount)
            
            if heights[start] < heights[end]:  #we need get rid of the smaller segment, since that decides the height of the container
                start += 1
            elif heights[start] > heights[end]:
                end -= 1
            else:   #if both heights are the same, we just move both in. Or, could also just move one
                start += 1
                end -= 1

        return max_amount

# time: O(n)
# space: O(1)