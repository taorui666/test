#!/usr/bin/python3
a = input("1")
b = input("2")
c = input("3")
temp = len(a)
if temp < len(b):
    temp = len(b)
if temp < len(c):
    temp = len (c)

fmt="%" + str(temp) + "s"
print(("%" + str(temp) + "s") % a)
print(("%" + str(temp) + "s") % b)
print(("%" + str(temp) + "s") % c)
