class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # students array rotates vales and dequeues: [1,0,0,1] -> [0,0,1,1] -> [0,1,1]
        # sandwiches array dequeues: [1,0,1] -> [0,1]

        #every student can eventually rotate through the same sandwich!

        ones = 0 
        zeros = 0

        for val in students: #getting count of student sandwich preferences
            if val == 1:
                ones += 1
            else:
                zeros += 1
        
        for s in sandwiches:

            if s == 1 and ones > 0:
                ones -= 1

            elif s == 0 and zeros > 0: 
                zeros -= 1
                
            else:
                break
    
        return ones + zeros




