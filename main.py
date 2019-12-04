import problem , topic , learner , test
problem_paths=[]
problem_folder = "./problems"
global_time =0 


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
	

# Main entry point of the script
def main():
	print("1. Enter 0 for manual time tracking\n2. Enter 1 for real time tracking")
	real_time = int(input())

	if real_time:
		pass
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

			

if __name__ == "__main__":
	main()



