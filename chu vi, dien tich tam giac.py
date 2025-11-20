a=int(input('Nhap canh thu nhat ='))
b=int(input('Nhap canh thu hai ='))
c=int(input('Nhap canh thu ba ='))
P=(a+b+c)/2
S=(P * (P - a) * (P - b) * (P - c)) ** 0.5
print('chu vi tam giac=',P*2)
print('dien tich tam giac=',S)