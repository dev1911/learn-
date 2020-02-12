

class Topic():

	def __init__(self , name , problems , threshold=None):
		# overall threshold for the topic
		self.name = name
		self.problems = problems 
		if threshold:
			self.threshold = threshold
		
	def display(self):
		print("Topic Name :",self.name)
		print("Number of questions :",len(self.problems))	
		print("Threshold :" , self.threshold)

