class CountSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        point = tuple(point)    #change list to tuple so we can add as key

        #update counter of points
        if point in self.points:
            self.points[point] += 1
        else: 
            self.points[point] = 1

    def count(self, point: List[int]) -> int:
        counter = 0
        for p in self.points.keys():
            x_diff, y_diff = abs(p[0] - point[0]), abs(p[1] - point[1])

            if min(x_diff, y_diff) > 0 and (p[0], point[1]) in self.points and \
            (point[0], p[1]) in self.points:
                counter += self.points[(point[0], p[1])]*self.points[(p[0], point[1])]*\
                self.points[(p[0],p[1])]
        return counter
        
