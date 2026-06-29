class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # students array rotates vales and dequeues: [1,0,0,1] -> [0,0,1,1] -> [0,1,1]
        # sandwiches array dequeues: [1,0,1] -> [0,1]
        
        # n = count = len(students) #number of students = number of sandwiches
        # #should I use linked list? Or dynamic array?
        # while count > 0:
        # # for i in range(n):
        #     if students[i] == sandwiches[0]:
        #         count -= 1

        ones = 0 
        zeros = 0

        for val in students: #getting count of student sandwich preferences
            if val == 1:
                ones += 1
            else:
                zeros += 1
        print(ones, zeros)
        
        for s in sandwiches:
            print(f"sandwich is {s}")
            if s == 1 and ones > 0:
                print("decrementing ones counter by one and removing student")
                ones -= 1
            elif s == 0 and zeros > 0: 
                print("decrementing zeros counter by one and removing student")
                zeros -= 1
            else:
                break
        
        # print(ones, zeros)
        return ones + zeros




