#!/usr/bin/python3
m1 = int(input("Enter no. of rows : \t"))
n1 = int(input("Enter no. of columns : \t"))
a = []
print("Enter Matrix 1:\n")
for i in range(n1):
   row = list(map(int, input().split()))
   a.append(row)
print(a)
m2 = int(n1)
print("\n Your Matrix 2 must have",n1,"rows and",m1,"columns \n")
n2 = int(m1)
b = []
for i in range(n2):
   row = list(map(int, input().split()))
   b.append(row)
print(b)
res = []
res = [ [ 0 for i in range(m2) ] for j in range(n1) ]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
                res[i][j] += a[i][k] * b[k][j] 
print(res)