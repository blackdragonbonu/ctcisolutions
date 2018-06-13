import numpy as np
from abc import ABC,abstractmethod

class Linked_list():
	def __init__(self):
		pass

	@abstractmethod
	def __add_node(self,**kwargs):
		pass

	@abstractmethod
	def __delete_node(self,**kwargs):
		pass

	@abstractmethod
	def print_list(self,**kwargs):
		pass
	
	def initialize_list(self,end_string='None'):
		print("This will add nodes to the linked list, enter the node values, to stop type : ",end_string)
		while True:
			input_val=input("Enter value \n")
			if input_val==end_string:
				break
			self._add_node(value=input_val)
			

class Node():
	def __init__(self,**kwargs):
		node_type=kwargs.pop('type','single')
		node_value=kwargs.pop('value',None)
		if not node_value:
			try :
				raise ValueError('Got no input for node_value')
			except ValueError:
				print ("Please make sure that you enter a value corresponding to node_value")
		if node_type=='single':
			self.value=node_value
			self.forward=None
		elif node_type=='double':
			self.value=node_value
			self.forward=None
			self.backward=None
		else:
			try:
				raise ValueError("Incorrect option passed for node_type")
			except ValueError:
				print("Please make sure that the value entered for node_type is either single or double")

		


class Single_linked_list(Linked_list):
	def __init__(self):
		self.head=None
		self.tail=None

	def _add_node(self,**kwargs):
		node_value=kwargs.pop('value',None)
		if not node_value:
			try:
				raise ValueError('Value of a new node cannot be None')
			except ValueError:
				print("Please ensure that a None none value is passed")
				return


		new_node=Node(value=node_value)
		if not self.head:
			self.head=new_node
		else :
			self.tail.forward=new_node
		self.tail=new_node

	def _delete_node(self,**kwargs):
		node_value=kwargs.pop('value',None)
		current_node=self.head
		if not self.head:
			try:
				raise ValueError('The linked list is empty and hence operation is not permitted')
			except ValueError:
				print ("Please ensure that linked list is not empty before deletion")
				return

		if not node_value:
			if current_node==self.tail:
				self.head=None
				self.tail=None
				return

			while not current_node.forward==self.tail:
				current_node=current_node.forward
			current_node.forward=None
			self.tail=current_node
		else :
			if node_value==self.head.value and self.head==self.tail:
				self.head=None
				self.tail=None
				return
			if node_value==self.head.value:
				self.head=current_node.forward
				return

			while not current_node.forward.value==node_value:
				current_node=current_node.forward

			current_node.forward=current_node.forward.forward

			if current_node.forward==None:
				self.tail=current_node
			return
	
	def print_list(self):
		current_node=self.head
		while current_node:
			print (current_node.value,end='',flush=True)
			if  current_node.forward:
				print("->",end='',flush=True)
			current_node=current_node.forward
		print ("\n")

	def initialize_linked_list(self,end_string='None'):
		print ("Enter the elements of the linked list, To stop entering type : ",end_string)
		while True:
			input_val=input("Enter value \n")
			self._add_node(input_val)
		
class double_linked_list(Linked_list):
	def __init__(self):
		self.head=None
		self.tail=None

	def _add_node(self,**kwargs):
		node_value=kwargs.pop('value',None)
		if not node_value:
			try:
				raise ValueError('Value of a new node cannot be None')
			except ValueError:
				print("Please ensure that a None none value is passed")
				return


		new_node=Node(value=node_value,type='double')
		if not self.head:
			self.head=new_node
		else :
			self.tail.forward=new_node
			new_node.backward=self.tail
		self.tail=new_node

	def _delete_node(self,**kwargs):
		node_value=kwargs.pop('value',None)
		current_node=self.head
		if not self.head:
			try:
				raise ValueError('The linked list is empty and hence operation is not permitted')
			except ValueError:
				print ("Please ensure that linked list is not empty before deletion")
				return

		if not node_value:
			if current_node==self.tail:
				self.head=None
				self.tail=None
				return

			while not current_node.forward==self.tail:
				current_node=current_node.forward
			current_node.forward=None
			self.tail=current_node
			
		else :
			if node_value==self.head.value and self.head==self.tail:
				self.head=None
				self.tail=None
				return
			if node_value==self.head.value:
				self.head=current_node.forward
				self.head.backward=None
				return

			while not current_node.forward.value==node_value:
				current_node=current_node.forward

			if not current_node.forward==self.tail:
				current_node.forward.forward.backward=current_node
			else:
				self.tail=current_node
			current_node.forward=current_node.forward.forward

			return
		
	def print_list(self):
		current_node=self.head
		while current_node:
			print (current_node.value,end='',flush=True)
			if  current_node.forward:
				print("->",end='',flush=True)
			current_node=current_node.forward
		print ("\n")
						
				
if __name__=='__main__':
	print ("Enter the value for new node, enter None to exit")
	new_list=double_linked_list()
	new_list.initialize_list()
	new_list.print_list()
	print ("Enter the node that you want to be deleted")
	input_val=input("Enter value of the node \n")
	new_list._delete_node(value=input_val)
	new_list.print_list()


	
			
