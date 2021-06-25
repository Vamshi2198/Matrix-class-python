# Matrix-class-python
This project uses object oriented programmig to implement a matrix class in python

## Objective
Python does not implement operations with matrix data type directly. A matrix can be created using a nested list data type and by using the numpy library in python. To account for this, I have created a simple matrix class that can be imported as a .py file.

## Prerequisites/Dependencies  
* For this project, I used [Visual Studio Code](https://code.visualstudio.com/download).
* To setup python in VS Code, follow instructions [here](https://code.visualstudio.com/docs/python/python-tutorial).
* You can also use [Jupyter Notebooks](https://jupyter.readthedocs.io/en/latest/install.html) or [Google Colab](https://colab.research.google.com/notebooks/intro.ipynb).

## Instructions
1. Clone this repository using `git clone https://github.com/Vamshi2198/Matrix-class-python`.
2. Make sure you create a new .py file or .ipynb notebook in the same directory where matrix.py file exists.
3. import the Matrix class using `from matrix import Matrix, zeroes, identity`. The zeroes and identity functions are defined in matrix class and are required to do some operations with matrices.
4. You can use the basic operations by calling `Matrix.(function/object name)`. The overloaded operators are called by using symbols.
5. you can add your own functions in matrix class. To test your functions, follow the unit test file provided and add tests to it.

## Supported Operations
   * Determinant, Trace and Inverse (for 1x1 and 2x2 only) of the matrix.
   * Addition, Subtraction, Negation, Multiplication and scalar multiplication of matrices.

## Examples
 ```
   m1 = Matrix([[1, 2],  
               [3, 4]])

   m2 = Matrix([[2, 5],
               [6, 1]])

   m3 = m1 + m2 # for addition.
   m4 = m1 - m2 # for subtraction.
   m5 = m1 * m2 # for multiplication, (a number) * matrix # for scalar multiplication.
   m6 = Matrix.determinant(m3) # for calculating determinant.
   m7 = Matrix.trace(m4) # for calculating trace.
   m8 = Matrix.inverse(m5) # for calculating inverse.
   m9 = Matrix.T(m2) # for transpose of a matrix.
 ```  


