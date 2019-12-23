import sys
import numpy
import scipy.linalg as la
from numpy.linalg import matrix_power


def diagonal_matrix(Matrix):
    eigen_value, eigen_vector=numpy.linalg.eig(Matrix)
    
    return numpy.diag(tuple(eigen_value))

def eigenvector(Matrix):
    eigen_value, eigen_vector=numpy.linalg.eig(Matrix)

    #debug
    #v1 = eigen_vector[:,0] # First column is the first eigenvector
    
    #list_eigen_vector=[]
    #for i in range(len(eigen_vector)):
    #list_eigen_vector.append(eigen_vector[i])
    return eigen_vector


#get input
Matrix=[]
for line in sys.stdin:
    Array=line.split()
    Array = [int(i) for i in Array]
    Matrix.append(Array)


#convert into int
#Matrix = [int(i) for i in Matrix]
#Matrix = numpy.array(Matrix)
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
