import LA
import QR
import LS

def test_back_substitution():
    matrix_s = [[1, 0, 0], [0, 1, 0], [2, 2, 1]]
    matrixζ = [[1, 2, 3], [2, 1, 0], [1, 1, 2]]
    vector_s = [3, 2, 1]
    vectorζ = [2, 2, 1]
    assert LS.back_substitution(matrix_s, vector_s) == [1.0, 0.0, 1.0]
    assert LS.back_substitution(matrixζ, vectorζ) == [-1.5, 1.5, 0.5]

def test_least_squares():
    matrix_a = [[4,0,0],[5,1,0],[6,2,3]]
    vector_a = vector_a = [3,3,6]
    matrix_u = [[1,1,1],[3,2,3], [6,2,8]]
    vector_u = [3,3,1]
    assert LS.least_squares(matrix_a, vector_a) == [-1.0, -1.0, 2.0]
    assert LS.least_squares(matrix_u, vector_u) == [-2.999999999999919, 3.999999999999955, -0.9999999999999928]
