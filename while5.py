#!/usr/bin/python3
s=int(input('Please Input Line:'))
print('#' * s)
i = 0
while i < s - 2:
    print('#' + ' ' * (s - 2) + '#')
    i += 1
print('#' * s)

