class CountSquares:

    def __init__(self):
        self.points = {}    #dictionary to store new points how duplicates we get

    def add(self, point: List[int]) -> None:
        point = tuple(point)    #change list to tuple so we can add as key

        if point in self.points:  #update dictionary with new point
            self.points[point] += 1 
        else: 
            self.points[point] = 1

    def count(self, point: List[int]) -> int:
        counter = 0 #initialize counter for #ways to form square
        for p in self.points.keys():    #check all points in dictionary
            x_diff, y_diff = abs(p[0] - point[0]), abs(p[1] - point[1]) #calculate differences

            if min(x_diff, y_diff) > 0: #if both differences are greater than 0
                # we update the counter. The .get ensures if the point isn't store, it
                # just multiplies by zero and makes no contribution
                counter += \
                self.points.get((point[0], p[1]),0)*\
                self.points.get((p[0], point[1]),0)*\
                self.points.get((p[0],p[1]),0)
        return counter
        
        
