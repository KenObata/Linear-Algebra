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
    return numpy.sum(v * w)/numpy.sum(w * w) * w

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
    
    # Perp v2 = v2 - Proj(v2, v1) #projection of V2 onto v1
    v2 = Matrix[:,1]  - proj(Matrix[:,1] ,v1)
    orthogonal_basis.append(v2)
    
    # Perp v3 = v3 - (Proj(v3, v1) + proj(v3, v2))
    v3 = Matrix[:,2] - proj(Matrix[:,2], v1) - proj(Matrix[:,2], v2)
    orthogonal_basis.append(v3)
    
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

print("---------Gram Schmidt Process-------------")
ortho_normal_basis = gram_schmidt(numpy.array(Matrix))
print(numpy.array(ortho_normal_basis))
