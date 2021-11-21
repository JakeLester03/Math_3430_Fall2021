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

#matrix = [[-1, 1], [3, 4]]
#matrix_02 = [[1,1,1,1],[3,2,3,2],[6,2,8,4]]
#print(GramSchmidt(matrix_02))


#NOT USING
'''
def GramSchmidt_unstable(matrix: list) -> list:

    The unstable version of Gram-schmidt factorization. First we create an empty list for Q, V, and R. We want to build R as a square matrix 
    so that we can return it along with Q. Let V be a matrix  the same size as A and essentially a copy. We will start a for loop to indexing 
    over the matrix, then append that onto V. Then we will star another for loop to iterate over the columns so that R can be overwritten; this
     will allow us to build an upper triangular matrix. Then we can multiply the rows of Q and columns of V using inner_produt to over write R.
     V is overwritten with R, and then we subtract off the product of R and Q using add vectors and scalar_vector_mult. We will then take the p-norm
     of the columns to be stored in R. Finally, we will normalize V and multiply by R using scalar_vector_mult; we append this to Q to get the 
     orthogonal matrix. 

Args:
    An Matrix which will satisfy the equation A = Q * R

Result:
    An orthogonal matrix Q and the upper triangular matrix R both stored in a list.
    

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
            #V[outer_index] = LA.add_vectors(V[outer_index], LA.scalar_vector_mult( Q[inner_index, -R[outer_index][inner_index],]))
        R[outer_index][outer_index] = LA.p_norm(V[outer_index])
        Q.append(LA.scalar_vector_mult(1/R[outer_index][outer_index], V[outer_index]))
       
    return [Q, R]
'''

#matrix = [[-1,10,1],[2,2,10],[3,-4,3]]
#matrix =[[1,2,3],[4,2,-4],[12,0,0]]
#print(GramSchmidt_unstable(matrix))

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
    

matrix_a = [[0, -1], [1, 2]]
matrix_b = [[1,1,1,1],[3,2,3,2],[6,2,8,4]]
#print(orthonormal_vectors(matrix_a))

def Identity_Matrix_converter(matrix):
    result: list[list] = [([0] *(len(matrix))) for element in range(len(matrix[0]))]
    print(matrix)
    for index in range(len(matrix)):
        result[index][index] = 1
    return result

def Identity(n: int)-> int: 
    '''
    Builds an identity matrix of nxn size.

    Args:
        An integer n which denotes the size of the square identity matrix.
    
    Result:
        An nxn Identity matrix
    

    '''
    result:list =[[0 for element in range(n)] for index in range(n)]
    for index in range(n):
        result[index][index] = 1
    return result

print(Identity(3))

def sign(n:float)-> float:
    if n < 0:
        return -1
    else:
        return 1

def complex_conjugate(scalar:float)-> float:
    if scalar.imag == 0: return scalar
    else:
        return complex(scalar.real, - scalar.imag)
    
#scalar=2-1j
#print(complex_conjugate(scalar))


def conjugate_transpose(matrix:list)-> list:
    result_1:list = [[0 for element in range(len(matrix[0]))] for i in range(len(matrix))]
    result_2:list = [[0 for element in range(len(matrix[0]))] for i in range(len(matrix))]
    for index_1 in range(len(matrix[0])):
        for index_2 in range(len(matrix[0])):
            result_1[index_1][index_2] = complex_conjugate(matrix[index_1][index_2])
    for index_3 in range(len(matrix[0])):
        for index_4 in range(len(matrix)):
            result_2[index_3][index_4] = result_1[index_4][index_3]
    return result_2

'''def conjugate_transpose(matrix_a):
    result: list = [[0 for element in range(len(matrix_a[0]))] for index in range(len(matrix_a))]
    ct: list = [[0 for element in range(len(matrix_a[0]))] for index in range(len(matrix_a))]
    for x in range(len(matrix_a[0])):
        for y in range(len(matrix_a[0])):
            result[x][y] = matrix_a[x][y].conjugate()
    for index in range(len(matrix_a[0])):
        for element in range(len(matrix_a)):
            ct[index][element] = result[element][index]
    return ct'''

matrix_a = [[1,3], [2,5]]
print('conjugate_transpose:')
print(conjugate_transpose(matrix_a))


def v_reflection(vector: list)-> list:
    e = [0 for element in vector]
    e[0] = 1
    print('e:'+ str(e))
    vnorm = LA.p_norm(vector)
    s = sign(vector[0]) * vnorm
    w =LA.scalar_vector_mult(e, s)
    V = LA.add_vectors(w, vector)
    return V

vector_a= [2,2,1]
print('v_reflection:')
print(v_reflection(vector_a))

def vector_vector_mult(vector:list, vector_b:list)-> list:
    result: list = []
    for index in range(len(vector)):
        result.append(LA.scalar_vector_mult(vector_b, vector[index]))
    return result

#vector_a = [1,2,3]
#vector_b = [2,2,2]
#print(vector_vector_mult(vector_a, vector_b))



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

    print('vector in F_builder:'+ str(vector))
    x = 2/LA.p_norm(vector)**2
    y = LA.scalar_matrix_mult(vector_vector_mult(vector, vector), -x) 
    z = LA.matrix_add(Identity(len(vector)), y)
    return z


vector_a = [5,2,1]
res = LA.p_norm(vector_a)
print(res)
print('F_builder:')
print(F_builder(vector_a))


def deep_copy(matrix: list[list]) -> list[list]:
    result = [[0 for element in range(len(matrix_a[0]))] for i in range(len(matrix))]
    for index_1 in range(len(matrix[0])):
        for index_2 in range(len(matrix)):
            result[index_1][index_2] = matrix[index_1][index_2]
    return result
print('deep_copy:')
print(deep_copy(matrix_a))

def Q_builder(matrix: list[list], k)-> list:
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
    

matrix_a = [[2,2,1],[-2,1,2],[18,0,0]]
matrix_b = [[1,1,1], [-1,4,4], [4,-2,0]]
matrix_c = [[1,2,3],[-3,5,9],[1,-2,0]]
matrix_d = [[0,-1], [1,2]]
print('GS:')
print(Householder(matrix_a))







