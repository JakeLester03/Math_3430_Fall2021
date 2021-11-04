import LA

def GramSchmidt_unstable(matrix: list) -> list:
    '''
    The unstable version of Gram-schmidt factorization. First we create an empty list for Q, V, and R. We want to build R as a square matrix 
    so that we can return it along with Q. Let R be initialized as a matrix of 0's. Let V be a matrix  the same size as A and essentially a copy. 
    We will start a for loop to indexing over the matrix, then append that onto V. Then we will star another for loop to iterate over the columns 
    so that R can be overwritten; this will allow us to build an upper triangular matrix. Then we can multiply the rows of Q and columns of V using 
    inner_produt to over write R. V is overwritten with R, and then we subtract off the product of R and Q using add vectors and scalar_vector_mult. 
    We will then take the p-norm of the columns to be stored in R. Finally, we will normalize V and multiply by R using scalar_vector_mult; we append 
    this to Q to get the orthogonal matrix. 

Args:
    A Matrix which will satisfy A = Q * R

Results:
    An orthogonal matrix Q and the upper triangular matrix R both stored in a list.
    
    
    '''
    Q: list = []
    V: list = []
    R: list = []
    for element in matrix:
        R.append([0 for element in range(len(matrix))])
    for outer_index in range(len(matrix)):
        V.append(matrix[outer_index])
        for inner_index in range(0, outer_index):
            R[outer_index][inner_index] = LA.inner_product(Q[inner_index], V[outer_index])
            V[outer_index] = LA.add_vectors(V[outer_index], LA.scalar_vector_mult(-R[outer_index][inner_index], Q[inner_index]))
        R[outer_index][outer_index] = LA.p_norm(V[outer_index])
        Q.append(LA.scalar_vector_mult(1/R[outer_index][outer_index], V[outer_index]))
    return [Q, R]

def GramSchmidt_stable(matrix: list) -> list:
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
        Q.append(LA.scalar_vector_mult(1/R[outer_index][outer_index], V[outer_index]))
        for inner_index in range(outer_index, len(matrix)):
            R[inner_index][outer_index] = LA.inner_product(Q[outer_index], V[inner_index])
            V[inner_index] = LA.add_vectors(V[inner_index], LA.scalar_vector_mult(-R[inner_index][outer_index], Q[outer_index]))
    return [Q, R]


