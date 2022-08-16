# Matrix Addition
import numpy
matrix1=numpy.matrix([[1,2,3],[3,4,5],[1,2,3]])
matrix2=numpy.matrix([[2,3,4],[1,2,3],[3,4,5]])
matrix3=numpy.add(matrix1,matrix2)
print(matrix3)

# Matrix Substraction
import numpy
matrix1=numpy.matrix([[1,2,3],[3,4,5],[1,2,3]])
matrix2=numpy.matrix([[2,3,4],[1,2,3],[3,4,5]])
matrix3=numpy.subtract(matrix1,matrix2)
print(matrix3)

# Matrix Multiplication
import numpy
matrix1=numpy.matrix([[1,2,3],[3,4,5],[1,2,3]])
matrix2=numpy.matrix([[2,3,4],[1,2,3],[3,4,5]])
matrix3=numpy.matmul(matrix1,matrix2)
print(matrix3)

# Scalar Multiplication

import numpy
matrix1=numpy.matrix([[1,2,3],[3,4,5],[1,2,3]])
matrix2=2*matrix1
print(matrix2)


# Matrix Transpose

import numpy
matrix1=numpy.matrix([[1,2,3],[3,4,5],[1,2,3]])
print(matrix1)

matrix2=numpy.transpose(matrix1)
print(matrix2)
