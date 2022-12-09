import numpy as np
x= np.random.randint(low=-1000, hight = 1000, size = 1000)

file = str(input('nhap ten tap tin:'))

with open(file, mode='w',encoding='utf-8') as f:
    for i in range(1,x+1):
        f.write(str(x[i]))
        if i % 10 == 0:
            f.write('\n')
        else:
            f.write(',')


with open(file,mode='r',encoding='utf-8') as f:
    a = f.readlines()
    for i in a:
        before = line.strip()
        after = before.replace()
        print(after)