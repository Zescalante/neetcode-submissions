class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #first sort by position asc
        combined = [(p, s) for p, s in zip(position, speed)]
        combined.sort(key= lambda x: x[0])

        # iterate backwards
        stack = [] #storing separate fleets
        for i in range(len(position) - 1, -1, -1):
            
            time_to_go = (target - combined[i][0])/combined[i][1]

            if stack:   #if there's a stack 
                if stack[-1] < time_to_go:  #check if current car takes longer than previous car
                    stack.append(time_to_go)  #if yes, then new fleet
                else:
                    continue
            else:   #if no stack, then we just append the time and increment count
                stack.append(time_to_go)

        return len(stack)

# time: O(nlogn)
# space: O(n)