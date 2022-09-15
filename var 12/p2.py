a = float(input("A паралелепіпеда: "))
b = float(input("B паралелепіпеда: "))
c = float(input("C паралелепіпеда: "))

k = float(input("Коефіцієнт: "))

a *= k
b *= k
c *= k

print(f"""A под. = {a}
B под. = {b}
C под. = {c}""")

print(f"V = {a*b*c}")

print(f"S = {2*(a*b) + 2*(a*c) + 2*(c*b)}")
