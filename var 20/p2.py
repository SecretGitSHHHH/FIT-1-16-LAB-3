num = input("Число: ")
l = len(num)

mult = 1

for i in num:
    mult *= int(i)

print(mult**(1/l))
