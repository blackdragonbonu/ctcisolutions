
class Queue():
	def __init__(self):	
		self.size=0
		self.top=None
		self.data=[]

	def push(self,data):
		if not data:
			try :
				raise ValueError("Should supply an integer or string, but was supplied None")
			except ValueError:
				print ("Exception encountered")
		self.size+=1
		self.data.append(data)
		return data
		
	def pop(self):
		if self.size==0:
			try :
				raise Exception("Underflow error")
			except ValueError:
				print("Under flow Exception")
		
		self.size-=1
		popped_value=self.data[0]
		self.data=self.data[1:]
		return popped_value

	def peek(self):
		if self.size==0:
			print ("Empty stack")
			return None
		else :
			return self.data[0]

if __name__=='__main__':
	sample_queue=Queue()
	sample_queue.push(2)
	sample_queue.pop()
	sample_queue.pop()
	sample_queue.pop()
