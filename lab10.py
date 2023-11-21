import random
import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="a")

k = input()
n = input()
number = random.randint(0,n)
for i in range(k):
    a = int(input())
    logging.warning(a)
    if a < number:
        print("введенное число больше")
    elif a > number:
        print("введенное число меньше")
    elif a == number:
        print("вы выиграли!")
