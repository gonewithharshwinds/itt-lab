#!/usr/bin/python3
def ispalinls(str): return print("Is palindrome") if str == str[::-1] else print("Is NOT palindrome")
ls = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    a = int(input())
    ls.append(a)
print("The list is :")
print(ls)
ls = ' '.join([str(ad) for ad in ls])
ispalinls(ls)