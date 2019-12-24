# Author: Ken Obata
# Created Date: December, 24, 2019
# Description:
# This program reads input text file line by line and
# returns result of gram-schmidt process.
# At the end, user gets orthonomal basis.


import sys
import numpy
import math
import scipy.linalg as la
from numpy.linalg import matrix_power


# Function proj:
# Project vector v onto w.
def proj(v,w):
    v = numpy.array(v)
    w = numpy.array(w)
    scalar = float(numpy.sum(v * w)) / float(numpy.sum(w * w))
    
    return  numpy.array([scalar * element for element in w])

# Function gram_schmidt:
# Return orthonormal basis where it is a set of vector {v1,v2,...vn}
def gram_schmidt(Matrix):
    
    # variable declaration
    orthogonal_basis = []
    ortho_normal_basis = []
    size = len(Matrix)
    
    # Base vector
    v1 = Matrix[:,0]
    orthogonal_basis.append(v1)
    
    # If, Matrix has only one column, then return the orthogonal_basis.
    if(len(Matrix) == 1):
        return orthogonal_basis

    for i in range(1, len(Matrix)):
        # First create first projection.
        sum_proj = proj(Matrix[:,i] ,orthogonal_basis[0])

        # Perp Vi = Vi - (proj(Vi, v1) + proj(Vi, v2) + ...) <- get this sum of proj.
        for j in range(1, len(orthogonal_basis)):
            sum_proj += proj(Matrix[:,i] ,orthogonal_basis[j])
       
        orthogonal_basis.append(Matrix[:,i] - sum_proj)
    
    #normalize vectors
    for i in range(len(orthogonal_basis)):
        temp = orthogonal_basis[i] \
        /math.sqrt(numpy.sum(orthogonal_basis[i] * orthogonal_basis[i]))
        
        ortho_normal_basis.append(temp)

    return ortho_normal_basis



#get input
Matrix=[]
for line in sys.stdin:
    Array=line.split()
    Array = [int(i) for i in Array]
    Matrix.append(Array)

print("Input Matrix is:")
print(numpy.array(Matrix))

print("---------Gram Schmidt Process (Orthonormal basis)-------------")
ortho_normal_basis = gram_schmidt(numpy.array(Matrix))
print(numpy.array(ortho_normal_basis))
