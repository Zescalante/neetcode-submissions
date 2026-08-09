class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #first sort by position asc
        combined = [(p, s) for p, s in zip(position, speed)]
        combined.sort(key= lambda x: x[0])

        # iterate backwards
        stack = [] #storing separate fleets
        for i in range(len(position) - 1, -1, -1):
            
            time_to_go = (target - combined[i][0])/combined[i][1]

            if stack and stack[-1] >= time_to_go:   #if there's a stack and current car takes less time than car in stack, then they become one fleet, so continue
                    continue
            stack.append(time_to_go) #otherwise we add the curr car to the stack

        return len(stack)

# time: O(nlogn)
# space: O(n)