import numpy as np


class Basic_Operations:
    """ Basic_Operations: This class performs basic operations between two matrices.
    """

    def __init__(self, matrix1=None, matrix2=None):
        """Instantiation method

        Args:
            matrix1 (np.ndarray): first matrix
            matrix2 (np.ndarray): second matrix
        """

        self.matrix1 = self.check_type_matrix(matrix1)
        self.matrix2 = self.check_type_matrix(matrix2)

    def check_type_matrix(self, matrix):
        """check_type_matrix: Check that the matrix is of type numpy to be able to perform
                              operations between matrices.

        Args:
            matrix : Matrix in which its type is checked.

        Return: A matrix of type <<numpy.ndarray>>.
        """
        if type(matrix) != np.ndarray and matrix != None:
            return np.asfarray(matrix)
        elif type(matrix) == np.ndarray and matrix != None:
            return matrix

    def addition(self):
        """addition: sum two matrix

        Return : result of the operation between matrices of type <<numpy.ndarray>>.
                If an error occurs, it returns a message indicating what the error is.
        """
        try:
            addition = self.matrix1 + self.matrix2

        except Exception as e:
            return f"Error: {e}"

        return addition

    def subtraction(self):
        """substraction : subtraction of two matrices

        Return : result of the operation between matrices of type <<numpy.ndarray>>. 
                If an error occurs, it returns a message indicating what the error is.
        """
        try:
            subtraction = self.matrix1 - self.matrix2

        except Exception as e:
            return f"Error: {e}"

        return subtraction

    def multiplication(self):
        """multiplication: multiply two matrices 

        Return : result of the operation between matrices of type <<numpy.ndarray>>. 
                If an error occurs, it returns a message indicating what the error is.
        """

        try:
            multiplication = self.matrix1 * self.matrix2

        except Exception as e:
            return f"Error: {e}"

        return multiplication

    def division(self):
        """division: divide two matrices 

        Return : result of the operation between matrices of type <<numpy.ndarray>>. 
                If an error occurs, it returns a message indicating what the error is.
        """

        try:
            division = self.matrix1 / self.matrix2

        except Exception as e:
            return f"Error: {e}"

        return division

    def dot(self):
        """dot: Dot product of two arrays

        Return : result of the operation between matrices of type <<numpy.ndarray>>. 
                If an error occurs, it returns a message indicating what the error is.
        """

        try:
            dot = np.dot(self.matrix1, self.matrix2)

        except Exception as e:
            return f"Error: {e}"

        return dot
