i=int(input("输入一个数"))
j = 0
a = 0
while j < i:
    j +=1
    a += j
    if j == i:
        print (j,end='=')
    else:
        print("%d" % j ,end='+' )
    
print(a)
    
