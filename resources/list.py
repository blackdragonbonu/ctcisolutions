'''
Created By : Albert James

This is the basic list implementation that we are going to use for our projects


'''
class list_element():
	def __init__(self,arg):
		self.value=arg
		self.next=None



class linked_list(object):
	head=None
	last=None
	"""This is the linked list implementation that we are going to use for our project, 
	we can initialise a linked list by providing  a list or a value"""
	def add_element(self,arg):
		if self.head==None:
			self.head=list_element(arg)
			self.last=self.head
		else:
			self.last.next=list_element(arg)
			self.last=self.last.next


	def __init__(self, arg):
		if type(arg)==list:
			for element in arg:
				self.add_element(element)
				
		else:
			self.head=list_element(arg)
			self.last=self.head

	
	def display_list(self):
		start=self.head
		while start and start!=self.last:
			print("{} -> ".format(start.value),end="")
			start=start.next
		if start==self.last:
			print("{} -> ".format(start.value),end="")
			if self.last.next:
				print("{}->".format(self.last.next.value),end="")

		print("None")

	def middle_element(self):
		slow=self.head
		fast=self.head
		while slow.next!=None:
		#	print(slow.value,fast.value)
			if fast and fast.next and fast.next.next:
				fast=fast.next.next
				slow=slow.next
			else:
				break
		return slow

	def middle_elements(self):
		""" Returns all middle elements returns two middle elments when they are even"""		
		slow=self.head
		fast=self.head
		while slow.next!=None:
		#	print(slow.value,fast.value)
			if fast and fast.next and fast.next.next:
				fast=fast.next.next
				slow=slow.next
			elif fast and fast.next:
				return (slow,slow.next)
			else:
				break
		return tuple(slow)
	
	def reverse_list_recursive(self,current_node=None):
		if not current_node:
			current_node=self.head
		if current_node.next:
			previous_node=self.reverse_list_recursive(current_node.next)
			previous_node.next=current_node
		else:
			self.head=current_node
		current_node.next=None	
		return current_node

	def reverse_list_iterative(self):
		current_node=self.head
		previous_node=None
		if current_node:
			next_node=self.head.next
		else :
			return 
		while next_node:
			current_node.next=previous_node
			previous_node=current_node
			current_node=next_node
			next_node=next_node.next
		current_node.next=previous_node
		self.head=current_node
		return 

	#the cycle will be created with the last element of the existing list 
	def add_cycle(self,cycle_elements):
		loop_element=self.last
		for element in cycle_elements:
			self.add_element(element)
		self.last.next=loop_element

			
		
__all__=['linked_list']
if __name__=="__main__":

	a=linked_list(input().split())
	a.display_list()
	a.add_cycle(input().split())
	a.display_list()
