class Solution:
    def calPoints(self, operations: List[str]) -> int:

        res = []
        for i, op in enumerate(operations):
            if op == "+":
                res.append(int(res[-1]) + int(res[-2]))
            elif op == "C":
                res.pop()
            elif op == "D":
                res.append(2*int(res[-1]))
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