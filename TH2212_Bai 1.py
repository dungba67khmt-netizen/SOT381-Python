while True:
 w=float(input('nhap canh w  '))
 if(w>=0)and(w<=100):
    break
 else:
     print('nhap lai')
while True:
  h=float(input('nhap canh h  '))
  if(h>=0)and(h<=100):
    break
  else:
     print('nhap lai')
P=(w+h)*2
S=(w*h)
print(f"{P:.2f}")
print(f"{S:.2f}")