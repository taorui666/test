c=int(input("请输入"))
for j in range(c):
    for i in range(1,c+1):
        print("%3d" % int(i + j) ,end="") 
    print()
