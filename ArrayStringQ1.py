'''
The question is As follows :

Implement an algorithm to determine if a string has all unique characters. What if you
can not use additional data structures?

the basic idea is we need to determine if a string has all unique characters, there are two ways of doin this
the first way is to use a hash. The alternative is to check or the remainder for duplicates
'''
solutions_available=2
inputs_required=1
input_type=['str']

def hash_solution(str):
	letter_seen={}
	for letter in list(str):
		if letter in letter_seen:
			return False
		else:
			letter_seen[letter]=1
	return True

def iterative_solution(str):
	for index,letter in enumerate(list(str)):
		for upcoming_letter in list(str)[index+1:]:
			if letter==upcoming_letter:
				return False
	return True

def solutions(str,method):
	if method=="hash_solution":
		check=hash_solution(str)
	elif method=="iterative_solution":
		check=iterative_solution(str)
	if check:
		print ("The string is composed of unique characters")
	else:
		print ("String is not composed of unique characters")



if __name__=="__main__":
	input=input("Enter a string that you want to be checked for unique characters\n")
	solutions(input,"iterative_solution")

