import threading
import time
from threading import  Timer
import test , learner
import numpy as np
problem_folder = "./problems"

class UpdateThread(threading.Thread):
    def __init__(self , time_interval , student):
        threading.Thread.__init__(self)
        self.time_interval = time_interval
        self.student = student

    def run(self):
        print("Thread executing")
        
        while True:
            t = Timer(self.time_interval , self.update)
            t.start()    
            t.join()
            print(threading.active_count())

    def update(self):
        self.student.decay_scores(time_step = self.time_interval)		
        self.student.score_history.append(list(self.student.scores))
        self.student.check_scores()
        self.student.update_review_queue()		
        self.student.update_probability()
        self.student.display_state()
        


if __name__ == "__main__":
    test_ = test.Test()
    test_.construct_test(folder=problem_folder)
    student = learner.Learner(test_)
    student.scores = np.array([10,10,10,10,10,10,10,10,10])
    student.decay_rates = np.array([0.1,0.2,0.3,0.4,0.2,0.6,0.1,0.9,0.1])
    update_thread = UpdateThread( 1 , student)
    update_thread.start()