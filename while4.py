#!/usr/bin/python3
i = 1
k = 1 
while i <= 20:
    print('%3s' % i,end=' ')
    if k >= 5:
        print()
        k = 0
    i += 1
    k += 1
