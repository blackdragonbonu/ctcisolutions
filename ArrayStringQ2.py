'''
This is the third Quesiton in the text, the second question of reversing a string has been avoided for now

Design an algorithm and write code to remove the duplicate characters in a string
without using any additional buffer. NOTE: One or two additional variables are fine.
An extra copy of the array is not.

We are gonna use to the method that we used for question one, we are gonna find a character iterate through the string and add it to the string if there is nothing unique.

The second solution that we are going to use does not create a new buffer per say we assume that the input to the second solution is an array of characters instead of a string. This is true in non Python languages, in python strings are immutable hence inplace string modification is forbidden. This is to illustrate the fundamental concept of a two pronged apprach to this problem.
'''

def iterative_solution(str):
	i=0
	output=[]
	for letter in str:
		if letter not in str[:i]:
			output.append(letter)
		i+=1
	return ''.join(output)

def inplace_solution_arr(list_str):
	start_index=0
	stop_index=0
	while stop_index<len(list_str):
		if not start_index==stop_index:
			found=False
			for i in range(start_index-1,-1,-1):
				if list_str[i]==list_str[stop_index]:
					found=True
			if not found:
				list_str[start_index]=list_str[stop_index]
				start_index+=1
		stop_index+=1
	return list_str[:start_index]

def inplace_solution(str):
	str_list=list(str)
	return ''.join(inplace_solution_arr(str_list))


def solutions(str,method):
	if method=="iterative_solution":
		unique_str=iterative_solution(str)
		print ("The string after removing duplicates is : {0}".format(unique_str))

	if method=="inplace_solution":
		unique_str=inplace_solution(str)
		print ("The string after removing duplicates is : {0}".format(unique_str))

if __name__=="__main__":
	input_str=input("Enter a string to remove duplicates\n")
	solutions(input_str,"iterative_solution")
	solutions(input_str,"inplace_solution")
		
