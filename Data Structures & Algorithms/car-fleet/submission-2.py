class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #first sort by position asc
        combined = [(p, s) for p, s in zip(position, speed)]
        combined.sort(key= lambda x: x[0])

        # iterate backwards
        fleet_count = 0
        stack = []
        for i in range(len(position) - 1, -1, -1):
            
            time_to_go = (target - combined[i][0])/combined[i][1]

            if stack:   #if there's a stack 
                if stack[-1] < time_to_go:  #check if current car takes longer than previous car
                    stack.append(time_to_go)  #if yes, then new fleet
                    fleet_count += 1
                else:
                    continue
            else:
                stack.append(time_to_go)
                fleet_count += 1

        return fleet_count

# time: O(nlogn)
# space: O(n)