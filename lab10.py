import random
import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="a")

print('количество попыток пользователя: ')
k = int(input())
print('максимальное число, которое может загадать компьютер: ')
n = int(input())
flag = 0

number = random.randint(1,n)

for i in range(k):
    print('введите число')
    a = int(input())
    logging.warning(a)
    if a < number:
        print("загаданное число больше")
    elif a > number:
        print("загаданное число меньше")
    elif a == number:
        print("вы выиграли!")
        logging.warning('вы выиграли!')
        flag += 1
if flag == 0:
    print('попытки закончились')