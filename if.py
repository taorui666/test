#!/usr/bin/python3
#n=int(input("请输入一个整数"))
#if n % 2 :
#    print("这个值是奇数")
#else:
#    print("这个值是偶数")



#n=int(input("请输入一个季度"))
#if n == 1 :
#    print("1 2 3")
#elif n == 2 :
#    print("4 5 6")
#elif n == 3 :
#    print("7 8 9")
#elif n == 4 :
#    print("10 11 12")
#else :
#    print("请输入1-4之间")
#elif n > 80:
   # print("在80-100")
#elif n < 0:
   # print("小于0")

n=int(input("请输入一个月份"))
if 1<= n <= 3  :
    print(end="")
elif 4 <= n <= 6 :
    print("2")
elif 7 <= n <= 9 :
    print("3")
elif 10 <= n <= 12 :
    print("4")
else :
    print("请输入1-12之间")
