
def after_file(text, file):
    with open(file, mode='a', encoding='utf-8') as f:
        f.write(text)


def read_file(file):
    with open(file, mode='r', encoding='utf-8') as f:
        f.read(10)
        print(f.read())

def main():
    text = str(input('nhap chuoi ki tu: '))
    file = str(input('nhap ten tap tin '))
    after_file(text, file)
    print('noi dung tap tin la: ',read_file )

if __name__ == '__main__':
    main()