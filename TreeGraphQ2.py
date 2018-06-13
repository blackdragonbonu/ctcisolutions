import ds.graph as graph
import ds.stack as stack
import ds.queue as queue
from enum import Enum



def SearchMethod(Enum):
	bfs=1
	dfs=2


def bfs(current_graph,first_node,second_node):
	start_node=current_graph.nodes_dict[first_node]
	destination_node=current_graph.nodes_dict[second_node]
	process_queue=queue.Queue()
	process_queue.push(start_node)
	seen_nodes={}
	while True:
		if process_queue.size==0:
			return False
		current_node=process_queue.pop()
		seen_nodes[current_node.value]=1
		for child in current_node.children:
			if not seen_nodes.get(child.value,0):
				process_queue.push(child)
		if current_node==destination_node:
			return True
	


def dfs(current_graph,first_node,second_node):
	start_node=current_graph.nodes_dict[first_node]
	destination_node=current_graph.nodes_dict[second_node]
	process_stack=stack.stack()
	process_stack.push(start_node)
	seen_nodes={}
	while True:
		if process_stack.size==0:
			return False
		current_node=process_stack.pop()
		seen_nodes[current_node.value]=1
		for child in current_node.children:
			if not seen_nodes.get(child.value,0):
				process_stack.push(child)
		if current_node==destination_node:
			return True


if __name__=='__main__':
	sample_graph=graph.Graph()
	sample_graph._initialize_graph()	
	print("We now try to find if there is a path between to nodes")
	print("Type quit() when promted for first node to exit program")
	while True:
		print("=======================================")
		first_node=input("Enter first node \n")
		if first_node=='quit()':
			break
		second_node=input("Enter second node \n")
		search_method=input("Enter the search method \n 1.bfs\n 2.dfs\n")
		
		if search_method=='bfs':
			print("Path present : ",bfs(sample_graph,first_node,second_node))
		elif search_method=='dfs':
			print("Path present : ",dfs(sample_graph,first_node,second_node))
		else:
			print("Invalid input")
		print("========================================")















