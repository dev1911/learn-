import json

class Problem():
	def __init__(self , path):
		self.path = path

	def load_problem(self):
		with open(self.path , "r") as f:
			self.__dict__.update(json.load(f))

	def display(self):
		print("----------------------------------------------------------")
		# print("Topic :",self.topic)
		print("Problem " , self.problem_no)
		print(self.question_text)
		print("Options")
		print("A :"+self.options["A"] , "\tB :"+self.options["B"], "\tC :"+self.options["C"] , "\tD :"+self.options["D"])		
		print("Difficulty :",self.difficulty)
		print("Threshold :",self.threshold)
		if "prerequisites" in self.__dict__.keys():
			print("Prerequisite questions :",self.prerequisites)
		print("----------------------------------------------------------")	

	def __str__(self):
		return "Question : " + self.question_text + " \n"

if __name__=="__main__":
	p = Problem("./problems/problem4.json")
	p.load_problem()
	p.display()
	# print(type(p.prerequisites))