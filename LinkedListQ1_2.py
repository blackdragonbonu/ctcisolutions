from ds.LinkedList import Single_linked_list

def remove_duplicates_iter(linked_list):
	curr_node=linked_list.head.forward
	while curr_node:
		check_node=linked_list.head
		found=False
		while True:
			if check_node.value==curr_node.value:
				found=True
			if check_node.forward==curr_node:
				break

			check_node=check_node.forward
		
		if found:	
			check_node.forward=curr_node.forward

		curr_node=curr_node.forward



if __name__=='__main__':
	new_list=Single_linked_list()
	new_list.initialize_list()
	new_list.print_list()
	remove_duplicates_iter(new_list)
	new_list.print_list()
