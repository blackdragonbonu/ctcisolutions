'''
In this question we are asked to implement a set of stacks. We create a list of stacks and add a new stack to it ones the capacity is reached. We keep doing this for all the element
'''
from ds.stack import stack

def SetOfStacks():
	def __init__(self,max_capacity=5):
		self.set_of_stacks=[]
		self.max_capacity=max_capcity
		self.current_stack=0
		self.set_of_stacks.append(stack())
	
	def push(self,value):
		if self.set_of_stacks[self.current_stack].size==self.max_capacity:
			self.set_of_stacks.append(stack())
			self.current_stack+=1
		
		self.set_of_stacks[self.current_stack].push(value)
	
	def pop(self):
		if self.set_of_stacks[self.current_stack].size==0:
			if self.current_stack==0:
				try:
					raise Exception("Stack Empty ")
				except Exception:
					print ("Take care while popping")
			else:
				self.set_of_stacks=self.set_of_stacks[:-1]
				self.current_stack-=1
		return self.set_of_stacks[self.current_stack].pop()
	
	def pop_at(self,location):
		if location> len(self.set_of_stacks)-1:
			print ("Error")	
			return
		
		if self.set_of_stacks[location].size==0:
			location-=1

		if location<0:
			print("Error ")
			return
			
		return self.set_of_stacks[location].pop() 



if __name__=='__main__':
	print("Enter values, type None to stop")
	stack_set=SetOfStacks(max_capacity=2)
	while(True):
		input_val=input("Enter the value to add to stack \n")
		if input_val=='None':
			break
		stack_set.push(input_val)
	while(True):
		print ("What do you want to do next ? ")
		print ("1. Pop elements from stack ")
		print ("2. pop elements at a specific location")
		print ("3. Exit")
		input_choice=input()
		if input_choice=="3":
			break
		elif input_choice=="1":
			stack_set.pop()
		elif input_choice=="2":
			location=input("Enter location to pop \n")
			stack_set.pop_at(location)
	




		


