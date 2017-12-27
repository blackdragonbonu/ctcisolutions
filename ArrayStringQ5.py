'''
This question asks us to rotate an image so i have added a sample image for showing directions

Problem statement

Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?


'''

import matplotlib.pyplot as plot
import numpy as np

image_location="resources/download.jpg"

def rotate_image(image):
	length,breadth,depth=image.shape
	new_image=np.zeros([breadth,length,depth])
	#new_image=np.copy(image)
	print(new_image.shape)
	for i in range(length//2+1):
		for j in range(breadth//2+1):
			new_image[breadth-j-1,i]=image[length-i-1,breadth-j-1]
			new_image[j,i]=image[length-i-1,j]
			new_image[breadth-j-1,length-i-1]=image[i,breadth-j-1]
			new_image[j,length-i-1]=image[i,j]
	plot.figure()
	plot.imshow(new_image/255)
	plot.show()
	plot.figure()
	plot.imshow(np.transpose(image,(1,0,2)))
	plot.show()

if __name__=="__main__":
	image=plot.imread(image_location)
	print(image.shape)
	plot.imshow(image)
	plot.show()	
	rotate_image(image)