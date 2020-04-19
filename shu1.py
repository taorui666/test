#!/usr/bin/python3
x = int(input("please input :"))
for i in range(1,x+1):
    print(' ' * (x-i) + '*' * (2*i-1))
