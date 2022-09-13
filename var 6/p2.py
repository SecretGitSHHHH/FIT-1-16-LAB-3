import math

r = float(input("Радіус: "))
h = float(input("Висота: "))

S = math.pi * r**2  # math.pi можна замінити на 3.14

V = S * h
Sf = 2 * math.pi * r * h

print("Об'єм:", V)
print("Площа поверхні:", Sf)
