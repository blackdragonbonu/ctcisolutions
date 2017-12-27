'''
This is the third Quesiton in the text, the second question of reversing a string has been avoided for now

Design an algorithm and write code to remove the duplicate characters in a string
without using any additional buffer. NOTE: One or two additional variables are fine.
An extra copy of the array is not.

We are gonna use to the method that we used for question one, we are gonna find a character iterate through the string and add it to the string if there is nothing unique.


'''

def iterative_solution(str):
	i=0
	output=[]
	for letter in str:
		if letter not in str[:i]:
			output.append(letter)
		i+=1
	return ''.join(output)

def solutions(str,method):
	if method=="iterative_solution":
		unique_str=iterative_solution(str)
		print ("The string after removing duplicates is : {0}".format(unique_str))


if __name__=="__main__":
	input=input("Enter a string to remove duplicates\n")
	solutions(input,"iterative_solution")
			
