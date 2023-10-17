# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
import random

def are_queens_safe(queens):
    for i in range(8):
        for j in range(i+1, 8):
            if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1]:
                return False
            if abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                return False
    return True

successful_arrangements = []
attempts = 0

while len(successful_arrangements) < 4:
    attempts += 1
    queens = [(random.randint(1, 8), random.randint(1, 8)) for _ in range(8)]

    if are_queens_safe(queens):
        successful_arrangements.append(queens)
        print(f"Успешная расстановка {len(successful_arrangements)}: {queens}")

print(f"Потребовалось {attempts} попыток для нахождения 4 успешных расстановок.")

# Оооочень долго осуществляется подбор
