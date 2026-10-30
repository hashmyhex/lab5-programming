n = int(input("введите число: "))

if n < 2:
    print("число должно быть больше 1")
else:
    number = n
    factors = []
    d = 2
    while d * d <= number:
        while number % d == 0:
            factors.append(d)
            number //= d
        d += 1
    if number > 1:
        factors.append(number)

    print(f"{n} == " + " × ".join(map(str, factors)))
