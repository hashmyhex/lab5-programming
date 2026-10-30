numbers = [3, 11, 12, 22, 25, 64, 90]
target = int(input("введите число для поиска: "))

left = 0
right = len(numbers) - 1
found = -1
while left <= right:
    middle = (left + right) // 2
    if numbers[middle] == target:
        found = middle
        break
    elif numbers[middle] < target:
        left = middle + 1
    else:
        right = middle - 1

if found == -1:
    print(f"{target} == не найдено")
else:
    print(f"{target} == найдено, индекс {found}")
