a = input("Число: ")
length = len(a)
a = int(a)

for i in range(length):
    print(a % 10, end="")
    a = int(a / 10)
