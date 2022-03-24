#!/usr/bin/python3
s = input("please enter set 1 elements with spaces")
A = set(s)
s = input("please enter set 2 elements with spaces")
B = set(s)
print("Union :", A | B)
print("Intersection :", A & B)
print("Difference :", A - B)
print("Symmetric difference :", A ^ B)