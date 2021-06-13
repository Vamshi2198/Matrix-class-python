import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

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
        
        diag = [self.g[i][i] for i in range(self.h)]
        for i in range(1, len(diag)):
            trace[i] = diag[i-1] + diag[i]
        return trace
        
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        inverse =[]
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
        if self.h == 1:
            inverse.append([1/self.g[0][0]])
        elif self.h == 2:
            if self.determinant() == 0:
                raise ValueError("Cannot find the inverse if determinant is 0")
            else:
                a = self.g[0][0]
                b = self.g[0][1]
                c = self.g[1][0]
                d = self.g[1][1]
        
                factor = 1 /(a * d - b * c)

            
                inverse = [[d, -b],[-c, a]]
            
                for i in range(len(inverse)):
                    for j in range(len(inverse[0])):
                        inverse[i][j] = factor * inverse[i][j]
        return Matrix(inverse)
    
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        matrix_transpose = []
    # Loop through columns on outside loop
        for c in range(self.w):
            new_row = []
        # Loop through columns on inner loop
            for r in range(self.h):
            # Column values will be filled by what were each row before
                new_row.append(self.g[r][c])
            matrix_transpose.append(new_row)
    
        return Matrix(matrix_transpose)

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError,"Matrices can only be added if the dimensions are the same") 
            # initialize matrix to hold the results
        matrixSum = []
    
    # matrix to hold a row for appending sums of each element
        row = []
    
    # For loop within a for loop to iterate over the matrices
        for r in range(self.h):
            row = [] # reset the list
            for c in range(self.w):
                row.append(self.g[r][c] + other.g[r][c]) # add the matrices
            matrixSum.append(row)
    
        return Matrix(matrixSum)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        result = zeroes(self.h,self.w)
    
    # For loop within a for loop to iterate over the matrices
        for r in range(self.h):
            for c in range(self.w):
                result[r][c] = -self.g[r][c]
    
        return result

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        matrixSub = []
    
    # matrix to hold a row for appending sums of each element
        row = []
    
    # For loop within a for loop to iterate over the matrices
        for r in range(self.h):
            row = [] # reset the list
            for c in range(self.w):
                row.append(self.g[r][c] - other.g[r][c]) # add the matrices
            matrixSub.append(row)
    
        return Matrix(matrixSub)

    def __mul__(self, other):
        
        def get_row(self, row):
            return self[row]
        
        def get_column(other, column_number):
            column = []
            
            for r in range(other.h):
                column.append(other[r][column_number])
            return column
    
        def dot_product(vector_one, vector_two):
            result = 0
    
            for i in range(len(vector_one)):
                result += vector_one[i] * vector_two[i]
            return result 
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        m_rows = self.h
        p_columns = other.w
        result=[]
        for r in range(m_rows):
            row_result = []
            rowA = (self.g[r])
            for c in range(p_columns):
                colB = get_column(other,c)
                dot_prod = dot_product(rowA, colB)
                row_result.append(dot_prod)
            result.append(row_result)
        return Matrix(result)

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
        scalar_mul = []
        for i in range(self.h):
            row =[]
            for j in range(self.w):
                row.append(other*self.g[i][j])
            scalar_mul.append(row)
        return Matrix(scalar_mul)
