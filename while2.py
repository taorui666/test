#!/usr/bin/python3
s = input("Please input string:")
c = len(s)
i = 1
max1=s[0]
while i < c:
    a=s[i]
    i += 1
    if ord(a) > ord(max1):
        max1 = a
print(max1)
 
    
