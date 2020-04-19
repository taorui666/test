w=int(input("wigth"))
i = 1
while i <= w:
    fm='%'+str(w)+"s"
    a="*" * i
    print( fm  % a)
    i += 1
