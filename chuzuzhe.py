#!/usr/bin/python3
km=int(input("Please Input KM"))
if km < 3 :
    money=13
elif 3 < km < 15 :
    money=13 + (km - 3) * 2.3
elif km > 15:
    money=13 + (km -3) * 2.3 + (km - 15) * 2.3 * .5
print(money)
