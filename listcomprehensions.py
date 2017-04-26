"""You are given three integers X,Y and Z representing the dimensions of a cuboid. 
You have to print a list of all possible coordinates on a 3D grid where 
the sum of Xi+Yi+Zi is not equal to N. If X=2, the possible values of Xi can be 
0,1  and 2. 
The same applies to Y and Z.

#Print the list in lexicographic increasing order.

# Enter your code here. Read input from STDIN. Print output to STDOUT

    
X = int(raw_input())
Y = int(raw_input())
Z = int(raw_input())
N = int(raw_input())

coor_lis = [[a,b,c] for a in range(X+1) for b in range(Y+1) for c in range(Z+1) if a+b+c != N]
print coor_lis
