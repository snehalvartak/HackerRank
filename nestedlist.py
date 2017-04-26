"""Given the names and grades for each student in a Physics class of N
students, store them in a nested list and print the name(s) of any student(s)
having the second lowest grade.

2<=N<=5
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
def k(j):
    return j[1]
N = int(raw_input())
l = []
if N >= 2 and N <=5:
    for i in range(N):
        name = raw_input()
        mrks = float(raw_input())
        l.append([name,mrks])
sorted_l = sorted(l , key = k)
lowest = sorted_l[0][1]

filter_1 = [[a,b] for a,b in sorted_l if b > lowest]
filter_2 = sorted([[a,b] for a,b in filter_1 if b == filter_1[0][1]])

for l in range(len(filter_2)):
    print filter_2[l][0]
