## Basic algebra for Machine Learning
This package performs basic operations between two matrices that are used in the field of machine learning such as: *addition, subtraction, multiplication and division*. It can also perform single matrix operations such as: *dot product, inverse matrix finding and determinant*.

### Installation
Run the following command in your terminal: 

```
$ pip install -i https://test.pypi.org/simple/ basic-algebra-ml==0.0.1 
```

### Usage

The package is composed of two classes:
<h4>1) Basic_Operations</h4> Parent class that has the following methods:

* **check_type_matrix:** checks if the parameters are a matrix of type ```<<numpy.ndarray>>```.

* **addition:** adds two matrices together. For example:
```
# Declare the matrix
[In]:   from basic_operations import Basic_Operations

        # Declare the matrix
        matrix1 = ([1, 6, 5], [6, 14, 34], [21, 12, 4])
        matrix2 = ([3, 2, 54], [21, 12, 9], [1, 6, 5])
      
        # Instantiate the class
        test = Basic_Operations(matrix1, matrix2)


        print(test.addition())

[Out]:  [[ 4.  8. 59.]
        [27. 26. 43.]
        [22. 18.  9.]]

```

* **subtraction:** subtraction of two matrices. With the matrices of the previous example, then we have the following result:
```

[In]:   print(test.subtraction())

[Out]:  [[ -2.   4. -49.]
        [-15.   2.  25.]
        [ 20.   6.  -1.]]

```

<br>

* **multiplication:** multiply two matrices.

*Note: Remember that to perform multiplication between matrices the number of rows must match the number of columns.*  

```
[In]:   matrix3 = ([8, 56, 7], [6, 14, 34], [9, 63, 5])
        matrix4 = ([36, 1, 2], [94, 9, 12], [3, 66, 1])

        test2 = Basic_Operations(matrix3, matrix4)

        print(test2.multiplication())

[Out]:  [[ 288.   56.   14.]
        [ 564.  126.  408.]
        [  27. 4158.    5.]]

```
Note the following example where the dimensions do not match between more matrices. The program will give a message indicating the error.

```
[In]:   matrix3 = ([8, 56, 7], [6, 14, 34], [9, 63, 5])
        matrix4 = ([36, 1, 2], [94, 9, 12])

        print(test2.multiplication())

[Out]:  Error: operands could not be broadcast together with shapes (3,3) (2,3)

```

<br>

* **division:** divide two matrices. See the following example:



Below are several examples of how you can use this package: 

```
[In]:   print(test2.division())

[Out]:  [[ 0.22222222 56.          3.5       ]
        [ 0.06382979  1.55555556  2.83333333]
        [ 3.          0.95454545  5.        ]]

```

<br>

* **dot:** Dot product of two arrays. See the following example:

```
[In]:   matrix5 = ([8, 56, 7], [6, 14, 34], [9, 63, 5])
        matrix6 = ([3, 2, 54], [21, 12, 9], [1, 6, 5])

        test3 = Basic_Operations(matrix5, matrix6)

        print(test3.dot())

[Out]:  [[1207.  730.  971.]
        [ 346.  384.  620.]
        [1355.  804. 1078.]]
```

<h4>2) Operations_One_Matrix: </h4> 

Child class that inherits from **Basic_Operations**.  With this class you can perform the following operations with a matrix: 

* **scalar:** multiply a matrix by a scalar

```
[In]:   from matrix_manipulations import Operations_One_Matrix


        matrix = ([36, 1, 2], [94, 9, 12], [3, 66, 1])
        
        test = Operations_One_Matrix(matrix)

        print(test.scalar(2))


[Out]:  [[ 72.   2.   4.]
        [188.  18.  24.]
        [  6. 132.   2.]]
```

* **shape:** checks the dimensions of a matrix.
```
[In]:   print(test.scalar(2))


[Out]:  (3, 3)
```

* **inverse:** calculate the inverse of a matrix



* **transpose:** Invert or permute the axes of a matrix