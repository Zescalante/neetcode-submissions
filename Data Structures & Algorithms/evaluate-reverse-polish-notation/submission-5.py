class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ['-','+','*','/']
        for c in tokens:
            if c not in operations: 
                stack.append(int(c))

            else:
                y, x = stack.pop(), stack.pop()
                if c == '-':
                    stack.append(x - y)
                elif c == '+':
                    stack.append(x + y)
                elif c == '*':
                    stack.append(x * y)
                else:
                    stack.append(int(x / y))

        return stack[0]

# time: O(n); n = length of array
# space: O(n)