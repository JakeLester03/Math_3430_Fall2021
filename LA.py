#0 Vector Addition
"""Adds the two input vectors.
    Creates a result vector stored as a list of 0's the same length as the input 
    then overwrites each element of the result vector with the corresponding
    element of the sum of the input vectors. Achieves this using a for loop over
    the indices of result. 
    Args:
        vector_a: A vector stored as a list.
        vector_b: A vector, the same length as vector_a, stored as a list.

    Returns:
       The sum of the input vectors stored as a list. 
    
""" 
def add_vectors(vector_a:list[float],vector_b:list[float])->list[float]:
  result:list[float] = [0 for element in vector_a]
  for index in range(len(result)):
    result[index] = vector_a[index] + vector_b[index]
  return result  


#1 Salar-Vector Mult
"""
Multiplys a vector by a scalar. Creates a result vector stored as a list of 0's the same size of the input vector. Then we overwrite 
the elements with the corresponding result of the vector element scaled by the scalar. We can achieve this by using a for loop to toggle
through the result.
Args: 
    vector: A vector stored as a list
    scalar: a scalar represented as a float
Returns:
    the product of the vector and the scalar stored as a list.
"""
def scalar_vector_mult(vector:list[float], scalar:float)->list[float]:
    result:list[float] = [0 for elements in vector]
    for index in range(len(vector)):
        result[index]=vector[index] * scalar
    return result

#2 Scalar Matrix Multiplication
'''
Multiplys a Matrix by a scalar. We can create an empty list called result. A Matrix will be stored as a list of column vectors. Scalar
is scalar. By running a for loop over the indecies of the matirx. We can then multiply the corresponding elements of the column 
vectors by the scalar by using scalar_vector_mult. We can then append the result to our empty list and return the result.
Args:
    matrix: a list of column vectors
    scalar: a scalar represented as a float
Returns:
    the product of the matrix and the scalar stored as list of column vectors.
'''
def scalar_matrix_mult(matrix_a:list[float], scalar: float)->list[float]:
    result:list[float] = []
    for index in range(len(matrix_a)):
        result.append(scalar_vector_mult(matrix_a[index], scalar))
    return result

#3 Matrix Addition
'''
Used to find the sum of two matricies. We can create an empty list called result. Both matricies stored a column vectors. By indexing
over the elements in the stored columns of the first matrix, we can then use add_vectors to compute the sum of the corresponding
elements in the column vectores. Append the sum to the result which is the desired sum of the two matricies.
Args:
    matrix_a: a matrix stored as a list of column vectors
    matrix_b: another matrix of the same size as matrix_a.
Returns:
    the sum of the two matricies stored as a list of column vectors.

'''
def matrix_add(matrix_a:list[float], matrix_b:list[float])->list[float]:
    result:list[float] = []
    for index in range(len(matrix_a)):
        result.append(add_vectors(matrix_a[index], matrix_b[index]))
    return result

#4 Matrix Vector Multiplication
'''
Used to find the product of a matrix and a vector.
We will create a list of 0's equal to the size of the vector. We can then implement a linear combination
by multiplying the elements in the column vectors of matrix_a by the corresponding elements in the vectors. Uzing a for loop
over the indecies of the matrix, we can then use add_vectors to add the result and the product of scalar_vector_mult
until the result is overwritten.
Args:
    matrix_a: a list of column vectors stored as lists
    vectors: a vector stored as a list
Returns:
    a new matrix overwritten by the product of the elements in matrix_a and the vector stored as a list of column vectors.

'''
def matrix_vector_mult(matrix:list[float], vector:list[float])->list[float]:
    result:list[float] = [0 for element in matrix]
    for index in range(len(matrix)):
        result = (add_vectors(result, scalar_vector_mult(matrix[index], vector[index])))
    return result

#5 Matrix-Matrix Multiplication
'''
Used to find the multiplication of two matricies. Both matricies stored as lists of column vectors.
Initialize result as an empty list. By indexing though the columns in matrix_b we can calculate product of the 
two matricies by using the linear combination method 
by appending matrix_vector_mult, which will multiply by the coumns in matrix_a, to the result.

Args: 
    matrix_a: a list of column vectors stored as lists
    matrix_b: another matrix stored as a list fof column vectors. The number of columns of matrix_a will be equal to the number of
    rows matrix_b has.

Returns: 
    The product of the two matricies.
'''
def matrix_matrix_mult(matrix_a:list[float], matrix_b:list[float])->list[float]:
    result:list[float] = []
    for index in range(len(matrix_b)):
        result.append(matrix_vector_mult(matrix_a, matrix_b[index]))
    return result
