class Solution:
    def isHappy(self, n: int) -> bool:
        # memoization? two pointers
        seen = set()

        def square_sum(val):
            string = str(val)
            return sum([int(x)**2 for x in string])

        num = n
        while True:
            if num == 1:
                return True

            if num in seen:
                # num = seen[num]
                # continue
                return False
            seen.add(num)
            num = square_sum(num)
            
            # seen[num] = square_sum(num)
