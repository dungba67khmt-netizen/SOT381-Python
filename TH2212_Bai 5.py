n = int(input())
tu = 0
mau = 0
for i in range(1, n + 1):
    tu += i
for i in range(2, n + 1, 2):
    mau += i
S = tu / mau
print('Tong la:',S)