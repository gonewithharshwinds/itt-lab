#!/usr/bin/python3
def decimal_to_binary(dec):  
    decimal = int(dec) 
    print(decimal, " in Binary : ", bin(decimal))
def decimal_to_octal(n):  
    decimal = int(n) 
    print(decimal, "in Octal : ", oct(decimal))
def decimal_to_hexadecimal(n):  
    decimal = int(n) 
    print(decimal, "in Hexadecimal : ", hex(decimal))
n = int(input("Enter the number to convert\t"))
decimal_to_binary(n)
decimal_to_octal(n)
decimal_to_hexadecimal(n)