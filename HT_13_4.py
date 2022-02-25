# 13.4 Напишите функцию, которая создает список случайных элементов. На фход функция
# принимает кол-во элементов, минимальное и максимальное значение
# In: rand_nums(7, 2, 12)
# Out: [12, 6, 9, 2, 11, 5, 8]
import random

def rand_nums(n, min, max):
        ls = [random.randint(min, max) for i in range(n)]
        print(ls)
if __name__:
    a = int(input("введите число n "))
    b = int(input("введите число min "))
    c = int(input("введите число max "))
    rand_nums(a, b, c)