'''
In this question we are asked to check if a tree is a subtree of another tree. The approach is as follows, we move along the larger tree, if we find that there is a match along the second tree then we do as follows, we then recursively check if all the elements are the same if they are the same we return true else we return false

'''
import ds.tree as tree
import ds.stack as stack

def find_if_subtree(larger_tree,smaller_tree):
	process_stack=stack.stack()
	process_stack.push(larger_tree.root)
	while True:
		if process_stack.size==0:
			return False
		current_node=process_stack.pop()
		if current_node.value==smaller_tree.root.value:
			if check_if_same(current_node,smaller_tree.root):
				return True
		for child in current_node.children:
			process_stack.push(child)
	

def check_if_same(first_tree_node,second_tree_node):
	if not first_tree_node.value==second_tree_node.value:
		return False
	if not len(first_tree_node.children)==len(second_tree_node.children):
		return False
	for i in range(len(first_tree_node.children)):
		similarity=check_if_same(first_tree_node.children[i],second_tree_node.children[i])
		if not similarity:
			return False
	return True		
		
		



if __name__=='__main__':
	print ("Enter two tree_string, where tree string is a string showind the preorder traversal of the tree with markers to denote level. Eg, assume we have a tree with root node x and child nodes a and b, then the input string is as follows x(a)(b)")
	while True:
		print("===========================================")
		print("Please make sure that the first tree is larger than or equal to the second tree, If you want to stop the program enter None")
		first_tree_string=input("Enter first tree string \n")
		if first_tree_string=='None':
			break
		second_tree_string=input("Enter second tree string \n")
		first_tree=tree.Tree()
		second_tree=tree.Tree()
		first_tree.create_tree_prefix_string(first_tree_string)
		second_tree.create_tree_prefix_string(second_tree_string)
		print("Tree 2 is Subtree of Tree 1 : ",find_if_subtree(first_tree,second_tree))
		print ("===========================================")
		
		





