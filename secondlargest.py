"""You are given N numbers. Store them in a list and find the second 
largest number.

Constraints:
2 <= N <= 100
-100 <= A[i] <= 100

NOTE: Do not use the insertion sort method.

""" 

# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(raw_input())
A = list(map(int, raw_input().split()))

if N >= 2 and N<= 10 and len(A)<=100:
    desc = sorted(A, reverse = True)
    max_desc = desc[0]
    cnt = A.count(max_desc)
    if cnt > 1:
        print desc[cnt]
            
    else:
        print desc[1]