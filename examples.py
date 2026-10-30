def report():
    pass


numbers = [1, 3, 5, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(f"первое четное == {num}")
        break

total = 0
for num in [5, -3, 8, -1, 10, -7, 2]:
    if num < 0:
        continue
    total += num
print(f"сумма положительных == {total}")

report()
