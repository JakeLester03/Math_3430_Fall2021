import LA
import QR

def back_substitution(matrix, vector):
    '''
    Performs back substitution in order to solve a linear system of equations of the from Ax=B.

Args:
    a matrix (A) stored as a list of lists and a vector(B) stored as a list.

Result:
    vector x which satisfies Ax=B.

    '''
    
    result = [vector[-1]*(1/(matrix[-1][-1]))]
    for current in range(len(matrix)-2,-1,-1):
        temp = vector[current]
        for index in range(len(result)):
            temp -= matrix[len(matrix)-1-index][current]*result[index]
        temp *= 1/(matrix[current][current])
        result.append(temp)
    return result[::-1]
