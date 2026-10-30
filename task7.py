n = int(input("введите N: "))
m = int(input("введите M: "))

print("прямоугольник")
for i in range(n):
    print("*" * m)

print("треугольник")
for i in range(1, n + 1):
    print("*" * i)

print("ёлочка")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

print("ромб")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
