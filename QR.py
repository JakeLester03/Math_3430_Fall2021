import LA

def GramSchmidt(matrix: list) -> list:
    '''
    The stable version of Gram-Schmidt QR factorization. First we create an empty list for Q, V, and R. We want to build R as a square matrix 
    so that we can return it along with Q. Let V be a matrix  the same size as A. We can then begin by adding on each element of the matrix onto 
    V. Then let R have the same number of columns of the matrix which are equal to 0; this will allow us to build an upper triangular matrix. Next the
    p-norm of the columns of will be stored in R, and this will be done by a for loop. At the same time, we will normalize V and append to Q using 
    scalar_vector_mult. While this for loop is running, we will also run another for loop inside of it. Then we will find the dot product of Q and 
    V for the corresponding element in R. Finally, V is updated with R, and then we subtract off the product of R and Q using add vectors and scalar_vector_mult.
    
    Args:
        An Matrix which will satisfy the equation A = Q * R
    Result:
        An orthogonal matrix Q and the upper triangular matrix R both stored in a list.
    '''
    Q: list = []
    V: list = []
    R: list = []
    for element in matrix:
        V.append(element)
    for element in matrix:
        R.append([0 for element in range(len(matrix))])
    for outer_index in range(len(matrix)):
        R[outer_index][outer_index] = LA.p_norm(V[outer_index])
        Q.append(LA.scalar_vector_mult(V[outer_index], 1/R[outer_index][outer_index]))
        for inner_index in range(outer_index, len(matrix)):
            R[inner_index][outer_index] = LA.inner_product(Q[outer_index], V[inner_index])
            V[inner_index] = LA.add_vectors(V[inner_index], LA.scalar_vector_mult(Q[outer_index], -R[inner_index][outer_index]))
    return [Q, R]

def orthonormal_vectors(matrix: list) -> list:
    '''
    Takes an input list of vectors and returns the orthonormal list of vectors sharing the same span. In our Stable Gram-Schmidt
    algorithm, we return two matricies. An orthogonal Q and Upper triangular R. Likewise, Q is also foud to be orthonormal. Therefore,
    we can use the Gram-Schmidt algortihm and return the first element Q.

    Args:
        A list of vectors (i.e matrix).
    Returns:
        An orthonormal list of vectors sharing the same span.
    '''
    return GramSchmidt(matrix)[0]

def Identity(n: int)-> int:
    '''
    Builds an identity matrix of nxm size.

    Args:
        An integer n which denotes the size of the square identity matrix.
    
    Result:
        An nxm Identity matrix
    

    '''
    result:list =[[0 for element in range(n)] for index in range(n)]
    for index in range(n):
        result[index][index] = 1
    return result

def sign(n:float)-> float:
    '''
    Determines whether a number is positive or negative. If less than 0, returns -1. If greater than 0, returns 1.
    Args:
        an integer n
    Returns:
        -1 or 1.
    '''
    if n < 0:
        return -1
    else:
        return 1
    
def v_reflection(vector: list)-> list:
    '''
    Find the reflection V where V satisfies the equation V = sign(x)||x||e + x
    
    Args:
        a vector stored as a list.
    Returns:
        the reflection vector V.
    '''
    e = [0 for element in vector]
    e[0] = 1
    vnorm = LA.p_norm(vector)
    s = sign(vector[0]) * vnorm
    w =LA.scalar_vector_mult(e, s)
    V = LA.add_vectors(w, vector)
    return V

def complex_conjugate(scalar:float)-> float:
    '''
    Find the conjugate of a complex scalar by reversing the sign (+ or -) of the imaginary part. In order to negate a 0j imaginary component, implement if...else.
    If complex component, return only the scalar real value. Else, return the complex number consisting of scalar and imaginary.
    
    Args:
        A complex scalar consisting of a real part and an imaginary part.
    Result:
        The conjugated scalar with the sign reversed of the imaginary.
    '''
    def complex_conjugate(scalar:float)-> float:
    if scalar.imag == 0: return scalar
    else:
        return complex(scalar.real, - scalar.imag)

def conjugate_transpose(matrix:list[list])-> list[list]:
    '''
    Creates the conjugate transpose of a matrix. We first create two result matrix to be a copy of the input matrix of same nxm size filled
    with 0's for the appropiate range. We can implement a for loop to make the rows and columns of the first result matrix to be the equal to the input matrix. And at
    the same time, we will take the complex_conjugate of the elements, so that we can execute the complex conjugate and the transpose at the same time. The result will
    be the conjugate_transpose.
    
    Args: 
        A matrix stored as a list.
    Result:
        The conjugated transpose of the matrix    
    '''
    result_1:list = [[0 for element in range(len(matrix))] for i in range(len(matrix[0]))]
    for index_1 in range(len(matrix[0])):
        for index_2 in range(len(matrix)):
            result_1[index_1][index_2] = complex_conjugate(matrix[index_2][index_1])
    return result_1

def vector_vector_mult(vector:list, vector_b:list)-> list:
    '''
    Used in the process of calculating F_k = I - 2(vv*/v*v), where vectors (vv*/v*v)*2 will be calculated.
    Initialize result as an empy list. For elements in the first vector, use scalar_vector_mult to multiply the scalars of the vector by the 
    second vector.

    Args: 
        Two vectors.
    Returns:
        The product of the two vectors.   
    '''
    result: list = []
    for index in range(len(vector)):
        result.append(LA.scalar_vector_mult(vector_b, vector[index]))
    return result

def F_builder(vector:list)-> list:
    '''
    Returns F_k found by the equation F_k = I - 2(vv*/v*v). We can set an arbirtary scalar, x, equal to 2 divided by the norm of v squared. Then
    multiply the vectors, using vector_vector_mult and multiply by -x using scalar_vector_mult and set equal to y so y will now be negative. Finally, 
    using matrix_add, subtract y (add minus y) from the identity matrix by using matrix_add.
    Args:
        a vector stored as a list of lists
    Returns:
        the F_k value needed for Q_k.
    '''
    x = 2/(LA.boolean_norm(vector))**2
    y = LA.scalar_matrix_mult(vector_vector_mult(vector, vector), -x) 
    z = LA.matrix_add(Identity(len(vector)), y)
    return z

def deep_copy(matrix: list[list]) -> list[list]:
    '''
    Instead of creating a shallow copy as a reference point for our copies of the inputs, we can create a deep copy for our referenced
    lists. 
    First initialize a result matrix of the input matrix of same nxn size. Result matrix will be filled with 0's.
    Then, the the rows and colums will weill become a copy of the desired matrix to be copied.
    
    Args:
        a matrix stored as a list of lists.
    
    Returns:
        The deep copy of the matrix.
    '''
    result = [[0 for element in range(len(matrix[0]))] for i in range(len(matrix))]
    for index_1 in range(len(matrix)):
        for index_2 in range(len(matrix)):
            result[index_1][index_2] = matrix[index_1][index_2]
    return result

def Q_builder(matrix: list[list], k: float)-> list[list]:
    '''
    Used to solve Q_k such that Q_k = [[I_k-1, 0], [0, F_k]]. 
    First initialize result of the input matrix to be filled with zero's. Q will need to take the form Q = [[I_k-1, 0], [0, F_k]], so we run a for loop
    to initialize the innput matrix to be of the same dimensions of the matrix [[I_k-1, 0], [0, F_k]]. F_k is written, so we can set an element f equal to F_k using 
    F_builder. Using Identity, set Q_k as Q_builder equal to the identity matrix. We will then need to add in our F_k value f into the Q matrix using for loops to put it in the appropiate
    a_22 posistion. Return Q_k (or Q_builder).

    Args:
        a matrix stored as a list of lists.
        an integer k representing the indexing iterations
    Returns:
        Q_k of the form [[I_k-1, 0], [0, F_k]]
    '''
    Q: list = [[0 for element in range(k, len(matrix[index]))] for index in range(k, len(matrix))]
    for index in range(len(matrix)):
        for element in range(len(matrix[index])):
            if k + index < len(matrix[index]):
                if k + element < len(matrix[index]):
                    Q[index][element] = matrix[k + index][k + element]
    v = v_reflection(Q[0])
    f = F_builder(v)
    Q_builder = Identity(len(matrix))
    for index in range(k, len(Q_builder)):
        for element in range(k, len(Q_builder)):
            Q_builder[index][element] = f[index - k][element - k]
    return Q_builder

def Householder(matrix: list[list]) -> list[list]:
    '''
    Perfroms the householder decomposistion on a matrix. Initialize R to be the deep copy of the input matrix. An empty Q_list. We will then denote another variable, Q_temp,
    to be equal to the Q_k of R and the indecies interating in the for loop. R will then be equal to the multiplication of Q_temp * R. Use matrix_matrix_mult to calculate R in
    QR decomposistion. Now append the values of Q_temp to our empty Q_list, which we set to our final Q. We will start with the last indecy for finish Q. We then take the conjugate 
    transpose of Q_list beginning with the first vector. We finish building Q by taking the multiplications of Q and the conjugate_transpose. Return Q and R
    Args:
        a matrix stored as a list of lists.
    Returns:
        an orthogonal matrix Q and the upper triangular matrix R via the Householder decomposistion method.
    '''
    def Householder(matrix: list[list]) -> list:
    
    R: list = deep_copy(matrix)
    Q_list: list = []
    for index in range(len(R)):
        Q_temp: list = Q_builder(R, index)
        R = LA.matrix_matrix_mult(Q_temp, R)
        Q_list.append(Q_temp)
    Q: list = Q_list[-1]
    Q: list = conjugate_transpose(Q_list[0])
    for index in range(1, len(Q_list)):
        Q = LA.matrix_matrix_mult(Q, conjugate_transpose(Q_list[index]))
    return [Q, R]
  
  



