import LA
import QR
import LS

print('Hello World, my name is Jake! I am the author of this script.')
print(' ')

print('''This file demonstrates the functionality of various linear algebraic techniques, which can be found in LA.py, 
QR.py, and LS.py. We will start with demonstrating the functionality of LA.py, which includes elementary 
linear algebraic operations: ''')
print(' ')

print('''THE FIRST FUNCTION IN LA.PY IS ADD_VECTORS. IT WILL TAKE IN TWO VECTORS
AS ITS ARGUMENTS AND RETURN THEIR SUM: ''')
print('''For example, if a = [1,1] and b =[1,2], then add_vectors will return: ''')
a= [1,1]
b = [1,2]
print(LA.add_vectors(a,b))
print(' ')

print('''THE SECOND FUNCTION IN LA.PY IS SCALAR_VECTOR_MULT. IT WILL TAKE A SCALAR AND A VECTOR AS ITS
INPUTS AND RETURNS THEIR PRODUCT: ''')
print('''For example, if a scalar n = 2 and vector_a = [1,1], then scalar_vector_muult will return: ''' )
scalar = 2
vector_a = [1,1]
print(LA.scalar_vector_mult(vector_a, scalar))
print(' ')

print('''THE THIRD FUNCTION IN LA.PY SCALAR_MATRIX_MULT. IT TAKES A SCALAR AND A MATRIX AS ITS INPUTS AND RETURNS
THEIR PRODUCT: ''')
print('''For example, if a scalar = 2 and a matrix = [[2,4],[6,8]], then scalar_matrix_mult will return: ''')
matrix_a = [[2,4],[6,8]]
scalar = 2
print(LA.scalar_matrix_mult(matrix_a, scalar))
print(' ')

print('''THE FOURTH FUNCTION IN LA.PY IS MATRIX_ADD, WHICH TAKES TWO MATRICIES AS ITS INPUT AND RETURNS THEIR SUM: ''')
print('''For example, if a matrix_a = [[1,2,3], [4,5,6], [7, 8, 9]] and matrix_b represents the second matrix to be added, then
the result will be: ''')
matrix_a = [[1,2,3], [4,5,6], [7, 8, 9]]
print(LA.matrix_add(matrix_a, matrix_a))
print(' ')

print('''THE FIFTH FUNCTION IN LA.PY IS MATRIX_VECTOR_MULT. IT WILL TAKE A MATRIX AND A VECTOR AND RETURN THEIR PRODUCT: ''')
print('''For example, if matrix_α = [[1, 1], [1, 1]] and vector_α = [100, 100], the the result will be: ''')
matrix_α = [[1, 1], [1, 1]]
vector_α = [100, 100]
print(LA.matrix_vector_mult(matrix_α, vector_α))
print(' ')

print('''THE SIXTH FUNCTION IN LA.PY IS MATRIX_MATRIX_MULT. THIS FUNCTION WILL TAKE THE PRODUCT OF TWO MATRICIES: ''')
print('''For example, if a matrix_Δ = [[1,1,1],[1,1,2],[1,2,3]] and matrix_θ = [[100,100,100], [100,100,100], [100,100,100]],
then the result will be: ''' )
matrix_Δ = [[1,1,1],[1,1,2],[1,2,3]]
matrix_θ = [[100,100,100], [100,100,100], [100,100,100]]
print(LA.matrix_matrix_mult(matrix_Δ, matrix_θ))
print(' ')

print('''THE SEVENTH FUNCTION IN LA.PY IS ABSOLUTE_VALUE, AND IT WILL RETURN THE ABSOLUTE VALUE OF A NUMBER. THIS WORKS
FOR BOTH REAL AND COMPLEX NUMBERS. ''')
print('''For example, if a number n = -1, the result will be: ''')
scalar = -1
complex_a = 3-4j
print(LA.absolute_value(scalar))
print('''also, if wanting the absolute value complex number of 3-4j, then the result will be: ''')
print(LA.absolute_value(complex_a))
print(' ')

print('''THE EIGHTH FUNCTION IN LA.PY IS P_NORM. THIS FUNCTION WILL FIND THE P NORM OF A VECTOR, AND IT DEFAULTS TO 2 IF 
NOT SPECIFIED. THIS FUNCTION WORKS FOR BOTH COMPLEX AND REAL NUMBERS: ''')
print('''For example, if a vector_a = [1,2,3], then the result will be: ''')
vector_1 = [1,2,3]
print(LA.p_norm(vector_1))
print(' ')

print('''THE NINTH FUNCTION IN LA.PY IS INFINITY_NORM. THIS FUNCTION RETURN THE INFINITY NORM OF A VECTOR. ''')
print('''For examply, if a vector = [1,2,3], then the infinity norm will be: ''')
vector_3 = [1,2,3]
print(LA.infinity_norm(vector_3))
print(' ')

print('''THE TENTH FUNCTION IN LA.PY IS BOOLEAN_NORM. THIS FUNCTION IS BASED ON A BOOLEAN STATEMENT. IF A VECTOR = [1,2,3],
AND IF THE BOOLEAN IS FALSE, THEN IT WILL RETURN the P norm, as we saw in the p_norm function: ''')
vector_5 = [1,2,3]
print(LA.boolean_norm(vector_5, 2, False))
print('''However, if the Boolean is True, the it will return the infinity norm, as we saw demonstrated with infinity_norm: ''')
print(LA.boolean_norm(vector_5, 2, True))
print(' ')

print('''THE ELEVENTH AND FINAL FUNTION OF LA.PY IS INNER_PRODUCT. THIS FUNCTION WILL TAKE THE DOT PRODUCT (OR INNER
PRODUCT) OF TWO VECTORS. ''')
print('''For example, if a vector = [1,2,3] and another vector = [1,2,5], then the result will be: ''')
vector_p =[1,2,3]
vector_pp = [1,2,5]
print(LA.inner_product(vector_p, vector_pp))
print('''Note that this function also works for complex numbers.''')
print(' ')

print('''THIS CONCLUDES THE DEMOSTRATION OF THE 11 FUNCTIONS IN LA.PY. NOW WE WILL DEMONSTRATE THE FUNCTIONALITY OF THE FUNCITONS
IN QR.PY, WHICH INCLUDES VARIOUS TECHNIQUES FOR QR FACOTORIZATION: ''')

print('''THE FIRST FUNCTION IN QR.PY IS GRAM_SCHMIDT. THIS FUNCTION WILL DO A QR FACTORIZATION VIA THE GRAM-SCHMIDT METHOD.
Q and R will both be stored in a list [Q, R] ''')
print('''For example, if a matrix = [[1,1,1,1],[3,2,3,2],[6,2,8,4]], then the result will be: ''')
matrix = [[1,1,1,1],[3,2,3,2],[6,2,8,4]]
print(QR.GramSchmidt(matrix))
print(' ')

print('''THE SECOND FUNCTION IN QR.PY IS ORTHORNORMAL_VECTORS. THIS FUNTION WILL TAKE AS ITS INPUT A LIST OF VECTORS (A MATRIX) AND
RETURN THE ORTHONORMAL LIST OF VECTORS SHARING THE SAME SPAN. ''')
print('''For example, if a matrix = [[1,1,1,1],[3,2,3,2],[6,2,8,4]], then the orthonormal list of vectors will be: ''' )
matrix = [[1,1,1,1],[3,2,3,2],[6,2,8,4]]
print(QR.orthonormal_vectors(matrix))
print(' ')

print('''*NOTE: THE FOLLOWING FUNCTIONS WILL ALL BE USED IN ORDER TO IMPLEMENT HOUSEHOLDER DECOMPOSISTION. HOWEVER, THEY 
CAN STILL BE INDEPENDENT OF HOUSEHOLDER DECOMPOSISTION*''')
print(' ')

print('''THE THIRD FUNCTION IN QR.PY IS IDENTITY. THIS FUNCTION WILL BUILD AN IDENTITY MATRIX OF SPECIFIED NXM SIZE. ''')
print('''For example, if the input size of the desired identity matrix is 3, then the result will be: ''')
matrix_size_a = 3
print(QR.Identity(matrix_size_a))
print(' ')

print('''THE FOURTH FUNCTION IN QR.PY IS SIGN. THIS FUNCTION WILL RETURN A 1 IF THE NUMBER IS GREATER THAN 0, OR A -1
IF LESS THAN 0. ''')
print('''For example, if 2 is the input, then the result will be: ''')
s = 2
print(QR.sign(s))
print(' ')

print('''THE FIFTH FUNCTION IN QR.PY IS COMPLEX_CONJUGATE. THIS FUNCTION WILL FIND THE CONJUGATE OF A COMPLEX SCALAR. ''')
print('''For example, if a scalar = 2 + 1j, then the result will be: ''')
scalar_c = 2+ 1j
print(QR.complex_conjugate(scalar_c))

print('''THE SIXTH FUNCTION OF QR.PY IS CONJUGATE TRANSPOSE. THIS FUNCTION WILL FIND THE CONJUGATE TRANSPOSE OF A 
MATRIX. ''')
print('''For example, for a matrix = [[1,2], [3,4]], the conjugate transpose is: ''')
matrix_ct = [[1,2], [3,4]]
print(QR.conjugate_transpose(matrix_ct))
print(' ')

print('''THE SEVENTH FUNCTION OF QR.PY IS V_REFLECTION. THIS FUNCTION WILL BUILD A REFLECTION VECTOR IN ORDER TO SATISFY THE EQUATION
V = sign(x)||x||e + x, WHERE V WILL BE USED LATER FOR HOUSEHOLDER DECOMPOSISTION. ''' )
print('''For example, given the vector =  [1,0,0], the reflection will be: ''')
vector_v =  [1,0,0]
print(QR.v_reflection(vector_v))
print(' ')

print('''THE EIGHTH FUNCTION OF QR.PY IS VECTOR_VECTOR_MULT. THIS FUNCTION WILL COMPUTE THE MULTIPLICATION (OUTER PRODUCT)
OF TWO VECTORS. ''')
print('''For example, if a vector = [1,2,3] and another vector = [2,2,2], then the result will be: ''')
vector_m = [1,2,3]
vector_μ = [2,2,2]
print(QR.vector_vector_mult(vector_m, vector_μ))
print(' ') 

print('''THE NINTH FUNCTION IN QR.PY IS F_BUILDER. THIS FUNCTION WILL BUILD F_k IN ORDER TO SATISFY THE EQUATION 
F_k = I - 2(vv*/v*v). ''')
print('''For example, if we have a vector = [10,4,2], then F_k will be: ''')
vector_fb = [10,4,2]
print(QR.F_builder(vector_fb))
print(' ')

print('''THE TENTH FUNCTION IN QR.PY IS DEEP_COPY. THIS FUNCTION WILL CREATE A COPY OF THE MATRIX.''')
print('''For example, if a matrix = [[1,1,1],[2,2,2], [3,3,3]], the copy will be: ''')
matrix_c = [[1,1,1],[2,2,2], [3,3,3]]
print(QR.deep_copy(matrix_c))
print(' ') 

print('''THE ELEVENTH FUNCTION IN QR.PY IS Q_BUILDER. THIS FUNCTION WILL BUILD Q_K SUCH THAT 
Q_k = [[I_k-1, 0], [0, F_k]]. ''')
print('''For example, given an input matrix = [[1,1,1], [-1,4,4], [4,-2,0]], the result will be: ''')
matrix_k = [[1,1,1], [-1,4,4], [4,-2,0]]
k = 0
print(QR.Q_builder(matrix_k, k))
print(' ')

print('''THE TWELVTH AND FINAL FUNCTION OF QR.PY IS HOUSEHOLDER, WHICH IS THE FUNCTION THE PREVIOUS FUNCTIONS
HAVE BEEN BUILDING TOWARDS. THIS FUNCITON WILL COMPUTE A QR DECOMPOSISTION VIA THE HOUSEHOLDER METHOD, AS OPPOSED
TO GRAM-SCHMIDT. ''')
print('''For example, given the input matrix [[1,1,1], [-1,4,4], [4,-2,0]], the result list [Q,R], will be: ''')
matrix_h = [[1,1,1], [-1,4,4], [4,-2,0]]
print(QR.Householder(matrix_h))
print(' ')

print('''THIS CONCLUDES THE DEMOSTRATION OF THE 12 FUNCTIONS IN QR.PY. NOW WE WILL MOVE ON THE DEMONSTRATING THE
FUNCTIONALITY OF LS.PY. ''')
print(' ')

print('''THE FIRST FUNCTION IN LS.PY IS BACK SUBSTITUTION. THIS FUNCTION IS USED TO SOLVE A SYSTEM OF EQUATIONS OF FORM
Ax = B.''')
print('''For example, if a matrix_A = [[4,0,0],[5,1,0],[6,2,3]] and a vector_B = [3,3,6], then the result x will be: ''')
matrix_A = [[4,0,0],[5,1,0],[6,2,3]]
vector_B = [3,3,6]
print(LS.back_substitution(matrix_A, vector_B))
print(' ')

print('''THE FINAL FUNCTION IN LS.PY IS LEAST_SQUARES. THIS FUNCTION TAKES A MATRIX AND A VECTOR AND RETURNS THE LEAST SQUARES SOLUTION
FOLLOWING THE FORM A*Ax = A*B (* is the transpose). ''')
print('''For example, if a matrix = [[1,1,1],[3,2,3], [6,2,8]] and a vector = [3,3,1], the result x will be:''')
matrix_bs = [[1,1,1],[3,2,3], [6,2,8]]
vector_bs = [3,3,1]
print(LS.least_squares(matrix_bs, vector_bs))

