#!/usr/bin/python3
s=input("请输入ABCDEFG")
c=len(s) 
if c % 2 == 1:
    c +=1
    c //=2
else: 
    exit()
print(s[c-1])

