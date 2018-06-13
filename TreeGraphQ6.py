'''
We are asked to find the first common anscestor of two nodes in a binary tree, We are going to do this as follows:
For each node , we check what the core is for left and right if the score is  for right. Where a score of 1 indicates one of the elements were found there and score of two indicate the other element has been found there. The common ancestor is the element for which there is a score of one for one of the child and one for the other child
'''
import ds.tree as tree


def LCA(sample_tree,first_node,second_node):
	value,score=find_LCA(sample_tree.root,first_node,second_node)
	if value:
		return value
	else :
		return "None"	

def find_LCA(current_node,first_node,second_node):
	#first we check score of left search
	return_score=0
	if current_node.value==first_node or current_node.value==second_node:
		return_score+=1
	if len(current_node.children)>0:	
		left_search_result=find_LCA(current_node.children[0],first_node,second_node)
		print("Current Node: {0} Left search result : {1}".format(current_node.value,left_search_result[1]))
		if left_search_result[0]:
			return left_search_result
		if return_score==1 and left_search_result[1]==1:
			return current_node.value,2
		return_score+=left_search_result[1]

	if len(current_node.children)>1:
		right_search_result=find_LCA(current_node.children[1],first_node,second_node)
		print("Current Node: {0} Right search result : {1}".format(current_node.value,right_search_result[1]))
		if right_search_result[0]:
			return right_search_result
		if return_score==1 and right_search_result[1]==1:
			return current_node.value,2
		
		return_score+=right_search_result[1]	
	if return_score==2:
		return current_node.value,2	
	return None,return_score



if __name__=="__main__":
	sample_tree=tree.Tree()
	print("Enter the string for creating the tree, the string has to be entered using postfix notation, as an example, suppose you want to have a tree x with two children a and b , then you can give the tree string as x(a)(b)")
	tree_string=input("Enter the tree string using the format said before\n")
	sample_tree.create_tree_prefix_string(tree_string)
	while True:	
		print ("=========================================")
		print("Now we fill find LCA of two nodes,type in None if you want to stop")
		first_node=input("Enter first node \n")
		if first_node=='None':
			break	
		second_node=input("Enter second Node \n")
		print("LCA is : ",LCA(sample_tree,first_node,second_node))
