# Создайте функцию генератор чисел Фибоначчи.

def Fibbonachi(n: int):
    fib1 = fib2 = 1
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib2

for i, num in enumerate(Fibbonachi(10), start=3):
    print(f'{i} iteration = {num}')