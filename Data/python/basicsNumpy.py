import numpy as np
a = -3
# TODO: make a vector
vectorX = np.array([1,4,9])
vectorY = np.array([1,3,5])

# TODO: identity matrix 
# I3 = np.identity(3, dtype = float)
I3 = np.identity(3, dtype = int)
Zeros = np.zeros((3,3), dtype = int)
Ones = np.ones((2,3), dtype = int)

X = np.array([ [1,2,3], [4,5,6],[7,8,9] ])
Y = np.array([ [1,2,3], [2,5,6],[3,6,9] ])

print(I3)
print("\n")
print(Zeros)
print(Ones)
print(X)
print(Y)
# TODO: calculations

print(vectorX + vectorY)
print(np.dot(vectorX, vectorY))

# TODO: elementwise multiplication
print(vectorX*vectorY)

# TODO: use identity matrix with scalar
print(vectorX*I3*vectorY)
print(vectorX*vectorY*I3)

print("Important: insert Identity matrix in scalar matrix multiplication has the same result, eigenvalue equation!!")
print(a*I3)
print(a*X)
# TODO: matrix multiplication 
print(np.dot(a*I3 ,X))

# TODO: linear equation system Ax = b
# TODO: the numpy array is by row vector
A = np.array([[-1, 3], [3 ,5]])
# TODO: make this a column vector, 2 by 1
b = np.array([[3], [7]])
invA = np.linalg.inv(A)
print(invA)
x = np.dot(invA, b)
print(x)