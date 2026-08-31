class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(start, path):
            if start == len(s):
                res.append(list(path))
                return 
            
            for end in range(start + 1, len(s) + 1):
                sub = s[start:end]
                if sub[:] == sub[::-1]:
                    path.append(sub)
                    backtrack(end, path)
                    path.pop()

        backtrack(0, [])
        return res

# time: O(n*2^n)
# space: O(n)