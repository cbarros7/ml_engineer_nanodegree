import unittest

from basic_operations import Basic_Operations
from matrix_manipulations import Operations_One_Matrix
import numpy as np


class TestBasicOperationClass(unittest.TestCase):
    def test_type(self):
        matrix1 = ([8, 56, 7], [6, 14, 34], [9, 63, 5])
        matrix2 = ([3, 2, 54], [21, 12, 9], [1, 6, 5])
        test = Basic_Operations(matrix1, matrix2)
        self.assertEqual(type(test.matrix1),
                         np.ndarray)

    def test_shape(self):
        matrix3 = ([8, 56, 7], [6, 14, 34], [9, 63, 5])
        test = Operations_One_Matrix(matrix3)
        self.assertEqual(test.shape(),
                         (3, 3))

    def test_determinant(self):
        matrix4 = ([1, 6, 5], [6, 14, 34], [21, 12, 4])
        test = Operations_One_Matrix(matrix4)
        self.assertEqual(round(test.determinant()), 2678)

    def test_child_class(self):
        child = Operations_One_Matrix()
        self.assertIsInstance(child, Basic_Operations)


if __name__ == '__main__':
    unittest.main()
