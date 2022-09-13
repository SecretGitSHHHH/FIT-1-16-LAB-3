import sys

a = input("число: ")

if len(a) != 3:
    print("Число не трьохзначне")
    sys.exit()

for i in a:
    print(i)
