class CountSquares:

    def __init__(self):
        self.table = {}    #initialize a dictionary to store points and their occurrences

    def add(self, point: List[int]) -> None:
        point = tuple(point)    #convert the point from list to tuple so we can properly call it

        if point in self.table:     #if the tuple is already in the dictionary 
            self.table[point] += 1  #increment it's value by one
        else:
            self.table[point] = 1   #otherwise set it's value to one. Actually this might be redundant

    def count(self, point: List[int]) -> int:
        #we're given a point. Check this point against the added points
        # to see if any four (including input point) make a square
        
        # point = tuple(point)    #convert the input to a tuple. Not sure I need to do this?

        res = 0         #initialize number of ways to form squares with this point
        for p in self.table:    #go through points stored in the hashmap
            x_diff = abs(p[0] - point[0])   #find the diff in x and y
            y_diff = abs(p[1] - point[1])

            #for a square, x_diff and y_diff must be equal, and both diffs must be greater than 0 
            if x_diff == y_diff and x_diff > 0 and y_diff > 0:
                #if criteria met, then just multiply all values together.
                #.get() handles if the point is not in the hashmap
                res += self.table.get((p[0], p[1]), 0)*\
                        self.table.get((point[0], p[1]), 0)*\
                       self.table.get((p[0], point[1]), 0)
        return res
# time: O(n)
# space: O(n)