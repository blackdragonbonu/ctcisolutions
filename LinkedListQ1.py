'''
This is a single file for problems 1 to 5 in linked list
'''

from resources.list import *


def elment_already_seen(value,last_element,linked_list):
	start=linked_list.head
	while start !=last_element:
		if start.value==value:
			return True
		start=start.next
	return False

def remove_duplicates(linked_list):
	current=linked_list.head
	previous=linked_list.head
	while current:
		if elment_already_seen(current.value,current,linked_list):
			print(current.value,"True")
			previous.next=current.next
			del current
			current=previous
		previous=current
		current=current.next

def find_nth_from_last(n,linked_list):
	current=linked_list.head
	future=linked_list.head
	for i in range(n):
		if not future:
			return None
		future=future.next
	while future:
		future=future.next
		current=current.next
	return current

def remove_middle_element(middle_element):
	backup=middle_element.next
	middle_element.value=backup.value
	middle_element.next=backup.next
	return

def sum_linked_list(linked_list_A,linked_list_B):
	A=linked_list_A.head
	B=linked_list_B.head
	c=0
	out=[]
	while A or B:
		if A:
			a=int(A.value)
			A=A.next
		else :
			a=0
		if B:
			b=int(B.value)
			B=B.next
		out.append((a+b+c)%10)
		c=(a+b+c)//10
	if c>0:
		out.append(c)
	return linked_list(out)

def find_start_of_cycle(linked_list):
	slow=linked_list.head
	fast=linked_list.head.next
	while slow!=fast:
		slow=slow.next
		for i in range(2):
			fast=fast.next
			if slow==fast:
				break
	slow=linked_list.head
	while slow!=fast:
		fast=fast.next
		if slow==fast:
			break
		slow=slow.next
	return slow

if __name__=="__main__":
	user_input=input("type the elements of the linked list seperated by spaces\n").split(' ')
	a=linked_list(user_input)
	#a.display_list()
	#remove_middle_element(a.middle_element())
	a.display_list()
	user_input=input("type the elements of the cycle  seperated by spaces\n").split(' ')
	a.add_cycle(user_input)
	a.display_list()
	cycle_start=find_start_of_cycle(a)
	print(cycle_start.value)

	# user_input=input("type the elements of the linked list seperated by spaces\n").split(' ')
	# a=linked_list(user_input)
	# a.display_list()
	# user_input=input("type the elements of the linked list seperated by spaces\n").split(' ')
	# b=linked_list(user_input)
	# b.display_list()
	# c=sum_linked_list(a,b)
	# c.display_list()

	# remove_duplicates(a)
	# a.display_list()

	# user_input=int(input("N value for findding nth from the end\n"))
	# out=find_nth_from_last(user_input,a)
	# if out:
	# 	print(out.value)
	# else:
	# 	print("The array does not have {} elements".format(user_input))

