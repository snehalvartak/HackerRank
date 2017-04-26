#Task 

"""Initialize your list (L = []) and follow the N commands given over N lines.
Each command will be 1 of the 8 commands given above. 
The extend(L) method will not be used. 
Each command will have its own value(s) separated by a space."""

#PROBLEM

"""Input Format

The first line contains an integer,N  (the number of commands). 
The N subsequent lines each contain one of the 8 commands described above.

Sample Input
12
insert 0 5
insert 1 10
insert 0 6
print 
remove 6
append 9
append 1
sort 
print
pop
reverse
print

Sample Output
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
L = []
N = int(raw_input())
for n in range(N):
    cmd = raw_input().split(" ")
  
    if cmd[0].lower() == "insert":
        L.insert(int(cmd[1]),int(cmd[2]))
    elif cmd[0].lower() == "append":
        L.append(int(cmd[1]))
    elif cmd[0].lower() == "remove":
        L.remove(int(cmd[1]))
    elif cmd[0].lower() == "pop":
        if len(cmd) >1:
            L.pop([int(cmd[1])])
        else:
            L.pop()
    elif cmd[0].lower() == "index":
        L.index(int(cmd[1]))
    elif cmd[0].lower() == "count":
        L.count(int(cmd[1]))
    elif cmd[0].lower() == "sort":
        L.sort()
    elif cmd[0].lower() == "reverse":
        L.reverse()
    elif cmd[0].lower() == "print":
        print L
     
    

