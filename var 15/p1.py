a = input("Число: ")
l = len(a) + 1
a = int(a)

for i in range(1, l):
    n = int(a % 10)
    a /= 10
    print(n, end="")
    if i % 2 == 0:
        print()
