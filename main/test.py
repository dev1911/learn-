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
				# print("Root :",root , "\tDir :",dir,"\tFiles :",files)
				problems = []
				for file in files:
					problems.append(Problem(os.path.join(root,file)))
			for prob in problems:
				prob.load_problem()
				# prob.display()	
			self.problems = problems	

		else:
			for path in paths:
				problems=[]
				prob = Problem(path)
				prob.load_problem()
				problems.append(prob)
			# for prob in problems:
			# 	prob.display()
			self.problems = problems				

	def generate_graph(self):
		self.adj_matrix = [[0 for i in range(len(self.problems))] for j in range(len(self.problems))]
		for prob in self.problems:
			if "prerequisites" in prob.__dict__.keys():
				idx = 0
				for p in prob.prerequisites:
					self.adj_matrix[prob.problem_no - 1][p - 1] = prob.prerequisite_weights[idx]
					idx+=1 

	def display_adj_matrix(self):
		for i in range(len(self.problems)):
			print(self.adj_matrix[i])

if __name__ == "__main__":
	test_ = Test()
	test_.construct_test(folder="./problems")
	test_.generate_graph()
	test_.display_adj_matrix()
	# print(test_.adj_matrix)
	# test_.construct_test(paths=["./problems/problem1.json" , "./problems/problem2.json"])		
	# print(test_.__dict__)	
	# for q in test_.problems:
	# 	print(q)		
