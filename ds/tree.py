'''
This is a class for creating a tree. We have two classes here the first is the binary tree while the second is the general tree. The binary tree has two childre both of which are trees. While a general tree has no bound on number of childre it can have
'''
#from stack import stack 
from . import stack
from enum import Enum

#class TreeType(Enum):
#	binary=1
#	general=2

class TreeSettings():
	verbose=1
	
class TreeNode():
	def __init__(self):
		self.value=None
		self.children=[]
		

class Tree():
	def __init__(self):
		self.root=None
		self.tree_depth=0
		self.tree_size=0
	
	def create_tree_prefix_string(self,tree_string,**kwargs):
		verbosity=kwargs.pop('verbose',None)
		
		current_pos=0
		process_stack=stack.stack()
		#string_stack=stack()
		if tree_string[0]=='(' or tree_string[0]==')':
			return
		self.root=TreeNode()
		current_node=self.root
		while current_pos<len(tree_string):
			if verbosity==TreeSettings.verbose:
				print('=======================================')
				print('Current char : ',tree_string[current_pos])
				print('=======================================')
			if tree_string[current_pos]=='(':

				if verbosity==TreeSettings.verbose:
					print('Pushed value : ',current_node.value)
				process_stack.push(current_node)
				new_node=TreeNode()
				current_node.children.append(new_node)
				current_node=new_node
			elif tree_string[current_pos]==')':
				current_node=process_stack.pop()
				
				if verbosity==TreeSettings.verbose:
					print('Popped Value : ',current_node.value)
			else:
				current_node.value=tree_string[current_pos]
				
				if verbosity==TreeSettings.verbose:
					print('Assingned value to node : ',current_node.value)
			current_pos+=1

			if verbosity==TreeSettings.verbose:
				print('\n\n')
	
def print_tree_prefix(current_node=None):
	if not current_node:
		print("Pass a tree with some nodes present")
		return

	print(current_node.value,end='')
	for child in current_node.children:
		print('(',end='')
		print_tree_prefix(child)
		print(')',end='')
			
			

if __name__=='__main__':
	sample_tree=Tree()
	string_tree='1(2(3)(4))(3(5)(6(7)))'
	#string_tree="1(2)(3)"
	sample_tree.create_tree_prefix_string(string_tree,verbose=TreeSettings.verbose)
	print_tree_prefix(sample_tree.root)
	print('\n')
