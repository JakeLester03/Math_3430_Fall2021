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
    #result = [vector[-1]*(1/(matrix[-1][-1]))]
    #for current in range(len(mat)-1,-1,-1)
    for index_1 in range(length-1,-1,-1):
        temp = vector[index_1]
        for index_2 in range(len(result)):
            temp -= matrix[len(matrix)-1-index_2][index_1]*result[index_2]
        temp *= 1/(matrix[index_1][index_1])
        result.append(temp)
    return result[::-1]



'''matrix_u = [[1, 0, 0], [2, 1, 0], [3, 2, 1]]
vector_b = [6, 3, 1]
print(back_substitution(matrix_u, vector_b))
'''

#Pseudo-Code
# matrix a stored as a list
# vector stored as a list
#Least square:
#Compute grahm schmidt on matrix_a to get Q and R
# For Q: compute conjugate transpose
    #multiply conjugate transpose of Q by vector
    #Denote solution as Q_new (vector)
#Implement back_sub(R, Q_new)
#Return result


def least_squares(matrix, vector):
    Q,R = QR.GramSchmidt(matrix)
    Q_new = QR.conjugate_transpose(Q)
    Q_newagain = LA.matrix_vector_mult(Q_new, vector)
    #result = back_substitution(R, Q_newagain)
    return back_substitution(R, Q_newagain)

'''matrix_a = [[4,0,0],[5,1,0],[6,2,3]]
vector_a = [3,3,6]
matrix_b = [[1,0,0],[0,1,0],[2,2,1]]
vector_b = [3,4,5]
print(least_squares(matrix_b, vector_b))
'''

def division(a, b):
    result1 = a // b
    result2 = a / b
    return result1 and result2

a = 4
b = 3

print(division(a,b))

    
