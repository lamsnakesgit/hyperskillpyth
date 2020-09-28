# 3 3 3 = 2 2 2 = 6
a = int(input())
b = int(input())
c = int(input())
add = 0
if (a % 2) == 1:
    add += 1
if (b % 2) == 1:
    add += 1
if (c % 2) == 1:
    add += 1
print(int(a / 2) + int(b / 2) + int(c / 2) + add)
