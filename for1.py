s=input("请出如")
a=int(0)
b=int(0)
for i in s:
    if i == "A":
        a += 1
    if i == " ":
        b += 1
print(a)
print("空格：",b)
