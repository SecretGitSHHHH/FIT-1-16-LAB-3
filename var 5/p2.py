# a = []
# for i in range(4):                            Виконання через цикл
#     a.append(float(input(f"{i+1}-й кут: ")))
#
# print(360-sum(a))

a = float(input("1-й кут: "))
b = float(input("2-й кут: "))
c = float(input("3-й кут: "))
d = float(input("4-й кут: "))

print((180*3)-a-b-c-d)
