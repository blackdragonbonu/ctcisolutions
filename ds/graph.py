'''
We try to create a graph , we create the graph by specifying a child node and at the same time how to proceed further with it. A node in graph has three fields, first is the node id which uniquely identifies,unless specified otherwise this is the same as the value, the second element in the node is the value of the node, the third element is the descendants of the  node
'''
from enum import Enum


class GraphNode():
	def __init__(self):
		self._id=None
		self.value=None
		self.children=[]

	def _initialize(self,value):
		self.value=value


class Graph():
	def __init__(self):
		#nodes list is a dictionary of all nodes in the graph
		self.nodes_dict={}
		self.nodes_list=[]
		self.start_node=None
	
	def add_node(self,node_value):
		new_node=GraphNode()
		new_node._initialize(node_value)	
		self.nodes_dict[node_value]=new_node
		self.nodes_list.append(node_value)

	def add_children(self,node,children):
		_node=self.nodes_dict[node]
		for child in children:
			if child in self.nodes_list:
				child_node=self.nodes_dict[child]
				_node.children.append(child_node)
	
	def _initialize_graph(self):
		while True:	
			value=input('Enter the nodes for the graph , Enter None if you want to end \n')
			if value=='None':
				break
			self.add_node(value)
		for node in self.nodes_list:
			children=input("Enter the children for : {} \n values seperated by , \n".format(node))
			children=children.split(',')	
			self.add_children(node,children)
			
if __name__=='__main__':
	sample_graph=Graph()
	sample_graph._initialize_graph()

 




