Ax = int(input("Ax: "))                            #           B
Ay = int(input("Ay: "))                            #         /   \
Bx = int(input("Bx: "))                            #       /       \
By = int(input("By: "))                            #      A-------- C

AB = ((Bx-Ax)**2 + (By-Ay)**2)**0.5

AC = -Ax*2

print(f"AB = BC = {AB}")
print(f"AC = {AC}")
