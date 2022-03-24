#!/usr/bin/python3
def recsum(n): return n if n<=1 else n+recsum(n-1)
n = int(input("Enter your number\t"))
if n < 0:
   print("Enter a positive number")
else:
   print("The sum is",recsum(n))