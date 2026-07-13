

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        #each student can pass through the same sandwich 

        #which students prefer what?
        one_counts = 0 
        zero_counts = 0
        for val in students:
            if val == 1:
                one_counts += 1
            else:
                zero_counts += 1

        for s in sandwiches:
            if s == 1 and one_counts > 0:
                one_counts -= 1
            elif s == 0 and zero_counts > 0:
                zero_counts -= 1
            else:
                break

        return one_counts + zero_counts

# time: O(n)
# space: O(1)