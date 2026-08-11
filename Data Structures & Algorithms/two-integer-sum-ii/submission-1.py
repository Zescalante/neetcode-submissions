class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #guaranteed one solution. Since arr is sorted, we can use two pointers and increment/decrement as needed
        i, j = 0, len(numbers) - 1  #start and end pointers
        while i != j:   #we don't want to check indentical indices
            curr_sum = numbers[i] + numbers[j]  #get the current sum
            if curr_sum > target:   #if we overshoot the target
                j -= 1  #then larger el index should be decremented
            elif curr_sum < target: #or if we're under, then
                i += 1  #increment lower index
            else:   #otherwise we have the desired pair, so return the indices
                return [i + 1, j + 1]  #make sure they're one-indexed

# time: O(n)
# space: O(1)