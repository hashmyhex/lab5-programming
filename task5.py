n = int(input("введите число: "))

number = abs(n)
count = 0
total = 0
product = 1
reverse = 0

if number == 0:
    count = 1
    product = 0

while number > 0:
    digit = number % 10
    count += 1
    total += digit
    product *= digit
    reverse = reverse * 10 + digit
    number //= 10

print(f"количество цифр == {count}")
print(f"сумма цифр == {total}")
print(f"произведение цифр == {product}")
print(f"перевернутое число == {reverse}")
