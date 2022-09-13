a = float(input("Сторона основи A: "))
b = float(input("Сторона основи B: "))

if a != b:
    print("Основа не є квадратом")
    exit()

c = float(input("Висота: "))

print("Площа поверхні:", 2*(a*b + a*c + b*c))
print("Об'єм:", (a*b)*c)

