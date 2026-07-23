class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # stack to maintain times of fleets. LIFO
        fleet_stack = [] #we just need the length of this stack at the end

        #first combine the cars position and speeds into one array
        arr = [[p, s] for p,s in zip(position, speed)]
        
        #sort the array by DECREASING position for ease of calculating final speed
        arr.sort(reverse=True) #time O(nlogn)

        #loop through the cars
        for pos,s in arr:
            time_to_reach = (target - pos) / s  #find the time to reach the target

            #if there's at least on fleet in the stack, and time_to_reach is leq to last added fleet
            if fleet_stack and time_to_reach <= fleet_stack[-1]:
                continue    #then the car will join that fleet, so just move to next car

            # otherwise we append to the stack to make a new fleet
            fleet_stack.append(time_to_reach)

        #return the number of fleets at the end
        return len(fleet_stack)

# time: O(nlogn) 
# space: O(n)