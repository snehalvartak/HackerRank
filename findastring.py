"""
In this challenge, the user enters a string and a substring. You have to print 
the number of times that the substring occurs in the given string. 
String traversal will take place from left to right, not from right to left.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
S = raw_input()
sub = raw_input()
cnt = 0
i = 0
if len(S) > len(sub):
    while i < len(S):
        idx = S.find(sub,i,len(S))
        if idx != -1:
            cnt+=1
            i = idx + 1
        else:
            i+= 1
            
    print cnt
    