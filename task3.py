def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


n = int(input("введите N: "))

if n < 1:
    print("N должно быть больше 0")
else:
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

    print(*[fib(i) for i in range(n)])
