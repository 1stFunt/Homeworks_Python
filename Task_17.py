"""
Напишите функцию группового переименования файлов. Она должна:
принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
принимать параметр количество цифр в порядковом номере.
принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
принимать параметр расширение конечного файла.
принимать диапазон сохраняемого оригинального имени. 
Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
К ним прибавляется желаемое конечное имя, если оно передано. 
Далее счётчик файлов и расширение.
"""
import os


def batch_rename(file_paths, desired_name, num_digits, initial_extension, final_extension, name_range=None):
    counter = 1
    for file_path in file_paths:
        if not os.path.isfile(file_path):
            print(f"Файл '{file_path}' не существует.")
            continue

        file_name = os.path.basename(file_path)
        if file_name.endswith(initial_extension):
            if name_range:
                start, end = name_range
                if start > len(file_name) or end > len(file_name):
                    print(f"Диапазон имен ({start}, {end}) выходит за пределы имени файла {file_name}")
                    continue
                name_part = file_name[start-1:end]
            else:
                name_part = ""

            new_name = f"{desired_name}{name_part}{counter:0{num_digits}d}.{final_extension}"
            new_path = os.path.join(os.path.dirname(file_path), new_name)

            os.rename(file_path, new_path)
            print(f"Переименован файл '{file_name}' в '{new_name}'")
            counter += 1


file_paths = ["1_test.txt", "2_test.txt"]
batch_rename(file_paths, "new_name_", 3, ".txt", "new.txt", name_range=(1, 5))