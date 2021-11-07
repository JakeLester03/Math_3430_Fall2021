import LA
import QR
import pytest

def test_GramSchmidt():
    matrix_c = [[1,1,1,1],[3,2,3,2],[6,2,8,4]]
    matrix_d = [[0,-1,-1],[1,1,1],[2,1,3]]
    assert QR.GramSchmidt(matrix_c) == ([[[0.5, 0.5, 0.5, 0.5], [0.5, -0.5, 0.5, -0.5], [-0.5, -0.5, 0.5, 0.5]], [[2.0, 0, 0], [5.0, 1.0, 0], [10.0, 4.0, 2.0]]])
    assert QR.GramSchmidt(matrix_d) == ([[[0.0, -0.7071067811865475, -0.7071067811865475], [1.0, 2.220446049250313e-16, 2.220446049250313e-16], [0.0, -0.7071067811865475, 0.7071067811865475]],
 [[1.414213562373095, 0, 0], [-1.414213562373095, 1.0, 0], [-2.82842712474619, 2.0, 1.414213562373095]]])
    
def test_orthonormal_vectors():
  matrix_c = [[1,1,1,1],[3,2,3,2],[6,2,8,4]]
  matrix_e = [[0,-1], [1,2]]
  assert QR.orthonormal_vectors(matrix_c) == ([[0.5, 0.5, 0.5, 0.5], [0.5, -0.5, 0.5, -0.5], [-0.5, -0.5, 0.5, 0.5]])
  assert QR.orthonormal_vectors(matrix_e) ==([[0.0, -1.0], [1.0, 0.0]])
