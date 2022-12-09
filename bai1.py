import os

def bai1(text,file):
    with open(file,mode='w',encoding='utf-8')as f:
        f.write(text)

def main():
    text = str(input('nhap chuoi: '))
    file = str(input('nhap ten tap tin:'))
    bai1(text,file)

if __name__ =='__main__':
    main()
