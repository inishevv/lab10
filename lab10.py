import random
import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="a")

def chislo(ch):
    while True:
        user_ch = input(ch)
        try:
            numb = int(user_ch)
            if numb >= 1:
                return numb
            else:
                print('число должно быть больше 1')
                logging.warning('число должно быть больше 1')
        except ValueError:
            print('Введено не число, попробуйте снова')
            logging.warning('Введено не число, попробуйте снова')

print('количество попыток пользователя: ')
logging.warning('количество попыток пользователя: ')
k = chislo('')
logging.warning(k)
print('максимальное число, которое может загадать компьютер: ')
logging.warning('максимальное число, которое может загадать компьютер: ')
n = chislo('')
logging.warning(n)
flag = 0

number = random.randint(1,n)
logging.warning('загаданное число:')
logging.warning(number)

for i in range(k):
    if flag == 0:
        print('введите число')
        a = chislo('')
        logging.warning(a)
        if a < number:
            print("загаданное число больше")
            logging.warning("загаданное число больше")
        elif a > number:
            print("загаданное число меньше")
            logging.warning("загаданное число меньше")
        elif a == number:
            print("вы выиграли!")
            logging.warning('вы выиграли!')
            flag += 1
if flag == 0:
    print('попытки закончились')
    logging.warning('попытки закончились')