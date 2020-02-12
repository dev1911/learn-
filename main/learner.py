import matplotlib.pyplot as plt
import numpy as np
import test
# Model the student here
score_constant = 50

class Learner():

	def __init__(self , test):
		self.problems_list = test.problems
		self.no_of_problems = len(self.problems_list)

		self.scores = np.zeros(shape = self.no_of_problems , dtype=float)
		self.decay_rates = np.zeros(shape = self.no_of_problems , dtype=float) 
		self.times = np.zeros(shape = self.no_of_problems , dtype=float)
		self.no_review_events = np.zeros(shape = self.no_of_problems)
		
		self.latest_question_index = -1
		self.curr_question_index = -1
		self.review_queue = []

		self.score_history = []
		self.decay_rate_history = []
		self.time_history = []
		self.no_review_events_history = []
		
		self.probability = 1
		self.overall_score = 0

	#TODO correct formula
	def calculate_score(self , problem , correct , time):
		"""
		Calculates score for a given problem and response
		score = problem.difficulty / time
		
		Parameters:
		problem : type:Problem
		correct : bool   0 for wrong answer. otherwise 1 
		time    : float   Time required to answer the question

		Returns:
		score : float
		"""
		if time == 0:
			time = 1
		if correct == 0:
			score = 20
		else:
			score = score_constant * problem.difficulty / time

		return score	

	#TODO correct formula
	def calculate_decay_rate(self , score , no_of_event):
		"""
		Calculates decay rate based on score and no of review events occured
		decay_rate = 1 / (score * no_of_event)

		Parameters:
		score : Score for a question
		no_of_event : Number of review events already occured

		Returns:
		decay_rate : float
		"""
		if no_of_event == 0:
			no_of_event = 1
		decay_rate = 1 / (score * no_of_event)
		return decay_rate


	def update_score(self , index , score):
		"""
		Updates score vector 

		Parameters:
		index : Index of question
		score : Score to be updated
		"""
		self.scores[index] = score
		self.times[index] = 0

	def update_decay_rate(self,index,decay_rate,alpha):
		"""
		Updates Decay rate vector

		Parameters:
		index : Index of question
		decay_rate : Decay rate to be updated
		alpha : Ratio of new decay_rate/old decay rate 
		"""
		# self.decay_rates[index] = decay_rate
		temp = self.decay_rates[index]
		self.decay_rates[index] = alpha * temp + (1-alpha)*decay_rate

	def update_review_queue(self):
		"""
		Updates the review queue with new prioritites for questions
		"""
		# print("Updating review queue")
		self.review_queue.sort(key=lambda x:self.scores[x[1]] - self.problems_list[x[1]].threshold)
		for i in range(len(self.review_queue)):
			if self.scores[self.review_queue[i][1]] > self.problems_list[self.review_queue[i][1]].threshold:
				self.review_queue.pop(i)

	def decay_scores(self , time_step = 1):
		"""
		Decays score vector exponentially
		"""
		# print("Decaying scores")
		# self.lambda_time_product = self.decay_rates * self.times
		for i in range(self.no_of_problems):
			if self.scores[i] == 0:
				continue
			else:
				self.scores[i] = self.scores[i] * np.exp(-1*self.decay_rates * time_step)[i]

	def check_scores(self):
		"""
		Checks for any question with score below its threshold
		"""
		for i in range(self.latest_question_index+1):
			if self.scores[i] < self.problems_list[i].threshold and self.scores[i]!=0:
				# print("Problem ", i , " to be added to review queue")
				self.add_to_review_queue(self.problems_list[i] , i)

	def add_to_review_queue(self , problem , index):
		"""
		Adds a question to the review queue
		"""
		if (problem,index) not in self.review_queue:
			# print("New problem entered in review queue")
			self.review_queue.append((problem , index))

	def increment_time(self , time_interval = 1):
		"""
		Takes one time step

		Increments time of a question if score and decay rate are not 0.
		Decays scores of all questions
		Checks scores of questions and adds question to review queue if score is below threshold
		Updates priorities of questions in review queue
		"""
		# print("*********** TIME INCREMENT ***************")
		for i in range(self.no_of_problems):
			if self.scores[i]==0 and self.decay_rates[i]==0:
				continue
			else:
				self.times[i] += time_interval
		self.decay_scores(time_step = time_interval)		

		self.score_history.append(list(self.scores))
		self.decay_rate_history.append(list(self.decay_rates))
		self.time_history.append(list(self.times))
		self.no_review_events_history.append(self.no_review_events)
		
		self.check_scores()
		self.update_review_queue()		
		self.update_probability()
		# self.display_state()

	def calculate_overall_score(self):
		"""
		Calculates overall score of a student
		Mathematically it is just the sum of individual scores at different time points
		"""
		self.overall_score = sum(self.score_history)

	def show_overall_score_graph(self , save=False , display=True):
		"""
		Shows a graph of overall score at different time points
		"""
		values = []
		fig = plt.figure()
		for i in range(len(self.score_history)):
			
			values.append(np.sum(self.score_history[:i]))
		# print(values)
		plt.plot(values)
		if save:
			fig.savefig("./graphs/overall_score.png")
		if display:	
			plt.show()	

	def to_be_reviewed(self):
		"""
		Outputs whether a review event should occur or not , based on a probability
		"""
		if self.latest_question_index >= self.no_of_problems - 1:
			return 1
		if len(self.review_queue) == 0:
			return 0
		random_int = np.random.random()
		if random_int > self.probability:
			return 0
		else:
			return 1	

	def display_review_queue(self):
		queue = []
		for problem in self.review_queue:
			queue.append(problem[1]+1)
		print(queue)	
		# return queue

	#TODO 
	def update_probability(self):
		"""
		Function to dynamically adjust the probability of occurence of a review event
		"""
		self.probability = 0.5

	def next_question(self):
		"""
		Gives next question 

		Checks if review event is to be scheduled and returns appropriate question 
		"""
		# print("Learner next question ")

		if self.latest_question_index >= self.no_of_problems - 1 and len(self.review_queue) == 0:
			return None

		elif self.latest_question_index >= self.no_of_problems - 1 and len(self.review_queue)!=0:
			prob = self.review_queue[0]
			self.curr_question_index = prob[1]
			self.no_review_events[self.curr_question_index] += 1
			self.review_queue.pop(0)		
			return prob[0]
		else:	
			review = self.to_be_reviewed()
			if review:
				prob = self.review_queue[0]
				self.curr_question_index = prob[1]
				self.no_review_events[self.curr_question_index] += 1
				self.review_queue.pop(0)		
				return prob[0]		
			else:
				# print("Current problem index : ",self.curr_question)
				# print("Current problem list : ", self.problems_list)
				if self.latest_question_index > len(self.problems_list):
					print("Test completed !")
					return None
				self.latest_question_index = (self.latest_question_index + 1 )
				self.curr_question_index = self.latest_question_index
				ret_prob =  self.problems_list[self.latest_question_index]

				return ret_prob
	
	def display_state(self):
		print("Current question ",self.latest_question_index)
		print("Active question ",self.curr_question_index)
		print("Scores \n",self.scores)
		print("Decay rates \n",self.decay_rates)
		print("Time elapsed \n",self.times)
		print("Review events\n",self.no_review_events)
		print("Review queue \n",self.review_queue)

	def answer(self , problem , ans , time):
		"""
		Updates scores and decay rates based on a response

		Parameters:
		problem : Problem which is answered
		ans     : Response given
		time    : Response time
		"""
		if ans == problem.answer:
			score = self.calculate_score(problem,1,time)
			print("Correct answer!")
		else:
			score = self.calculate_score(problem,0,time)
			print("Wrong answer!")
		decay_rate = self.calculate_decay_rate(score,self.no_review_events[self.curr_question_index])
		self.update_score(self.curr_question_index , score)
		self.update_decay_rate(self.curr_question_index , decay_rate , 0)
		self.times[self.curr_question_index] = 0
				
	def show_score_history(self):
		print(self.score_history)			

	def show_question_graph(self , index ,save=False , display=True):
		"""
		Shows graph of scores of a single question

		Parameters:
		index : index fo the question in the problem list
		"""
		values=[]
		fig = plt.figure()
		for i in range(len(self.score_history)):
			values.append(self.score_history[i][index])
		plt.axhline(y=self.problems_list[index].threshold)
		plt.plot(values)

		if save:
			fig.savefig("./graphs/question_{}.png".format(index))
		if display:	
			plt.show()

	def show_decay_rate_graph(self , index ,save=False , display=True):
		"""
		Shows graph of scores of a single question

		Parameters:
		index : index fo the question in the problem list
		"""
		values=[]
		fig = plt.figure()
		for i in range(len(self.decay_rate_history)):
			values.append(self.decay_rate_history[i][index])
		# plt.axhline(y=self.problems_list[index].threshold)
		plt.plot(values)

		if save:
			fig.savefig("./graphs/decay_rate_{}.png".format(index))
		if display:	
			plt.show()

	def show_time_graph(self , index ,save=False , display=True):
		"""
		Shows graph of scores of a single question

		Parameters:
		index : index fo the question in the problem list
		"""
		values=[]
		fig = plt.figure()
		for i in range(len(self.time_history)):
			values.append(self.time_history[i][index])
		# plt.axhline(y=self.problems_list[index].threshold)
		plt.plot(values)

		if save:
			fig.savefig("./graphs/time_{}.png".format(index))
		if display:	
			plt.show()

	def show_no_of_review_events_graph(self , index ,save=False , display=True):
		"""
		Shows graph of scores of a single question

		Parameters:
		index : index fo the question in the problem list
		"""
		values=[]
		fig = plt.figure()
		for i in range(len(self.no_review_events_history)):
			values.append(self.no_review_events_history[i][index])
		# plt.axhline(y=self.problems_list[index].threshold)
		plt.plot(values)

		if save:
			fig.savefig("./graphs/no_of_review_event_{}.png".format(index))
		if display:	
			plt.show()			

if __name__ == "__main__":
	test_ = test.Test()
	test_.construct_test(folder="./problems")	
	student = Learner(test_)
	# print("Problem")
	
	########## Simulation test ##################
	test_.problems[0].display()
	student.curr_question_index=0
	student.answer(test_.problems[0],"D",10)
	student.latest_question_index+=1
	student.curr_question_index+=1
	
	student.increment_time()
	student.display_state()
	
	test_.problems[1].display()
	student.answer(test_.problems[1],"B",1)
	student.latest_question_index+=1

	student.increment_time()
	student.display_state()
	
	student.increment_time()
	student.display_state()

	student.increment_time()
	student.display_state()