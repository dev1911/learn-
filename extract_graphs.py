import argparse
import re
from decimal import *
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file" , help="Input file path")
    parser.add_argument("-o" , "--output_folder" , help="Output folder path")

    args = parser.parse_args()
    score = [[] for i in range(20)]
    decay_rates = [[] for i in range(20)]
    time_elapsed = [[] for i in range(20)]
    review_events = [[] for i in range(20)]
    question_queue = [[] for i in range(20)]
    regex = re.compile(r'\d+')
    i = 0
    j = 0
    k = 0
    s = 0
    b = 0
    with open(args.input_file) as input_file:
        session_id = regex.search(args.input_file).group(0)
        print(session_id)
        for line in input_file:
            # if re.search("-------" , line):
            if(re.search("Scores",line)):
                # while(re.search("Decay rates",line)):
                score[i].append(line[8:])
                i = i+1
            elif(re.search("Decay rates",line)):
                decay_rates[j].append(line[12:])
                j = j+1
            elif(re.search("Time elapsed",line)):
                time_elapsed[k].append(line[13:])   
                k = k+1
            elif(re.search("Review events",line)):
                review_events[s].append(line[14:])                
                s = s+1
            elif(re.search("Review Queue",line)):
                question_queue[b].append(line[13:])
                b = b+1
        print("---Scores---")
        l=[]
        for i in range(len(score)):
            for j in range(len(score[i])):
                score[i][j] = score[i][j].rstrip("\n").lstrip(" ").lstrip('[').rstrip(']')
                l = [float(k) for k in score[i][j].split(',')]
            score[i] = l
        print(score)
        print("---Decay Rates---")
        l=[]
        for i in range(len(decay_rates)):
            for j in range(len(decay_rates[i])):
                l=[]
                decay_rates[i][j] = decay_rates[i][j].rstrip("\n").lstrip(" ").lstrip('[').rstrip(']')
                for k in decay_rates[i][j].split(','):
                    l.append(float(k))
            decay_rates[i] = l
        print(decay_rates)
        print("---Time Elapsed---")
        l=[]
        for i in range(len(time_elapsed)):
            for j in range(len(time_elapsed[i])):
                l=[]
                time_elapsed[i][j] = time_elapsed[i][j].rstrip("\n").lstrip(" ").lstrip('[').rstrip(']')
                # l = [k for k in time_elapsed[i][j].split(',')] #Decimal(k)
                for k in time_elapsed[i][j].split(','):
                    if k =='':
                        l.append(k)
                    else:
                        l.append(float(k))
            time_elapsed[i] = l
        print(time_elapsed)
        print("---Question Queue---")
        l=[]
        # print(question_queue)
        for i in range(len(question_queue)):
            for j in range(len(question_queue[i])):
                question_queue[i][j] = question_queue[i][j].rstrip("\n").lstrip(" ").lstrip('[').rstrip(']')
                if(question_queue[i][j]!=''):
                    l = [int(k) for k in question_queue[i][j].split(',') ]
                else:
                    l = []
            question_queue[i]= l
        print(question_queue)
        print("---Review Events---")
        l=[]
        for i in range(len(review_events)):
            for j in range(len(review_events[i])):
                review_events[i][j] = review_events[i][j].rstrip("\n").lstrip(" ").lstrip('[').rstrip(']')
                l = [float(k) for k in review_events[i][j].split(',')]
            review_events[i] = l 
        print(review_events)

