import LA

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


