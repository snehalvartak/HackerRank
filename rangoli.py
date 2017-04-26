"""You are given an integer,N . 
Your task is to print an alphabet rangoli of size N. 
(Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:
#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

"""

import string

N = int(input())
alphabet = string.ascii_lowercase

for i in range(N - 1, 0, -1):
    row = ["-"] * (N * 2 - 1)
    for j in range(0, N - i):
        row[N - 1 - j] = alphabet[j + i]
        row[N - 1 + j] = alphabet[j + i]
    print("-".join(row))

for i in range(0, N):
    row = ["-"] * (N * 2 - 1)
    for j in range(0, N - i):
        row[N - 1 - j] = alphabet[j + i]
        row[N - 1 + j] = alphabet[j + i]
    print("-".join(row))