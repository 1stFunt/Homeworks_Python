# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.
import itertools


def find_possible_combinations(items, max_weight):
    all_combinations = []
    for i in range(1, len(items) + 1):
        combinations = itertools.combinations(items, i)
        all_combinations.extend(combinations)

    valid_combinations = []
    for combination in all_combinations:
        total_weight = sum(item[1] for item in combination)
        if total_weight <= max_weight:
            valid_combinations.append(combination)

    return valid_combinations


items = {
    "Тент": 2.5,
    "Спальник": 1.5,
    "Газ.балон": 0.5,
    "Еда": 1.0,
    "Перчатки": 0.2,
    "Фонарик": 0.3
}

max_weight = 5.0
valid_combinations = find_possible_combinations(items.items(), max_weight)

for combination in valid_combinations:
    print("Допустимый вариант:")
    for item, weight in combination:
        print(f"{item}: {weight} кг")
    print()