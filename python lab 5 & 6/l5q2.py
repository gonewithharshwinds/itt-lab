#!/usr/bin/python
import itertools
# read
m = int(input("Enter no. of rows : \t"))
n = int(input("Enter no. of columns : \t"))
a = []
# read
for i in range(n):
   row = list(map(int, input().split()))
   a.append(row)
# write
print(a)
at = []
# change
at = list(itertools.zip_longest(*a))
# write
print(at)