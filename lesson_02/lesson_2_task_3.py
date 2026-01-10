import math


def square(side):
    area = side ** 2
    return math.ceil(area)


side = float(input("Введите длину стороны квадрата "))

Result = square(side)

print("Площадь квадрата равна ", Result)
