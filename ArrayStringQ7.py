'''
This is the final question in the array and string section. We are asked to check given two strings if the second string is a rotated version of the first.
For checking this we create a string which is a concatenation of the first string reversed and the first string. Then we check if the second string is a part of this new combo string.
'''


import numpy as np


def create_combo_string(str1):
	return str1+str1


def solve_using_new_string(str1,str2):
	rotation_str=create_combo_string(str1)
	print (rotation_str)
	return str2 in rotation_str

def solution(str1,str2):
	print ("The statement that the second string was a rotated version of the first string is {0}".format(solve_using_new_string(str1,str2)))
	



if __name__=="__main__":
	str_1=input("Enter string 1 \n")
	str_2=input("Enter string 2 \n")
	solution(str_1,str_2)
