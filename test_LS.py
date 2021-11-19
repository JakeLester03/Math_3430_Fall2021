import LA
import QR
import LS

def test_back_substitution():
    matrix_a = [[4,0,0],[5,1,0],[6,2,3]]
    vector_a = vector_a = [3,3,6]
    matrix_b = [[1,0,0],[0,1,0],[2,2,1]]
    vector_b = [3,4,5]
    assert LS.least_squares(matrix_a, vector_a) == [-1.0, -1.0, 2.0]
    assert LS.least_squares(matrix_b, vector_b) == [-7.0, -6.0, 5.0]