#!/usr/bin/python3
s=input("请输入回文")
c=len(s)
12321
if c % 2:
    if  s[:c//2+1] == s[:c//2-1:-1]:
        print("是回文")
    elif s[:c//2+1] != s[:c//2-1:-1]:
        print("不是回文")
else:
    if s[0:c//2] == s[:-(c//2+1):-1]:
        print("是回文")
    else:
        print("不是回文")
        
