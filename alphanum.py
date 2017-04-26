"""
You are given a string S. 
Your task is to find out if the string S contains: alphanumeric characters, 
alphabetical characters, digits, lowercase and uppercase characters.

Output Format
               
In the first line, print True if S has any alphanumeric characters. 
Otherwise, print False. 
In the second line, print True if S has any alphabetical characters. 
Otherwise, print False. 
In the third line, print True if S has any digits. Otherwise, print False. 
In the fourth line, print True if S has any lowercase characters. 
Otherwise, print False. 
In the fifth line, print True if S has any uppercase characters.
Otherwise, print False.
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
S = raw_input()

isalpha = False
isalnum = False
isdigit = False
l = 0
u = 0 

for i in range(len(S)):
    if S[i].isalpha() == True:
        isalpha = True
    if S[i].isalnum() == True:
        isalnum = True
    if S[i].isdigit() == True:
        isdigit = True
    if S[i].islower() == True:
        l = 1   
    if S[i].isupper() == True:
        u = 1

#IS ALPHANUMERIC
if isalnum == True:
    print "True"
else:
    print "False"
#IS ALPHABETIC
if isalpha == True:
    print "True"   
else:
    print "False"
#IS DIGIT
if isdigit == True:
    print "True"
else:
    print "False"
        
#IS LOWERCASE      
if l == 1:
    print "True"
else:
    print "False"
#IS UPPERCASE
if u == 1:
    print "True"
else:
    print "False"

