'''
The problem statement 

Write a method to replace all spaces in a string with ‘%20’

'''

def simple_solution(str):
	return str.replace(' ',"%20")


def solutions(str,method):
	if method=="simple_solution":
		print ("The modified string is {0}".format(simple_solution(str)))


if __name__=="__main__":
	str=input("Enter the string with spaces\n")
	solutions(str,"simple_solution")