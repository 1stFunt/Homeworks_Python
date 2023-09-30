# Напишите программу, которая получает целое число и возвращает
# его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.
def custom_hex(number):
    hex_string = ""
    if number == 0:
        hex_string = "0"
    else:
        while number > 0:
            remainder = number % 16
            hex_digit = str(remainder) if remainder < 10 else chr(
                ord('a') + remainder - 10)
            hex_string = hex_digit + hex_string
            number //= 16
    return "0x" + hex_string  # Добавляем "0x" перед строкой, как у функции hex


decimal_number = int(input("Введите целое число: "))
hex_result = custom_hex(decimal_number)
print("Своя функция:", hex_result)
print("Функция hex:", hex(decimal_number))
