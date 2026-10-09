# 1. Считываем три числа
a = int(input())
b = int(input())
c = int(input())

# 2. Проверяем условия
if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)