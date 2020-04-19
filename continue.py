begin=int(input("begin"))
end=int(input("end"))
while begin < end:
    if begin % 2 == 0:
        begin += 1
        continue
    print(begin)
    begin += 1
