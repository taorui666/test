s=input("string:")
#i = 0
#a = 0
#while i < len(s):
#    if s[i].isspace():
#        a += 1
#    i += 1 
#print(a)
#print("--------------------")
i = 0
a = 0
while i < len(s):
    if s[i].isdigit():
        a += 1
        i += 1
    else:
        print("没有数字")
        break
if a == len(s):
    print(a)
