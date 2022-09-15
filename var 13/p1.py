a = input("Число 1: ")
b = input("Число 2: ")


def reverse(num):
    l = len(num)
    output = 0
    num = int(num)
    for i in range(l):
        output *= 10
        output += num % 10
        num = int(num / 10)

    return output


print(reverse(a))
print(reverse(b))
