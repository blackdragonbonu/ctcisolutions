'''
this is question 5 of array string 

Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column is set to 0.

There are two implementations and we are gonna do both, one with extra memory and the 
second that uses the matrix to represent the elements
'''

def normal_solution(matrix):
	row_zero=set()
	colomn_zero=set()
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			print(i,j)
			if matrix[i][j]==0:
				row_zero.add(i)
				colomn_zero.add(j)
	#setting matrix to zero

	for row in row_zero:
		for i in range(len(matrix[row])):
			matrix[row][i]=0
	for colomn in colomn_zero:
		for i in range(len(matrix)):
			matrix[i][colomn]=0

	return matrix


def optimized_solution(matrix):
	#check if there are any zeroes in first row or first colomn
	row_zero=False
	colomn_zero=False
	for i in range(len(matrix[0])):
		if matrix[0][i]==0:
			row_zero=True
			break
	for i in range(len(matrix)):
		if matrix[i][0]==0:
			colomn_zero=True
			break
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if matrix[i][j]==0:
				matrix[0][j]=0
				matrix[i][0]=0
	#setting rows to zero
	for i in range(len(matrix)):
		if matrix[i][0]==0:
			for j in range(len(matrix[0])):
				matrix[i][j]=0

	for i in range(len(matrix[0])):
		if matrix[0][i]==0:
			for j in range(len(matrix)):
				matrix[j][i]=0

	if row_zero:
		for i in range(len(matrix[0])):
			matrix[0][i]=0
	if colomn_zero:
		for i in range(len(matrix)):
			matrix[i][0]=0

	return matrix



def display_matrix(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			print("| {0} |".format(matrix[i][j]),end="")
		print("")
		print("-"*5*len(matrix[i]))


def solutions(matrix,method):
	if method=="normal_solution":
		matrix=normal_solution(matrix)
		print("The matrix after setting the rows and coloumn to zero are as follows : \n")
		display_matrix(matrix)

	elif method=="optimized_solution":
		matrix=optimized_solution(matrix)
		print("The matrix after setting the rows and coloumn to zero are as follows : \n")
		display_matrix(matrix)


def input_matrix():
	matrix=[]
	input_x=int(input("Enter number of rows in matrix\n"))
	input_y=int(input("Enter number of coloumn in matrix\n"))
	for i in range(input_x):
		row_vector=[]
		for j in range(input_y):
			row_vector.append(int(input("Enter value at position {0}{1}".format(i,j))))
		matrix.append(row_vector)
	return matrix

if __name__=="__main__":
	matrix=input_matrix()
	solutions(matrix,"optimized_solution")
