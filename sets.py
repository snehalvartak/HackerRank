
"""Task 
Given 2 sets of integers, M and N, print their symmetric difference 
in ascending order. The term symmetric difference indicates those
values that exist in either M or N but do not exist in both.

Input Format

The first line of input contains an integer, M. 
The second line contains M  space-separated integers. 
The third line contains an integer,N . 
The fourth line contains N space-separated integers.

Output Format

Output the symmetric difference integers in ascending order, one per line.
"""



# Enter your code here. Read input from STDIN. Print output to STDOUT

M = int(raw_input())
m_list = list(map(int,raw_input().split()))
N = int(raw_input())
n_list = list(map(int,raw_input().split()))

m_set = set(m_list)
n_set = set(n_list)

m_n_union = m_set.union(n_set)
m_n_inter = m_set.intersection(n_set)

m_n_sym_dif = m_n_union.difference(m_n_inter)
sym_diff_ls = sorted(list(m_n_sym_dif))
if len(sym_diff_ls)>0:
    for n in range(len(sym_diff_ls)):
        print sym_diff_ls[n]