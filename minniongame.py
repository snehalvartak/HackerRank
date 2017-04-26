"""
Minnion Game
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
S = raw_input()
vowels = ['A','E','I','O','U']

kevin_cnt = 0
stuart_cnt = 0


for i in range(len(S)):
	if S[i] in vowels:
		kevin_cnt += (len(S) - i)
	else:
		stuart_cnt += (len(S) - i)
            
    if kevin_cnt > stuart_cnt:
        print "Kevin" , kevin_cnt
    elif stuart_cnt > kevin_cnt:
        print "Stuart" ,stuart_cnt
    else:
        print "Draw"