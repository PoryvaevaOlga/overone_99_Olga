# Напишите функцию, вычисляющую значение факториала числа N. Используйте рекурсию
# In: 5
# Out: 120
def factorial(a):
    if a == 0:
        return 1
    else:
        return a * factorial(a - 1)
if __name__:
        n = int(input("введите число "))
        print(factorial(n))