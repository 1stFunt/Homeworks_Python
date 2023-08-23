# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
def find_duplicates(input_list):
    counter = {}
    duplicates = []
    for element in input_list:
        counter[element] = counter.get(element, 0) + 1
    for element, count in counter.items():
        if count > 1:
            duplicates.append(element)
    return duplicates


input_list = [1, 2, 2, 3, 4, 4, 5, 5, 5]
result = find_duplicates(input_list)
print(result)