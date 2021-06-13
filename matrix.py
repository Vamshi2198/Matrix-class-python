import math
from math import sqrt
import numbers
class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
 def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
            
        a = self.g[0][0]
        b = self.g[0][1]
        c = self.g[1][0]
        d = self.g[1][1]   
        return (a * d - b * c) 

def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
        
        trace = []
        non_trace = []
        for i in range (self.h):
            row = []
            for j in range (self.w):
                if i ==j:
                    row.append(self.g[i][j])
            trace.append(row)
            continue
        return trace

        