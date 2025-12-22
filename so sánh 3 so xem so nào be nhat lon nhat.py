a = float(input())
b = float(input())
c = float(input())
max = a
min = a
if b > max:
    max=b
if c> max:
    max=c
if b < min:
    min = b
if c < min:
    min = c
print("Lon nhat:", max)
print("Be nhat:", min)
    