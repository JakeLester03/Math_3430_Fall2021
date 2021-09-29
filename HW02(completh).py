"""
For this homework assignment we will take our work from HW01 and use it to
prepare a python script which will implement our algoirthms as python functions. 

For Problems #0-5 from HW01, Do the following.



1) Write your answer from HW01 in a comment.

2) Below the comment write a function which implements the algorithm from your
comment. If you find that you need to change your algorithm for your python
code, you must edit your answer in the comment. 

3) Test each of your functions on at least 2 inputs. 

4) Upload your .py file to a github repo named "Math_3430_Fall_2021"

This assignment is due by 11:59pm 09/27/2021. Do NOT upload an updated version to github
after that date. 
"""


#Example:

#Problem 00

"""
-The Three Questions

Q1: What do we have?

A1: Two vectors stored as lists. Denoted by the names vector_a and vector_b. 

Q2: What do we want?

A2: Their sum stored as a list.

Q3: How will we get there?

A3: We will create an empty list of the appropriate size and store the sums of
the corresponding components of vector_a and vector_b. 

-PsuedoCode

def add_vectors(vector_a,vector_b):

Initialize a result vector of 0's which is the same size as vector_a. Call this
vector result.

# Set each element of result to be equal to the desired sum.
for index in range(length(result)):
  result[index] = vector_a[index] + vector_b[index]

Return the desired result.
"""

def add_vectors(vector_a,vector_b):
  result = [0 for element in vector_a]
  for index in range(len(result)):
    result[index] = vector_a[index] + vector_b[index]
  return result

#End Example



#Problem 01 Scalar Vector Multiplication
''''
1. What do we have? We have a scalar named scalar and a vector called vector_a stored in a computer.
2. What do we want? We want a new result vector multiplied by the scalar.
3. How do we get there? We will create a result vector called result and multiply the elements in vector by the scalar

### pseudo code
def scalar_vector_mult(scalar_vector_a):
#initialize result vector as a list of 0's the same size as vector_a, making it a copy.
#let the list be a copy of elements in vector_a
#iterate for loop for elements in vector_a to be multiplied by the scalar number
#for loop for vector_a[index] * scalar
#make the elements in result equal to the product of the scalar and the vector
#result[index]= vector_a[index] * scalar
#return result
'''''

###Code###
def scalar_vector_mult(vector_a, scalar):
  result = [0 for elements in vector_a]
  for index in range(len(vector_a)):
    result[index] = vector_a[index] * scalar
  return result
###Test###
vector_a=[1,2,3]
scalar=3

#scalar_vector_mult(vector_a, scalar) should output [3,6,9]
print('Test Output for scalar_vector_mult: ' + str(scalar_vector_mult(vector_a, scalar)))
print('Should have been [3, 6, 9]')

vector_b=[2,4,6]
scalar_b=2

#scalar_vector_mult(vector_a, scalar) should output [4, 8, 12]
print('Test Output for scalar_vector_mult: ' + str(scalar_vector_mult(vector_b, scalar_b)))
print('Should have been [4, 8, 12]')

#Problem 02 Scalar Matrix Multiplication
''''
1. What do we have? a scalar called a scalar and a matrix called matrix_a stored as a list of lists, where each list represents a column vector.
2. What do we want? we want a matrix which is the scaled version of the given matrix.
3. How will we get there? we will copy matrix into a result matrix called result. Then we can append
scalar_vector_multi on each of the column vector now stored in result to give us the desired product

###pseudo code###
define scalar_matrix_multi(matrix, scalar)
#initialize result as a list to be a copy of the matrix called result
#by using a for loop similar to problem01, we can index through the column vectors in matrix stored as a list
#after running for loop, we can use scalar_vector_mult to multiply the scalar by each of the elements in the column vectors in the result matrix
#return result
'''
###Code###
#to execute properly I had to generalize my variable names from problem 1 (i.e. vector_a became "vector")#
#using scalar_vector_mult(vector, scalar)
###
def scalar_vector_mult(vector, scalar):
    result = [0 for elements in vector]
    for index in range(len(vector)):
        result[index] = vector[index] * scalar
    return result
###
def scalar_matrix_mult(matrix_a, scalar):
    result = []
    for index in range(len(matrix_a)):
        result.append(scalar_vector_mult(matrix_a[index], scalar))
    return result

###test###
matrix_a = [[2, 4], [6, 8]]
scalar = 2

# scalar_matrix_mult(matrix_a, scalar) should output [[4, 8], [12, 16]]
print('Test Output for scalar_matrix_mult: ' + str(scalar_matrix_mult(matrix_a,scalar)))
print('Should have been [[4,8], [12, 16]]')

matrix_b=[[1,2,3],[3,4,5],[5,6,7]]
scalar_b=3

# scalar_matrix_mult(matrix_a, scalar) should output [[3, 6, 9], [9, 12, 15], [15, 18. 21]]
print('Test Output for scalar_matrix_mult: ' + str(scalar_matrix_mult(matrix_b,scalar_b)))
print('Should have been [[3,6,9], [9, 12, 15],[15, 18, 21]]')

#Problem 03 Matrix Addition
'''
1.What do we have? We have two matricies stored as lists of lists called matrix_a and matrix_b. Each list within the lists in the matricies represents  a column.
2.What do we want? We want the sum of the two matricies
3.How do we get there? We will initialize a result matrix as a copy of matrix_a. Then for each list
in result we will add the corresponding list from matrix_b. We can append add_vectors from the example to take the sum of the matricies.

##pseudo code

def matrix_add(matrix_a, matrix_b)
##initialize result matrix as a copy of matrix a
result = [ ]
#we can use a for loop for each list in result and then we can append it with add_vectors
    for index in range(len(matrix_a)):
        result.append(add_vectors(matrix_a[index], matrix_b[index]))
return result 
'''
def add_matrix(matrix_a, matrix_b):
    result = []
    for index in range(len(matrix_a)):
        result.append(add_vectors(matrix_a[index], matrix_b[index]))
    return result

matrix_a = [[1,2,3], [4,5,6], [7, 8, 9]]
matrix_b = [[1,2,3], [4,5,6], [7, 8, 9]]

#matrix_add(matrix_a, matrix_b) should result [2, 4, 6], [8, 10, 12], [14, 16, 18]
print('Problem 3:Test Output for add_matrix: ' + str(add_matrix(matrix_a, matrix_b)))
print('Should have been [[2, 4, 6], [8, 10, 12], [14, 16, 18]]')

matrix_γ = [[3,2,1], [6,5,4], [9,8,7]]
matrix_δ = [[1,1,1], [2,2,2], [3,3,3]]

#matrix_add(matrix_γ, matrix_δ) should result [[4,3,2], [8,7,6], [12, 11, 10]]
print('Test Output for add_matrix: ' + str(add_matrix(matrix_γ, matrix_δ)))
print('Should have been [[4, 3, 2], [8, 7, 6], [12, 11, 10]]')

#Problem 04 Matrix Vector multiplication
'''
1. What do we have? We have a matrix called matrix, where each component list 
represents a column of the matrix, and a vector stored as a list.
2.What do we want? we want the product of the two matricies stored as a new list.
3. How will we get there? We will create a list of 0's equal to the size of the vector. We can then implement a linear combination
by multiplying the elements in the matrix by the corresponding column vectors. We can use scalar_vector_mult. Then we can use add_vectors to store the products to the new result.

#Pseudo Code
def matrix_vector_mult(matrix, vector)
First we can initialize a result vector of 0's which is the same size as matrix. Call this
vector result.
Then we can use a for loop each to make the elements equal to the combination of scalar_vector_mult and add_vectors
for index in range(len(matrix)):
    result[index] = (add_vectors(scalar_vector_mult(matrix[index], vector[index])))

'''
def matrix_vector_mult(matrix, vector):
    result = [0 for element in matrix]
    for index in range(len(matrix)):
        result[index] = (add_vectors(scalar_vector_mult(matrix[index], vector[index])))
    return result

matrix_a = [[1, 1], [1, 1]]
vector_a = [100, 100]

# matrix_vector_mult(matrix_a, vector_a) should output [200,200]
print('Test Output for matrix_vector_mult: ' + str(matrix_vector_mult(matrix_a, vector_a)))
print('Should have been [200, 200]')
#

matrix_c = [[1,1,1], [1,1,1], [1,1,1]]
vector_c = [100, 100, 100]

#matrix_vector_mult_=(matrix_c, vector_c) should output [300,300,300]
print('Test Output for matrix_vector_mult: ' + str(matrix_vector_mult(matrix_c, vector_c)))
print('Should have been [300, 300, 300]')


#Problem 05 Matrix Matrix Multiplication
'''
1.What do we have? We have two matricies stored as lists of lists, where each component list represents a column. We call 
these matricies matrix_a and matrix_b.
2.What do we want? We want the product matrix_a and matrix_b
3.How will we get there? We will create a result matrix which is a copy of matrix_b, called result.
then for each component of result, we will overwirte it with
matrix_vector_mult(matrix_a, matrix_b) by using append

##Pesudo code
def matrix_matrix_mult(matrix_a, matrix_b):
#Initailize result of matrix_b as a list:
    for index in matrix_b:
        result.append(matrix_vector_mult(matrix_a[index], matrix_b[index]))
#
'''
#Code
def matrix_matrix_mult(matrix_a, matrix_b):
    result = []
    for index in matrix_b:
        result.append(matrix_vector_mult(matrix_a[index], matrix_b[index]))
    return result

#Test
matrix_a = [[1,1,1],[1,1,2],[1,2,3]]
matrix_b = [[100,100,100], [100,100,100], [100,100,100]]
#matrix_matrix_mult(matrix_a, matrix_b) should output [[300,400, 500], [300, 400, 500], [300, 400, 500]]
print('Test Output for matrix_matrix_mult:' + str(matrix_matrix_mult(matrix_a, matrix_b))
print('Should have been [[300,400, 500], [300, 400, 500], [300, 400, 500]]')

matrix_2 = [[1,2],[2,1]]
matrix_3 = [[10, 20], [30, 40]
#matrix_matrix_mult(matrix_a, matrix_b) should output [[50,40], [110, 100]]
print('Test Output for matrix_matrix_mult:' + str(matrix_matrix_mult(matrix_2, matrix_3))
print('Should have been [[50,40], [110, 100]]')

