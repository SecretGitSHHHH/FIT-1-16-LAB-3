# def recSum(number, s=0, i=0):             Виконання через рекурсію
#     number = str(number)
#     if i < len(number):
#         s += int(number[i])
#         return recSum(number, s, i+1)
#     else:
#         return s
#
#
# print(recSum(1234))

a = input("Число: ")
print(int(a[0])+int(a[1])+int(a[2])+int(a[3]))
