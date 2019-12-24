# Author: Ken Obata
# Created Date: December, 24, 2019
# Description:
# This program reads input text file line by line and
# returns result of orthogonal diagonalization of a symmetric matrix.
# The equation is: input matrix = P*D*P_transpose
# where D is diagonal matrix with eigenvalues on diagonal entries.
# P is list of corresponding eigen vectors.

import sys
import numpy
import scipy.linalg as la
from numpy.linalg import matrix_power

# Dependencies:
import function_gram_schmidt as gram


def diagonal_matrix(Matrix):
    eigen_value, eigen_vector=numpy.linalg.eig(Matrix)
    
    return numpy.diag(tuple(eigen_value))

def eigenvector(Matrix):
    eigen_value, eigen_vector=numpy.linalg.eig(Matrix)
    
    return eigen_vector

# Function isSymmetrix(Matrix):
# Given a Matrix, this function returns True if Matrix is Symmetric.
# Return False otherwise.

def isSymmetric(Matrix):
    transpose = Matrix.T
    # If matrix is not symmetric square, print error message.
    for i in range(len(Matrix)):
        for j in range(len(Matrix[i]) ):
            if(Matrix[i][j] != transpose[i][j]):
                print("Matrix is not square Matrix.")
                return False
    return True


#get input
Matrix=[]
for line in sys.stdin:
    Array=line.split()
    Array = [int(i) for i in Array]
    Matrix.append(Array)

print("Input Matrix is:")
Matrix = numpy.array(Matrix)
print(Matrix)

#check if Matrix is Symmetric
if(isSymmetric(Matrix) is True):
    print("-----Ortho Diagonalize Input = P * D * P transpose-----")
    P = eigenvector(Matrix)
    
    #check orthogonality of columns in P
    print("---------Matrix P:-------------")
    P = numpy.array(gram.gram_schmidt(P)).T
    print(P)
    
    print("---------Matrix D:-------------")
    D = diagonal_matrix(Matrix)
    print(D)

    print("------Matrix P trans:----------")
    print(P.T)
