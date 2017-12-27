'''
The third question is as follows

Write a method to decide if two strings are anagrams or not.

We solve this by maintaining counts of letters in both strings and checking if they are equal, if they are they are anagrams. This can be implemented using a dictionary of byte array of size 26
'''
from collections import defaultdict

def hash_solution(str1,str2):
	dict1=defaultdict(int)
	dict2=defaultdict(int)
	if len(str1)==len(str2):
		for i,letter in enumerate(str1):
			dict1[letter]+=1
			dict2[str2[i]]+=1
		for key in dict1:
			if dict1[key]!=dict2[key]:
				return False
	else:
		return False

	return True



def solutions(str1,str2,method):
	if method=="hash_solution":
		check=hash_solution(str1,str2)

	if check:
		print("The string are anagrams")
	else:
		print("The strigs are not anagrams")

if __name__=="__main__":
	str1=input("Enter first string \n")
	str2=input("Enter second string \n")
	solutions(str1,str2,"hash_solution")