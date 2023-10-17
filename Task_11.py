# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
def split_path(file_path):
    parts = file_path.split("/")
    filename_with_extension = parts[-1]
    name, extension = filename_with_extension.split(".")
    return "/".join(parts[:-1]), name, "." + extension


file_path = "/путь/к/файлу/файл.txt"
result = split_path(file_path)
print(result)
