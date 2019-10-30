import os
from problem import Problem
class Test():

	def __init__(self):
		#wrapper for problems / topics
		pass

	#Construct test by specifying problems/problem folder
	def construct_test(self , paths=None , folder=None):
		if folder:
			for root,dir,files in os.walk(folder):
				print("Root :",root , "\tDir :",dir,"\tFiles :",files)
				problems = []
				for file in files:
					problems.append(Problem(os.path.join(root,file)))
			for prob in problems:
				prob.load_problem()
				prob.display()	
			self.problems = problems	

		else:
			for path in paths:
				problems=[]
				prob = Problem(path)
				prob.load_problem()
				problems.append(prob)
			for prob in problems:
				prob.display()
			self.problems = problems				



if __name__ == "__main__":
	test_ = Test()
	# test_.construct_test(folder="./problems")
	test_.construct_test(paths=["./problems/problem1.json" , "./problems/problem2.json"])					
