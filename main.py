import problem , topic , learner , test
problem_paths=[]
problem_folder = "./problems"
global_time=0
def start_loop():
	"""
	Callback
	"""
	pass

def end_loop():
	"""
	Callback
	"""
	print("Global Time :",global_time)
	pass	

# Main entry point of the script
def main():
	print("1. Enter 0 for manual time tracking\n2. Enter 1 for real time tracking")
	real_time = int(input())

	if real_time:
		pass
	else:	
		# Time is tracked here.
		question_time=0
		#Initialise test
		test_ = test.Test()
		test_.construct_test(problem_folder)

		#Initialise learner session
		student = learner.Learner() 
		#main time loop 
		while True:
			start_loop()
			ip = input()
			if ip == "n":
				global_time+=1
				question_time+=1
				continue
			elif ip == "a":
				if curr_prob.answer == "A":
					pass
				else:
					pass	
			elif ip == "b":
				if curr_prob.answer == "B":
					pass
				else:
					pass	
			elif ip == "c":
				if curr_prob.answer == "C":
					pass
				else:
					pass	
			elif ip == "d":
				if curr_prob.answer == "D":
					pass
				else:
					pass					
			else:
				curr_prob = student.next_question()
				curr_prob.display()
				question_time=0


			end_loop()


if __name__ == "__main__":
	main()



