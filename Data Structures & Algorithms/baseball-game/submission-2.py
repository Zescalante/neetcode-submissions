class Solution:
    def calPoints(self, operations: List[str]) -> int:

        res = []               #create new array (list) to hold scores     
        for i, op in enumerate(operations): #loop through operations
            if op == "+":           #if the op is a +
                res.append(res[-1] + res[-2]) #append sum of final two ints to res.
            elif op == "C":         #if op is a C
                res.pop()              #pop the last element from res
            elif op == "D":         #if op is a D
                res.append(2*res[-1])
            else:
                res.append(int(op))
            print(res)

        return sum(res)

# time: O(n)
# space: O(n)


        # tot = 0 
        
        # for i, op in enumerate(operations):
        #     if op == "+":
        #         res.append(int(res[i-1]) + int(res[i-2]))
        #     elif op == "C":
        #         res.pop()
        #     elif op == "D":
        #         res.append(2*int(res[-1]))
        #     else:
        #         total += int(op)
        #     print(res)

        # return sum(res)