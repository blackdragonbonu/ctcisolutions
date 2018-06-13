'''
We are asked to check if a tree is balanced or not, we are going to use the tree from ds to implement the tree. We are going to check if the tree is balanced or not by keeping track of the maximum and minimum depth of each branch of a tree
'''

import ds.stack as stack
import ds.tree as Tree
import math

def check_if_balanced(current_node=None,branching_factor=2):
	max_child_depth=None
	min_child_depth=None
#	print ("==========================")
#	print ("Current Node : ",current_node.value)
#	print ("==========================")
	if len(current_node.children)<branching_factor:
#		print ("This is being run")
		min_child_depth=0
		max_child_depth=0
	for child in current_node.children:
		balanced,min_depth,max_depth=check_if_balanced(child)
#		print("Child : {0} Depth : {1},{2}".format(child.value,min_depth,max_depth))
		if not balanced:
			return False,-1,-1
		if (not max_child_depth==None) and (abs(max_child_depth-min_depth)>1 or abs(min_child_depth-max_depth)>1):
			return False,-1,-1
		if max_child_depth==None or max_child_depth<max_depth:
			max_child_depth=max_depth
		if  min_child_depth==None or min_child_depth>min_depth:
			min_child_depth=min_depth
	if min_child_depth==None or max_child_depth==None:
#		print ("Return depth : 1,1 ")
		return True,1,1
#	print("Return depth : ",min_child_depth+1,max_child_depth+1)
#	print ("Return current value : ",current_node.value)
	return True,min_child_depth+1,max_child_depth+1







if __name__=="__main__":
	sample_tree=Tree.Tree()

#	tree_string="1(2(3)(4))(5(6)(7))"
	tree_string="1(2(3))(4(5)(6(7)))"
	sample_tree.create_tree_prefix_string(tree_string)
	print(check_if_balanced(current_node=sample_tree.root)[0])


