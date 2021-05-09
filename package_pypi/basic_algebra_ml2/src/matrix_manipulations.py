from basic_operations import Basic_Operations
import numpy as np


class Operations_One_Matrix(Basic_Operations):
    """This class performs basic operations with a matrix
    """

    def __init__(self, matrix1=None, matrix2=None):
        super().__init__()
        self.matrix1 = self.check_type_matrix(matrix1)
        self.matrix2 = self.check_type_matrix(matrix2)

    def scalar(self, number):
        """scalar : multiply a matrix by a scalar 

        Args:
            number: number to multiply by a matrix

        Return : result of the operation between matrices of type <<numpy.ndarray>>.
                If an error occurs, it returns a message indicating what the error is.
        """
        result = self.matrix1 * number
        return result

    def determinant(self):
        """determinant:  calculates the determinant of a matrix
        Return : an integer
        """
        determinat = np.linalg.det(self.matrix1)
        return determinat

    def shape(self):
        """shape: checks the dimensions of a matrix

        Return: Tuple of array dimensions.
        """
        dimensions = self.matrix1.shape
        return dimensions

    def inverse(self):
        """inverse : calculate the inverse of a matrix

        Return : result of the operation between matrices of type <<numpy.ndarray>>.
                If an error occurs, it returns a message indicating what the error is. 
        """
        try:
            if self.determinant() != 0 and (self.shape()[0] == self.shape()[1]):
                inverse = np.linalg.inv(self.matrix1)
            else:
                raise Exception

        except Exception as e:
            return f"Error: {e}"
        return inverse

    def transpose(self):
        """transpose: Invert or permute the axes of a matrix
        Return: returns the modified array with the matrix transpose
        """
        try:
            transpose = np.transpose(self.matrix1)
            return transpose

        except Exception as e:
            return f"Error: {e}"
