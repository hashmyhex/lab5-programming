import math

print(f"{'x':>10}{'sin(x)':>12}")
print("-" * 22)

step = math.pi / 10
for i in range(11):
    x = step * i
    print(f"{x:10.4f}{math.sin(x):12.4f}")
