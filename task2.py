n = int(input("введите N: "))

if n < 1:
    print("N должно быть больше 0")
else:
    total = 0
    product = 1
    squares = 0
    for i in range(1, n + 1):
        total += i
        product *= i
        squares += i ** 2

    print(f"сумма чисел == {total}")
    print(f"произведение чисел == {product}")
    print(f"сумма квадратов == {squares}")
