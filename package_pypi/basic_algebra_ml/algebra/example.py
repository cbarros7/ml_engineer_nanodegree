from basic_operations import Basic_Operations
from matrix_manipulations import Operations_One_Matrix
import numpy as np

#matrix1 = ([1, 6, 5], [6, 14, 34], [21, 12, 4])
#matrix2 = ([3, 2, 54], [21, 12, 9], [1, 6, 5])

#matrix1 = ([8, 56, 7], [6, 14, 34], [9, 63, 5])
matrix1 = ([36, 1, 2], [94, 9, 12], [3, 66, 1])


#test = Basic_Operations(matrix1, matrix2)
test2 = Operations_One_Matrix(matrix1)
# print(prueba)
# print(type(prueba.check_type_matrix(matrix2)))
#print(f'Result addition between matrix 1 and matrix 2: {test.addition()}')
# print(
#    f'Result subtraction between matrix 1 and matrix 2: {test.subtraction()}')
# print(
#    f'Result multiplication between matrix 1 and matrix 2: {test.multiplication()}')
# print(
#    f'Result dot multiplication between matrix 1 and matrix 2: {test.dot()}')

#print(f'Result division between matrix 1 and matrix 2: {test.division()}')

# print(test2.scalar(2))
print(test2.determinant())
print(test2.shape())
# print(round(test2.determinant()))
# print(test2.transpose())

# print(test.addition())
#print(np.asfarray([[11, 58, 61], [27, 26, 43], [10, 69, 10]]))
# print(np.testing.assert_array_equal(test.addition(),
# np.asfarray([[11, 58, 61], [27, 26, 43], [10, 69, 10]]), verbose = True))
# print(np.testing.assert_array_equal(
#  [1.0, 2.33333, np.nan], [np.exp(0), 2.33333]))
# print(type(matrix1))
