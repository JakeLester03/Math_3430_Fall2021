import LA
import pytest

#0 add vectors
def test_add_vectors():
    vector_a = [1,1]
    vector_b = [1,2]
    vector_c = [0,1]
    vector_d = [1,0] 
## vector_a + vector_b: [1+1, 1+2] = [2,3]
## vector_c + vector_d: [0+1, 1+0] = [1,1]
    assert LA.add_vectors(vector_a, vector_b) == [2,3]
    assert LA.add_vectors(vector_c, vector_d) == [1,1]

#1 Scalar-Vector Multiplication
def test_scalar_vector_mult():
    vector_e = [1,2,3]
    scalar_a = 3
    vector_f = [2,4,6]
    scalar_b = 2
## vector_e * scalar_a: [3*1, 3*2, 3*3] = [3,6,9]
## vector_f * scalar_b: [2*2, 2*4, 2*6] = [4,8,12]
    assert LA.scalar_vector_mult(vector_e, scalar_a) == [3,6,9]
    assert LA.scalar_vector_mult(vector_f, scalar_b) == [4,8,12]

#2 Scalar-Matrix Multiplication
def test_scalar_matrix_mult():
    matrix_a = [[2, 4], [6, 8]]
    scalar_c = 2
    matrix_b = [[1,2,3],[3,4,5],[5,6,7]]
    scalar_d = 3
## matrix_a * scalar_c: [[2*2, 2*4], [2*6, 2*8]] = [[4, 8],[12, 16]]
## matrix_b * scalar_d: [[3*1,3*2,3*3], [3*3,3*4,3*5],[3*5,3*6,3*7]] = [[3,6,9], [9,12,15],[15,18,21]]
    assert LA.scalar_matrix_mult(matrix_a, scalar_c) == [[4, 8], [12, 16]]
    assert LA.scalar_matrix_mult(matrix_b, scalar_d) == [[3,6,9], [9,12,15],[15,18,21]]

#3 MAtrix Addition
def test_matrix_add():
    matrix_c = [[1,2,3], [4,5,6], [7, 8, 9]]
    matrix_d = [[1,2,3], [4,5,6], [7, 8, 9]]
    matrix_e = [[3,2,1], [6,5,4], [9,8,7]]
    matrix_f = [[1,1,1], [2,2,2], [3,3,3]]
## matrix_c + matrix_d: [[1+1,2+2,3+3]],[4+4,5+5,6+6],[7+7,8+8,9+9]= [[2,4,6], [8,10,12], [14,16,18]]
## matrix_e + matrix_f: (repeat same method of addition) = [[4,3,2], [8,7,6], [12,11,10]]
    assert LA.matrix_add(matrix_c, matrix_d) == [[2,4,6], [8,10,12], [14,16,18]]
    assert LA.matrix_add(matrix_e, matrix_f) == [[4,3,2], [8,7,6], [12,11,10]]

#4 Matrix-Vector Multiplication
def test_matrix_vector_mult():
    matrix_α = [[1, 1], [1, 1]]
    vector_α = [100, 100]
    matrix_β = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    vector_β = [4, 8, 12, 16]
## matrix_α * vector_α: [[1*100, 1*100] +[1*100, 1*100] = [200,200]
## matrix_β * vector_β: [[1*4, 2*4, 3*4, 4*4]+[5*8, 6*8, 7*8, 8*8,]+[9*12,10*12,11*12,12*12]+[13*16,14*16,15*16,16*16]] = [360,400,440,480]
    assert LA.matrix_vector_mult(matrix_α, vector_α) == [200,200]
    assert LA.matrix_vector_mult(matrix_β, vector_β) == [360, 400, 440, 480]

#5 Matrix-MAtrix multiplication
def test_matrix_matrix_mult():
    matrix_Δ = [[1,1,1],[1,1,2],[1,2,3]]
    matrix_θ = [[100,100,100], [100,100,100], [100,100,100]]
    matrix_ζ = [[1,2],[2,1]]
    matrix_Ω = [[10, 20], [30, 40]]
## matrix_Δ * matrix_θ:[[1*100+1*100+1*100, 1*100+1*100+1*200, 1*100+2*100+3*100], [...], [...]] = [[300,400,600], [300,400,600], [300,400,600]]
## matrix_ζ * matrix_Ω: [[1*10],[2*10] + [2*20, 1*20]. [1*30,2*30]+[2*40, 1*40]] = [[50,40], [110, 100]]
    assert LA.matrix_matrix_mult(matrix_Δ, matrix_θ) == [[300,400,600], [300,400,600], [300,400,600]]
    assert LA.matrix_matrix_mult(matrix_ζ, matrix_Ω) == [[50,40], [110, 100]]
