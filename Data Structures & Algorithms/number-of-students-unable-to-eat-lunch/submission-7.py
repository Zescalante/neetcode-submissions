from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        n = len(students)  #get the total number of students
        q = deque(students) #initialize queue of students

        res = n             #start the result (#students unable to eat) at n
        
        for s in sandwiches:    #step through sandwiches in order
            count = 0           #start a counter at zero for the #student who have seen this sandwich
            while count < n and q[0] != s:  #while the count of students left is less than n, and the front student and s don't match
                curr = q.popleft()      #take the student from the front (left)
                q.append(curr)          #append to back of line
                count += 1              #and increment current student counter
            
            if q[0] == s:       #or, if the front student and s match
                q.popleft()     #remove the student 
                res -= 1        #and decrement number of students who haven't eaten a sandwich
            else:               #otherwise, break from loop
                break

        return res          #and return #students who couldn't eat