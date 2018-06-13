'''
Implement an algorithm to find the nth last element in a single linked list.

We solve the problem as follows ,we have two pointers. The first pointer starts n-1 moves ahead of the second pointer, then they
move at the same speed till they reach the end of the sentence. Then the second pointer corresponds to the nth last element

'''
from ds.LinkedList import Single_linked_list

def find_nth_last(linked_list,n):
	slow_pointer=linked_list.head
	fast_pointer=linked_list.head
	for i in range(n):
		if not fast_pointer:
			return slow_pointer.value
		else:
			fast_pointer=fast_pointer.forward
	while fast_pointer:
		slow_pointer=slow_pointer.forward
		fast_pointer=fast_pointer.forward
	return slow_pointer.value



if __name__=='__main__':
	print("Enter the elemnets of linked list, enter None once you are done entering all the elements")
	new_list=Single_linked_list()
	
	while(True):
		input_val=input("Enter value \n")
		if input_val=='None':
			break
		new_list._add_node(value=input_val)
	input_nth=int(input("Enter the n for nth last element \n"))
	print ("Nth last element is : ",find_nth_last(new_list,input_nth))
		
