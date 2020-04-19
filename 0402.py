#!/usr/bin/python3
import time
sc=50
print("执行开始".center(sc//2,"-"))
for i in range(sc + 1):
    a= '*' * i
    b= '.' * (sc -i)
    c=(i/sc) * 100
    print("\r{:^3.0f}%[{}->{}]".format(c,a,b),end="")
    time.sleep(0.1)
print( "\n" + "执行结束".center(sc//2,"-"))


