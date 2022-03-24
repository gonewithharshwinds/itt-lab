#!/usr/bin/python
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Please select operation : \n" \
		"1. Addition \n" \
		"2. Subtraction \n" \
		"3. Multiplication \n" \
		"4. Division \n")
select = int(input("Select operations form 1, 2, 3, 4 :"))
if select == 1:
	print(a, "+", b, "=", add(a,b))
elif select == 2:
	print(a, "-", b, "=", sub(a,b))
elif select == 3:
	print(a, "*", b, "=", mul(a,b))
elif select == 4:
    if b == 0:
        exit
    elif b != 0:
	    print(a, "/", b, "=", div(a,b))
else:
	print("Invalid input")
