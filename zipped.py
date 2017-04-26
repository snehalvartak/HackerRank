"""
The National University conducts an examination of N students in X subjects. 
Your task is to compute the average scores of each student.
The format for the general mark sheet is:

Student ID  ___1_____2_____3_____4_____5__               
Subject 1   |  89    90    78    93    80
Subject 2   |  90    91    85    88    86  
Subject 3   |  91    92    83    89    90.5
            |______________________________
Average        90    91    82    90    85.5 

"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
ip = list(map(int ,raw_input().split()))
if len(ip) == 2:
    N = ip[0]
    X = ip[1]
    subj = []
    if N > 0 and N<=100 and X>0 and X <=100:
        for x in range(X):
            temp = list(map(float,raw_input().split()))
            subj.append(temp)
        subj_zip = zip(*subj)
        for y in range(len(subj_zip)):
            mrks = subj_zip[y]
            print sum(mrks)/len(mrks)
        
    


        
    

