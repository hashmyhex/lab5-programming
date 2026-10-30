try:
    n = int(input("введите N: "))

    if n < 1:
        print("N должно быть больше 0")
    else:
        total = 0
        for i in range(1, n + 1):
            total += 1 / i
        print(f"сумма ряда при N == {n}: {total:.6f}")
except ValueError:
    print("ошибка!!! надо только цифры")
