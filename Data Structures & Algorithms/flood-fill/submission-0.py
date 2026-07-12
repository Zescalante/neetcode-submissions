class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        orig_color = image[sr][sc]

        if orig_color == color:
            return image

        def dfs(arr, start_r, start_c, val):
            rows, cols = len(arr), len(arr[0])

            # if arr[start_r][start_c] == val:
            #     return arr

            if (min(start_r, start_c) < 0) or \
            (start_r == rows) or \
            (start_c == cols) or \
            (arr[start_r][start_c] != orig_color):
            # ((start_r, start_c) in visit) or \
            # (arr[start_r][start_c] == color):
                return 

            # visit.add((start_r, start_c))

            arr[start_r][start_c] = val

            dfs(arr, start_r + 1, start_c, val)
            dfs(arr, start_r - 1, start_c, val)
            dfs(arr, start_r, start_c + 1, val)
            dfs(arr, start_r, start_c - 1, val)

            return arr

        return dfs(image, sr, sc, color)