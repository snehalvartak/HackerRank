"""You are given a string S. Your task is to swap cases. 
In other words, convert all lowercase letters to uppercase letters 
and vice versa.

Example:
Www.HackerRank.com ==> wWW.hACKERrANK.COM
Pythonist 2 ==> pYTHONIST 2

"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
S = raw_input()
s = ""
if len(S)>0 and len(s)<=1000:
    for i in range(len(S)):
        if S[i] == S[i].lower():
            s+= S[i].upper()
        else:
            s+= S[i].lower()
    print s