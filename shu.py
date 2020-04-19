#!/usr/bin/python
import time
c=int(input("aaa"))
a=1
for i in range(1,c+1):
    print(" " * (c - i) + "*" * a + " " * (c - i))
    time.sleep(0.5)
    a += 2
for j in range(c):
    print(" " * (c-1) + "*" + " " * (c-1) )
    time.sleep(0.3)

#   *   
#  ***  
# ***** 
#*******
