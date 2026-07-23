class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # stack to maintain times of fleets. LIFO
        fleet_stack = []

        arr = [[p, s] for p,s in zip(position, speed)]
        arr.sort(reverse=True) #time O(nlogn)

        for pos,s in arr:
            time_to_reach = (target - pos) / s

            if fleet_stack and time_to_reach <= fleet_stack[-1]:
                continue

            fleet_stack.append(time_to_reach)

        return len(fleet_stack)

# time: O(nlogn) 
# space: O(n)