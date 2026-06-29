class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = [] #initialize the result stack

        for op in operations:
            if op == '+':
                res.append(int(res[-2]) + int(res[-1]))
            elif op == 'D':
                res.append(2*int(res[-1]))
            elif op == 'C':
                res.pop()
            else: 
                res.append(int(op))
        return sum(res)

# time: O(n)
# space: O(n)
