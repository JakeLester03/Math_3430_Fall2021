import LA
import QR

def back_substitution(matrix:list[list], vector:list)->list:
    '''
    Performs back substitution in order to solve a linear system of equations satisfying Ax=B.

    Args:
        a matrix stored as a list or lists and a vector stored as a list.

    Result:
        vector b which satisfies Ax=B.

    '''
    length = len(matrix)-1
    result: list = [vector[-1]*(1/(matrix[-1][-1]))]
    for index_1 in range(length-1,-1,-1):
        temp = vector[index_1]
        for index_2 in range(len(result)):
            temp -= matrix[len(matrix)-1-index_2][index_1]*result[index_2]
        temp *= 1/(matrix[index_1][index_1])
        result.append(temp)
    return result[::-1]


def least_squares(matrix: list[list], vector: list)-> list:
    '''
    Solves a system of equations following the form A*Ax = A*B (* is the transpose). It first takes a matrix and return Q and R
    via Gram-Schmidt decomposistion. The transpose is then taken on Q, which can be denoted by Q_new. Q_new will then be multiplied
    by the input vector using matrix_vector_mult, and the result can be denoted by Q_newagain (Q has now been transformed two times). Finally,
    we can perform back substitution on Q_newagain and R to get the solution vector x.

    Args:
        a matrix stored as a list of lists and a vector.
    
    Results:
        the least squares soltion.
    '''
    QR_decomp:list = QR.Householder(matrix)
    Q:list = QR_decomp[0]
    R:list = QR_decomp[1]
    Q_new:list = QR.conjugate_transpose(Q)
    Q_newagain:list = LA.matrix_vector_mult(Q_new, vector)
    x:list = back_substitution(R, Q_newagain)
    return x
