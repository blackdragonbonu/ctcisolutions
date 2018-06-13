'''
In this question we are asked to add a new function to stack that finds the minimum element in order of 1 time. Our solution works as follows.
We have another stack , where we keep track of minimum values. When ever we encounter a value smaller than the top of the stack we push into stack
'''

import ds.stack as stack

if __name__=="__main__":
	print("Enter numbers to be enterred to the stack, we will then show minimum of stack as  the elements are popped one at a time")
	print("Enter None when you want to stop")
	s1=stack.stack()
	s2=stack.stack()
	while(True):
		number=input("Enter number to be added to stack \n")
		if number=='None':
			break
		else :
			number=int(number)
		s1.push(number)
		current_min=s2.peek()
		if not current_min or current_min>number:
			s2.push(number)
	
	while s1.peek():
		elem_popped=s1.pop()
		if elem_popped==s2.peek():
			s2.pop()
		print ("Element popped : {0} and Current Min {1}".format(
			elem_popped,s2.peek()))
	
