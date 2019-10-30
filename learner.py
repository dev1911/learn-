import matplotlib.pyplot as plt
import numpy as np
# Model the student here

class Learner():

	def __init__(self):
		#learner attributes
		#scores for questions / topics
		#decay rates for questions/topics
		#review queue
		self.problems_list = []
		self.curr_question = 0
		pass

	def calculate_score(self , problem , correct , time):
		pass

	def update_scores(self):
		pass

	def calculate_overall_score(self):
		pass

	def show_graph(self):
		pass	

	def to_be_reviewed(self):
		pass

	def update_probability(self):
		pass	

	def next_question(self):
		review = self.to_be_reviewed()
		if review:
			return review_queue[0]
		else:
			ret_prob =  self.problems_list[self.curr_question]
			self.curr_question+=1
			return ret_prob


#calculate decay rates
#calculate/update scores for each question/topic
#calculate overall score for each topic i.e. calculate metric
#function to decide occurence of review event with some probability
#function to calculate/update the probability
# display graphs of scores		
#function to display current progress/score/details