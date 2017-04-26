#Standardize Mobile Number Using Decorators

#CONCEPT :
"""Like most other programming languages, Python has the concept of closures. 
Extending these closures gives us decorators, which are an invaluable asset. 
You can learn about decorators in 12 easy steps here.
To solve the above question, make a list of the mobile numbers and pass it 
to a function that sorts the array in ascending order. 
Make a decorator that standardizes the mobile numbers and apply it to 
the function."""

#PROBLEM
"""You are given N mobile numbers. Sort them in ascending order then
print them in the standard format shown below:
	+91 xxxxx xxxxx
The given mobile numbers may have +91 ,91  or 0  written before the actual 
10 digit number. Alternatively, there may not be any prefix at all. 

Sample Input 
3
07895462130
919875641230
9195969878

Sample Output:
+91 78954 62130
+91 91959 69878
+91 98756 41230
"""	

# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(raw_input())
phone_dir = []
for n in range(N):
    num = raw_input()
    if len(num) > 10:
        num = num[-10:]
    phone_dir.append(num)

def format_num(phone):
    return "+91 "+phone[:-5] +" " + phone[-5:]

dir_sorted = sorted(phone_dir )

for n in range(N):
    print format_num(dir_sorted[n])
    

    

