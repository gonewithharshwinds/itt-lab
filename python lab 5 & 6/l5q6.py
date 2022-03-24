#!/usr/bin/python3
def fibo(n): return 0 if n==0 else 1 if n==1 else fibo(n-1)+fibo(n-2)
n = int(input("Enter your number\t"))
if n < 0:
    print("Enter a positive number")
elif n == 0:
    print("0")
else:
    for n in range(0, n):  
        print(fibo(n), end = ' ')