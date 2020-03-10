import problem , topic , learner , test , realtime
import threading
import time
from timeloop import Timeloop
from datetime import timedelta
problem_paths=[]
problem_folder = "./problems"
global_time =0 
time_interval = 0.5

print("1. Enter 0 for manual time tracking\n2. Enter 1 for real time tracking")
real_time = int(input())
if real_time:
	time_interval = float(input("Enter time interval :"))

tl = Timeloop()
test_ = test.Test()
test_.construct_test(folder=problem_folder)
test_.generate_graph()
test_.display_adj_matrix()
student = learner.Learner(test_)
# f = open("log.txt","w+")
def start_loop():
	"""
	Callback
	"""
	global global_time
	print("Start of time :",global_time)
	

def end_loop():
	"""
	Callback
	"""
	global global_time
	global_time+=1
	# print("Global Time :",global_time)
	

@tl.job(interval = timedelta(seconds = time_interval))
def callback():
	# print(".")
	global student
	student.increment_time(time_interval = time_interval)
	# print(student.scores)

# Main entry point of the script
def main():
	
	global student
	if real_time:
		global time_interval
		global student		

		print("Enter 'A','B','C','D' to answer a question\nEnter 'start' to start :" ) 
		ip = input("Enter input :")
		if ip == "start":
			tl.start() # Start a new job
		while True:
			curr_prob = student.next_question()
			if curr_prob:
				curr_prob.display()
				question_start_time = time.time()
				ip = input("Enter answer :")
				question_end_time = time.time()
				question_time = question_end_time - question_start_time
				# f.write("Question answered\n")
				student.answer(curr_prob , ip , question_time)

			else:
				print("Test completed")
				tl.stop()  # Stop the job
				for i in range(student.no_of_problems):
					student.show_question_graph(i , save=True , display=False)
					student.show_decay_rate_graph(i , save=True , display=False)
					# student.show_time_graph(i , save=True , display=False)
					# student.show_no_of_review_events_graph(i , save=True , display=False)

				student.show_overall_score_graph()	
				break
			# print("Scores")
			# print(student.__dict__)
			print(list(student.scores))
			# print(student.display_review_queue())
			


	else:
		# Time is tracked here.
		question_time=0
		global global_time
		#Initialise test
		test_ = test.Test()
		test_.construct_test(folder=problem_folder)

		#Initialise learner session
		student = learner.Learner(test_) 
		print("-----------INITIAL-------------")
		student.display_state()
		#main time loop
		print("Press 'n' to advance one time step\nPress 'A','B','C','D' to answer a question\nPress anyother button to start:" ) 
		while True:
			start_loop()
			ip = input("Input :")
			if ip == "n":
				print("Advancing one time step ")
				global_time+=1
				question_time+=1
				student.increment_time()

			elif ip=="A" or ip=="B" or ip=="C" or ip=="D":
				student.answer(curr_prob,ip,question_time)
				question_time+=1
				student.increment_time()

				curr_prob = student.next_question()
				if curr_prob:
					curr_prob.display()
					question_time=0
				else:
					print("Test completed!!")
					break

			elif ip == "curr":
				curr_prob.display()
				continue
			
			elif ip == "show":
				ip_ = input("Enter entity to display ")
				if ip_ == "score":
					student.show_overall_score_graph()
				else:
					student.show_question_graph(int(ip_))			

			elif ip == "start":
				curr_prob = student.next_question()
				student.increment_time()
				if curr_prob:
					curr_prob.display()
					question_time=0
				else:
					print("Test completed!!")
					break	
	
			elif ip == "exit":
				break				

			
			print("SCORE HISTORY")
			# student.show_score_history()
			print(student.score_history[-1])
			# print("CURRENT QUESTION TIME ",question_time)
			# print("GLOBAL TIME ",global_time)
			end_loop()

		student.show_overall_score_graph()
		for i in range(student.no_of_problems):
			student.show_question_graph(i)
			

if __name__ == "__main__":
	main()


