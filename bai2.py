import os
text = str(input('nhap chuoi: '))
file = str(input('nhap ten tap tin:'))
with open(file, mode='w', encoding='utf-8') as f:
    f.write(text)
    print(f.read(10))