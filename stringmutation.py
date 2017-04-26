#Read a given string, change the character at a given index and 
#then print the modified string.

# Enter your code here. Read input from STDIN. Print output to STDOUT
s = raw_input()
s_list = list(s)
ip = raw_input().split(" ")
if len(ip)== 2:
    i = int(ip[0])
    c = ip[1]
    s_list[i] = c
    s = "".join(s_list)
    print s