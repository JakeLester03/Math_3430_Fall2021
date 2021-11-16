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
##
def Identity(n: int)-> int:
    '''
    Builds an identity matrix of nxn size.

    Args:
        An integer n which denotes the size of the square identity matrix.
    
    Result:
        An nxn Identity matrix
    

    '''
    result:list =[[0 for element in range(n)] for index in range(n)]
    for i in range(n):
        result[i][i] = 1
    return result

print(Identity(1))

def sign(n:float)-> float:
    if n < 0:
        return -1
    else:
        return 1

def complex_conjugate(scalar:float)-> float:
    result = scalar.real + -scalar.imag*1j
    return result
scalar=2
#print(complex_conjugate(scalar))




'''
def Q_builder

#Doc String
 


def F_builder(vector:list)-> list:
    '''
    Return F_k
    '''
    
    x = 2/(LA.boolean_norm(vector))**2
    y = LA.scalar_vector_mult(#vector_vectormult(vect1, vec2), x)
    z = LA.matrix_add(Identity(len(vector)), y)
    return z



def Householder(matrix: list[list]) -> list[list]:
    #doc strng
    R: list = deep_copy(A)
    Q_list: list = []
for index in range(len(R)):
    Q_temp: list= Q_builder(R, index)
    A = La.matrix_mult(Q_temp, R)
    Q_list.append(Q_temp)
Q: list = conjugate_transpose(Q_list[0])
for index in range(len(1, len(Q_list))
    Q = La.mat_mult(Q, conjugate_transpose(Q_list[index])
return [Q, R]

write Q builder
write conjugate transpose
write deep copy
'''


