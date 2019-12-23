# Author: Ken Obata
# Created Date: December, 23, 2019
# Description:
# This program reads input text file line by line and
# returns result of diagonalization of a matrix.
# The equation is: input matrix = P*D*P_inverse
# where D is diagonal matrix with eigenvalues on diagonal entries.
# P is list of corresponding eigen vectors.


import sys
import numpy
import scipy.linalg as la
from numpy.linalg import matrix_power


def diagonal_matrix(Matrix):
    eigen_value, eigen_vector=numpy.linalg.eig(Matrix)
    
    return numpy.diag(tuple(eigen_value))

def eigenvector(Matrix):
    eigen_value, eigen_vector=numpy.linalg.eig(Matrix)

    return eigen_vector


#get input
Matrix=[]
for line in sys.stdin:
    Array=line.split()
    Array = [int(i) for i in Array]
    Matrix.append(Array)

print("Input Matrix is:")
print(numpy.array(Matrix))

print("---------Diagonalization of Matrix = P * D * P_inverse-------------")

print("---------Matrix P:-------------")
P = eigenvector(Matrix)
print(P)

print("---------Matrix D:-------------")
D = diagonal_matrix(Matrix)
print(D)

print("-------Matrix P inverse--------")
P_inv =la.inv(P)
print(P_inv)
