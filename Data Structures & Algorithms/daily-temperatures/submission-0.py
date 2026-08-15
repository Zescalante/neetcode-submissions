class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  #stack to hold indices in decreasing order
        res = [0]*len(temperatures)
        for i in range(len(temperatures) - 1, -1, -1): #iterate backwards
            #while there's a stack, and curr temp is geq temp at last added stack index
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop() #then pop. We're looking for a temp in stack that's less than curr temp

            res[i] = stack[-1] - i if stack else 0  #if there's any elements left, then update result
            stack.append(i) #and add the index to the stack as new highest temp

        return res

# time: O(n); n = size of input array
# space: O(n)