"""
You are given a string S and width w . 
Your task is to wrap the string into a paragraph of width w.
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
import textwrap
S= raw_input()
w = int(raw_input())

if len(S) > 0 and len(S)<1000 and w <len(S) and w> 0:
    print textwrap.fill(S,w)