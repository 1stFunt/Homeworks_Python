# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.
input_list = [1, 2, 2, 3, 4, 4, 5, 5, 5]
unique_set = set(input_list)
result_list = list(unique_set)
print(result_list)