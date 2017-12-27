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
		while start!=None:
			print("{} -> ".format(start.value),end="")
			start=start.next
		print("None")


if __name__=="__main__":
	a=linked_list([1,2,3])
	a.display_list()
	a.add_element("albert")
	a.display_list()


