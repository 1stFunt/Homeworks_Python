# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
import math
import csv
import random
import json


def quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)
    elif discriminant == 0:
        root = -b / (2*a)
        return (root,)
    else:
        return ()


def generate_csv(filename, num_rows):
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for _ in range(num_rows):
            row = [random.randint(1, 1000) for _ in range(3)]
            csv_writer.writerow(row)


def quadratic_roots_decorator(csv_filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(csv_filename, 'r') as csvfile:
                csv_reader = csv.reader(csvfile)
                results = []
                for row in csv_reader:
                    a, b, c = map(int, row)
                    result = func(a, b, c)
                    results.append({
                        "input": {"a": a, "b": b, "c": c},
                        "roots": result
                    })
                return results
        return wrapper
    return decorator


def save_to_json(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = func(*args, **kwargs)
            with open(filename, 'w') as jsonfile:
                json.dump(results, jsonfile, indent=4)
        return wrapper
    return decorator


@save_to_json('output.json')
@quadratic_roots_decorator('input.csv')
def find_roots(a, b, c):
    return quadratic_roots(a, b, c)


generate_csv('input.csv', 100)
find_roots()