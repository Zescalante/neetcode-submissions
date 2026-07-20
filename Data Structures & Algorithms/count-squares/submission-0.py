class CountSquares:

    def __init__(self):
        # self.table = []
        self.table = {}

    def add(self, point: List[int]) -> None:
        point = tuple(point)

        if point in self.table:
            self.table[point] += 1
        else:
            self.table[point] = 1
        # self.table.append(point)

    def count(self, point: List[int]) -> int:
        #we're given a point. Check this point against the added points
        # to see if any four (including input point) make a square
        
        point = tuple(point)
        # point_diffs = []
        res = 0 
        for p in self.table:
            x_diff = abs(p[0] - point[0])
            y_diff = abs(p[1] - point[1])

            # if x_diff == 0 or y_diff == 0:
            #     continue

            if x_diff == y_diff and x_diff > 0 and y_diff > 0:
                # if [point[0], p[1]] in self.table and \
                # [p[0], point[1]] in self.table:
                #     res += self.table[[point[0], p[1]]]*self.table[[p[0], point[1]]]
                res += self.table.get((p[0], p[1]), 0)*\
                        self.table.get((point[0], p[1]), 0)*\
                       self.table.get((p[0], point[1]), 0)
        return res
            # if p + [x_diff, 0] in self.table and 
            #     p - [x_diff, 0] in self.table and 
            # point_diffs.append([x_diff, y_diff])
        
