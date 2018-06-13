'''
We are asked to write a code to generate a tree given a sorted array. So for the pupose of this question we are goinhg to use the tree implemented in ds. So inorder to create a tree from a sorted array of minimum height we are gonna aim at creating the postfix string of minimum height. This would enable creation of tree of minimum height by extension.
'''
import ds.tree as tree
import ds.queue as queue
import ds.LinkedList as llist

def create_binary_tree_from_sorted_array(sorted_array):
	return generate_string(sorted_array,0,len(sorted_array)-1)

def generate_string(sorted_array,start,stop):
	if start>stop:
		return ""
	if start==stop:
		return str(sorted_array[start])
	middle=(start+stop)//2
	if start>middle-1:
		return '{0}({1})'.format(sorted_array[middle],generate_string(sorted_array,middle+1,stop))
	elif middle+1>stop:
		return '{0}({1})'.format(sorted_array[middle],generate_string(sorted_array,start,middle-1))
	return '{0}({1})({2})'.format(sorted_array[middle],generate_string(sorted_array,start,middle-1),generate_string(sorted_array,middle+1,stop))
	
def create_depth_wise_lists(sample_tree):
	process_queue=queue.Queue()
	list_of_linkedlist=[]
	depth=0
	process_queue.push((sample_tree.root,1))
	current_list=llist.Single_linked_list()
	while True:
		if process_queue.size==0:
			break
		current_node,current_depth=process_queue.pop()
		if not depth==current_depth:
			current_list=llist.Single_linked_list()
			list_of_linkedlist.append(current_list)
			current_list._add_node(value=current_node.value)
			depth=current_depth
		else:
			current_list._add_node(value=current_node.value)

		for child in current_node.children:
			process_queue.push((child,depth+1))
		
	return list_of_linkedlist
	


if __name__=='__main__':
	print("Enter the elements from which the binary tree needs to be formed, enter them in comma seperated format")
	values=list(map(int,input().split(',')))
	values=sorted(values)
	prefix_string=create_binary_tree_from_sorted_array(values)
	print("String for tree generation : ",prefix_string)
	sample_tree=tree.Tree()
	sample_tree.create_tree_prefix_string(prefix_string)
	list_of_linkedlists=create_depth_wise_lists(sample_tree)
	for linklist in list_of_linkedlists:
		linklist.print_list()
	
	
