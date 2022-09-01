# A basic code for matrix input from user

print("Enter details of matrix A : ")
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

# Initialize matrix
matrix_1 = []
print("Enter the entries rowwise:")

# For user input
for i in range(R):		 # A for loop for row entries
	a =[]
	for j in range(C):	 # A for loop for column entries
		a.append(int(input()))
	matrix_1.append(a)

# For printing the matrix
print("Matrix A : ")
for i in range(R):
	for j in range(C):
		print(matrix_1[i][j], end = " ")
	print()

print("Enter details of matrix B : ")
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

# Initialize matrix
matrix_2 = []
print("Enter the entries rowwise:")

# For user input
for i in range(R):		 # A for loop for row entries
	a =[]
	for j in range(C):	 # A for loop for column entries
		a.append(int(input()))
	matrix_2.append(a)

# For printing the matrix
print("Matrix B : ")
for i in range(R):
	for j in range(C):
		print(matrix_2[i][j], end = " ")
	print()

# We need install numpy in order to import it
import numpy as np

# This will return dot product
res = np.dot(matrix_1,matrix_2)

print("multiplication of Matrixs A and B : \n,..,")
# print resulted matrix
print(res)

