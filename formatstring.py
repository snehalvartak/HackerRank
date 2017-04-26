"""
Read the integer, N and print the decimal, octal, hexadecimal,
and binary values from 1 to N with space padding so that all fields take the 
same width as the binary value.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
if N>= 1 and N <=99:
    for n in range(1,N+1):
        s = len("{0:b}".format(N))
        for base in 'doXb':
            print "{0:{width}{base}}".format(n,base = base, width = s),
        print
   