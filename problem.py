import json

class Problem():
	def __init__(self , path):
		# problem properties
		# difficulty
		# problem text
		# problem options
		# correct answer
		# probelm path
		self.path = path
		# self.load_problem()
		pass

	def load_problem(self):
		
		with open(self.path , "r") as f:
			self.__dict__.update(json.load(f))
			# print(self.__dict__)

	def display(self):
		print("----------------------------------------------------------")
		print("Difficulty :",self.difficulty)
		print("Threshold :",self.threshold)
		print("Topic :",self.topic)
		print(self.question_text)
		print("Options")
		print("A :"+self.options["A"] , "\tB :"+self.options["B"], "\tC :"+self.options["C"] , "\tD :"+self.options["D"])		
		print("----------------------------------------------------------")	
# load problem from file.
#display problem
# display details of problem		

if __name__=="__main__":
	p = Problem("./problems/problem1.json")
	p.load_problem()
	p.display()