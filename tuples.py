"""Task 
You are given an integer,N , on a single line. 
The next line contains N space-separated integers. Create a tuple,T , of 
those N integers, then compute and print the result of hash(T).

Note: hash() is one of the functions in the __builtins__ module.

Input Format

The first line contains an integer, N (the number of elements in the tuple). 
The second line contains N space-separated integers describing T.

Output Format

Print the result of hash(T).
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
N= int(raw_input())
lt = []
ip = raw_input().split(" ")
if len(ip) == N:
    for i in range(N):
        ip[i] =int(ip[i])
    tup = tuple(ip)
    print hash(tup)
