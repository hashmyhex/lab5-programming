n = int(input("введите число: "))

number = n
reverse = 0
while number > 0:
    reverse = reverse * 10 + number % 10
    number //= 10

if n >= 0 and reverse == n:
    print(f"{n} == палиндром")
else:
    print(f"{n} == не палиндром")

text = input("введите строку: ").lower().replace(" ", "")
if text == text[::-1]:
    print("строка == палиндром")
else:
    print("строка == не палиндром")
