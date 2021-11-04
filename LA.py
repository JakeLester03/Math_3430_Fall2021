#0 Vector Addition

def add_vectors(vector_a:list[float],vector_b:list[float])->list[float]:
"""
   Adds the two input vectors.
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
  result:list[float] = [0 for element in vector_a]
  for index in range(len(result)):
    result[index] = vector_a[index] + vector_b[index]
  return result  


#1 Salar-Vector Mult

def scalar_vector_mult(scalar:float, vector:list[float])->list[float]:
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
    result:list[float] = [0 for elements in vector]
    for index in range(len(vector)):
        result[index]=vector[index] * scalar
    return result

#2 Scalar Matrix Multiplication

def scalar_matrix_mult(matrix_a:list[float], scalar: float)->list[float]:
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
    result:list[float] = []
    for index in range(len(matrix_a)):
        result.append(scalar_vector_mult(matrix_a[index], scalar))
    return result

#3 Matrix Addition

def matrix_add(matrix_a:list[float], matrix_b:list[float])->list[float]:
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
    result:list[float] = []
    for index in range(len(matrix_a)):
        result.append(add_vectors(matrix_a[index], matrix_b[index]))
    return result

#4 Matrix Vector Multiplication

def matrix_vector_mult(matrix:list[float], vector:list[float])->list[float]:
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
    result:list[float] = [0 for element in matrix]
    for index in range(len(matrix)):
        result = (add_vectors(result, scalar_vector_mult(matrix[index], vector[index])))
    return result

#5 Matrix-Matrix Multiplication

def matrix_matrix_mult(matrix_a:list[float], matrix_b:list[float])->list[float]:
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
    result:list[float] = []
    for index in range(len(matrix_b)):
        result.append(matrix_vector_mult(matrix_a, matrix_b[index]))
    return result

####### -> HW04

#1 Absolute Value of Real and Complex

def absolute_value(scalar: complex or float) -> complex or float:
'''
    Used to compute both the absolute value of real and complex numbers. We can set the result equal to the real part 
    of the scalar squared plus the imaginary part of the scalar squared. Then we take the square root of that result
    to get the absolute value.

Args:
    A scalar stored in a computer as either a complex or float.

Returns:
    The absolute value of the complex or real number
'''
    result: complex or float = ((scalar.real**2) + (scalar.imag**2))
    result = result**(1/2)
    return result

#2 P-norm

def p_norm(vector: list, p: float = 2) -> float:
'''
    Used to find the P-norm of a vector that defaults to 2. We can initialize result as an empty list. We can then
    append our absolute value functions to the new list and take the absolute value of each element in the vector.
    In the same process we can take it to the pth power. Return result as the sum of all the elements raised to 
    the 1/pth power.

Args:
    - A vector stored as a list.
    - p is a float which defaults to 2.

Result:
    returns the p-norm
'''
    result:list[float] = []
    for index in range(len(vector)):
        result.append((absolute_value(vector[index])**p))
    return (sum(result))**(1/p)

#3 Infinity Norm

def infinity_norm(vector: list) -> float:
'''
    Used to find the infinity norm of a vector stored as a list. We initialize a result as an empty list.
    Then we append the absolute value of the indices of the input vector to our new list. Then we can return 
    the greatest value from the list.

Args:
    a vector stored as a list 

Result:
    returns the infinity norm of the vector list
'''
    result: list[float] = []
    for index in range(len(vector)):
        result.append(absolute_value(vector[index]))
    return max(result)

#4 Boolean norm

def boolean_norm(vector: list, p: float=2, boolean: bool = False) -> float:
'''
    Used to compute p-norm or infinity norm of a vector. If the boolean is False, it will default to the 
    p-norm using our p_norm function, where p = 2. If True, it will go on to calculate the infinity norm using the
    infinity_norm function.

Args:
    - a vector stored as a list.
    - a scalar p which defaults to 2.
    - a boolean which defaults as False

Result:
    The default result is the p-norm. If true, it will result as the infinity norm.
'''
    if boolean == False:
        return p_norm(vector, p)
    else:
        return infinity_norm(vector)
    

#5 Inner Product of Vectors

def inner_product(vector_a:list[float or complex], vector_b:list[float or complex]) -> float or complex:
'''
Used to calculate the inner product of vectors, whether they are complex or real.
Creates a result vector stored as a list of 0's the same size of the input vector. Then we overwrite 
the elements with the corresponding result of the vector element multiplied by the other vector using a 
for loop to iterate through the elements. Then we can take the sum of the result to get the inner product.

Args:
    - two vectors stored as lists with real or complex elements.

Result:
    The inner product of the two vectors.
'''
    result:list[float or complex] = [0 for elements in vector_a]
    for index in range(len(vector_a)):
        result[index]=vector_a[index] * vector_b[index]
    return sum(result)
vector_f = [2+1j, 3]
print(inner_product(vector_e, vector_f))
#(6-1j)
'''
