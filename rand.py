import random

def genpwd(length):
    for i in range(length):
        random.randint(i)

length = eval(input())
random.seed(17)
for i in range(3):
    print(genpwd(length))

