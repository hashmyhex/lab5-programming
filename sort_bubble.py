numbers = [64, 25, 12, 22, 11, 90, 3]
print(f"до сортировки: {numbers}")

n = len(numbers)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(f"после сортировки: {numbers}")
