'''ex
def stable_QR(Matrix_A[j]):
    Q: list =[]
    V: list =[]
    R: list =[]
    for element in A:
        V.append(element)
    for index in range(something):
    R[index][index] = La.norm(V[index])
    Q.append(La.scalar_vec_mult(1/R[index][index], V[index]))
        for innder_index in range(something):
        R[index][inner_index] = La.inner_product(Q[index, V[inner_index]])
        Q[index] =La.add_vectors(V[index], La.scalar_vector_mult(-R[inner_index][index], Q[index]))
return [Q,R]
'''

import LA

def GramSchmidt_stable(matrix: list) -> complex:
    '''
    The stable version of Gram-Schmidt QR factorization.


Args:

Result:
    
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
    return [Q,R]
matrix = [[1, 0], [-5, -5]]
print(GramSchmidt_stable(matrix))



def GramSchmidt_unstable(matrix: list):
    '''
    The unstable version of Gram-schmidt factorization.

Args:

Results:
    
    
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

#matrix = [[-1,10,1],[2,2,10],[3,-4,3]]
#matrix =[[1,2,3],[4,2,-4],[12,0,0]]
#print(GramSchmidt_unstable(matrix))

