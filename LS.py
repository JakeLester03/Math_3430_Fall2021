import LA
import QR

def back_substitution(matrix, vector):
    '''
    Performs back substitution in order to solve a linear system of equations.

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


def least_squares(matrix, vector):
    Q,R = QR.GramSchmidt(matrix)
    Q_new = QR.conjugate_transpose(Q)
    Q_newagain = LA.matrix_vector_mult(Q_new, vector)
    return back_substitution(R, Q_newagain)


    
