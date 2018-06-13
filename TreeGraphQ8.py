'''
In this question we are asked to print all paths of a tree that sums up to a particular value, we are going to maintain a list of all possible paths till that noder.
'''
import ds.tree as tree



def sum_paths(sample_tree,sum_req):
	print("Printing all paths that sum up to given value :")
	print_paths(sample_tree.root,sum_req,[],[])
	return

def print_path_list(path):
	for i,element in enumerate(path):
		print(element,end='')
		if not i==len(path)-1:
			print("->",end='')
	print('')
				

def print_paths(node,sum_req,paths_till_now_passed,sums_till_now_passed):
	paths_till_now=[x[:] for x in paths_till_now_passed]
	sums_till_now=sums_till_now_passed[:]
	current_value=int(node.value)
	if sum_req==current_value:
		print(current_value)
#	print("Current Node : {0}, Sums : {1}, Paths : {2}".format(current_value,sums_till_now,paths_till_now))	
	'''
	now we iterate through all possible paths and print the paths we need to check if the sum exceeds a particular value if it does it the path needs to be removed if it is equallt to the sum, the path needs to be printed, if it is less than the sum keep the path
	'''
	if not sum_req<current_value:
		paths_till_now.append([current_value])
		sums_till_now.append(current_value)
		j=0
		for i in range(len(paths_till_now)):
			if i==len(paths_till_now)-1:		
				sums_till_now[j]=sums_till_now[i]
				paths_till_now[j]=paths_till_now[i]	
				j+=1
				continue
			paths_till_now[i].append(current_value)
			sums_till_now[i]+=current_value
			if sums_till_now[i]>sum_req:
				continue
			else:
				if sums_till_now[i]==sum_req:
					print_path_list(paths_till_now[i])
			sums_till_now[j]=sums_till_now[i]
			paths_till_now[j]=paths_till_now[i][:]	
			j+=1
#		print("j value : ",j)
		sums_till_now=sums_till_now[:j]
		paths_till_now= paths_till_now[:j]	
	else:
		paths_till_now=[]
		sums_till_now=[]
#	print("Path : ",paths_till_now)	
	for child in node.children:
#		print("Before passing to child :{0}, Path Values :{1} , Current Value : {2} ".format(child.value,paths_till_now,current_value))
		print_paths(child,sum_req,paths_till_now[:],sums_till_now[:])
	



if __name__=="__main__":
	print("The aim of the program is to print all possile paths in a tree that sums up to a given value. Hence only enter integer values. Also when prompted for tree string enter the prefix string form as given in questions preceedint this question")
	while True:
		print("Enter None if you want to stop, when prompted for a tree string")
		sample_tree=tree.Tree()
		tree_string=input("Enter tree string \n ")
		if tree_string=='None':
			break
		sample_tree.create_tree_prefix_string(tree_string)
		sum_req=input("Sum for which you want the paths \n")
		sum_req=int(sum_req)
		sum_paths(sample_tree,sum_req)	













