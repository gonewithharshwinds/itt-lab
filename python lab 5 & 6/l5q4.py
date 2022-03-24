#!/usr/bin/python3
m = int(input("Enter no. of rows : \t"))
n = int(input("Enter no. of columns : \t"))
a = []
print("Enter Matrix 1.")
for i in range(n):
   row = list(map(int, input().split()))
   a.append(row)
print(a)
print("\n Your Matrix 2 must have",m,"rows and",n,"columns.")
b = []
for i in range(n):
   row = list(map(int, input().split()))
   b.append(row)
print(b)
res = []
res = [ [ 0 for i in range(m) ] for j in range(n) ]
for i in range(m):
        for j in range(n):
                res[i][j] = a[i][j] + b[i][j]
print(res)